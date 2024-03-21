import traceback
from pathlib import Path
from typing import List, Optional, Iterable


def main():
    filepath = Path(__file__).absolute().parent.parent / 'STTR1'

    all_code_blocks = list(parse(code=filepath.read_text()))

    markdown_lines = [
        "```mermaid",
        "flowchart LR",
        *[
            f'{cb.start_line_number}["{cb.start_line_number}-{cb.end_line_number}"]\n'
            f"{cb.start_line_number} --> {' & '.join(map(str, cb.possible_next_line_numbers))}"
            for cb in all_code_blocks
        ],
        "```"
    ]

    markdown_filepath = filepath.with_name(filepath.name + '-flow.md')
    markdown_filepath.write_text("\n".join(markdown_lines))


def collect_targets(lines: List[str]) -> List[int]:
    targets = []
    for line_text, next_line_text in zip(lines, lines[1:] + [None]):
        line_text: str
        next_line_text: str
        line_number = None
        next_line_number = None
        if len(line_text) > 0 and line_text[0].isdigit():
            line_number = int(line_text.split(' ')[0])
        if len(line_text) == 0 or not line_text[0].isdigit():
            continue
        next_line_number = None
        if next_line_text is not None and len(next_line_text) > 0 and next_line_text[0].isdigit():
            next_line_number = int(next_line_text.split(' ')[0])
        if line_number is None:
            continue

        is_gosub = 'GOSUB' in line_text
        is_goto = 'GOTO' in line_text
        is_goto_of = is_goto and 'OF' in line_text
        is_if_then = 'THEN' in line_text

        line_parts = line_text.split(' ')
        if is_gosub or is_if_then:
            targets += [int(line_parts[-1]), next_line_number]
        elif is_goto_of:
            targets += [int(x) for x in line_parts[-1].split(',')]
            if next_line_number is not None:
                targets.append(next_line_number)
        elif is_goto:
            targets.append(int(line_parts[-1]))

    return targets


class LINE:
    def __init__(self, line: str, next_line: Optional[str], targets: List[int]):
        self.text = line

        parts: List[str] = line.split(' ')

        self.line_number: int = int(parts[0])

        is_goto = 'GOTO' in line
        is_goto_of = is_goto and 'OF' in line
        is_if_then = 'THEN' in line
        is_return = 'RETURN' in line
        is_gosub = 'GOSUB' in line

        next_line_number = None if next_line is None else int(next_line.split(' ')[0])
        is_next_line_start_of_new_block = next_line_number is not None and next_line_number in targets

        self.is_end_of_code_block = is_goto or is_if_then or is_return or is_gosub or is_next_line_start_of_new_block
        self.possible_next_line_numbers = []
        if is_goto_of:
            self.possible_next_line_numbers += [int(x) for x in parts[-1].split(',')]
        elif is_goto or is_if_then:
            self.possible_next_line_numbers += [int(parts[-1])]
        elif is_next_line_start_of_new_block:
            self.possible_next_line_numbers += [next_line_number]

        if next_line_number is not None and (is_gosub or is_if_then or is_next_line_start_of_new_block):
            self.possible_next_line_numbers += [next_line_number]

    def __str__(self):
        return f'{self.line_number} {self.is_end_of_code_block} {self.possible_next_line_numbers}'


class CodeBlock:
    def __init__(self):
        self.start_line_number: Optional[int] = None
        self.end_line_number: Optional[int] = None
        self.possible_next_line_numbers: List[int] = []
        self.is_complete = False

    def add_line(self, line: LINE):
        assert not self.is_complete
        assert self.start_line_number is None or line.line_number > self.start_line_number
        assert self.end_line_number is None

        if self.start_line_number is None:
            self.start_line_number = line.line_number

        self.end_line_number = line.line_number

        if line.is_end_of_code_block:
            self.possible_next_line_numbers = line.possible_next_line_numbers
            self.is_complete = True

    def __str__(self):
        return f'{self.start_line_number} {self.end_line_number} {self.is_complete} {self.possible_next_line_numbers}'


def parse(code: str) -> Iterable[CodeBlock]:
    lines = [l
             for l in code.split(sep='\n')
             if len(l) > 0 and l[0].isdigit()]
    targets = collect_targets(lines)
    print(targets)
    i: int = 0
    code_block: CodeBlock = CodeBlock()
    for i, (line_text, next_line_text) in enumerate(zip(lines, lines[1:] + [None]), start=1):
        try:
            line = LINE(line=line_text, next_line=next_line_text, targets=targets)
            if line.is_end_of_code_block:
                yield code_block
                print(code_block)
                code_block = CodeBlock()

            code_block.add_line(line=line)
        except Exception as e:
            traceback.print_exception(e)
            print(f'line={i}')
            print(line_text)
            exit(1)


if __name__ == '__main__':
    main()
