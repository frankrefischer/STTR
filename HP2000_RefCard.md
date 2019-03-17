# Quick Reference to HP 2000 Time-Shared BASIC

Reference for all commands used in STTR1.

## OPERATORS

_NOTE: The numeric values used in logical evaluation are:_
* _"true" = any nonzero number_
* _"false" = 0_

|Symbol|Sample Statement|Purpose/Meaning/Type|
|:---|:---|:---|
|__`=`__ |<code>__100 A = B = C = 0__ </code>||
|__`*`__ |<code>____</code>||
|__`/`__ |<code>____<code>||
|__`+`__ |<code>____<code>||
|__`-`__ |<code>____<code>||
|__`=`__ |<code>____<code>||
|__`<>`__ |<code>____<code>||
|__`>`__ |<code>____<code>||
|__`<`__ |<code>____<code>||
|__`>=`__ |<code>____<code>||
|__`<=`__ |<code>____<code>||

## STATEMENTS

|Full Name|Example|Purpose|
|:---|:---|:---|
|**`REM`** |<code>630 **REM** ANY TEXT</code>|Inserts non-executable remarks in a program.||
|**`GOSUB`** |<code>470 **GOSUB** 800</code>|Begins executing the subroutine at specified statement (see `RETURN`)|
|**`PRINT`** |<code>540 **PRINT** A,B,C$</code>|Prints the specified values; 5 fields per line when commas are used as separators, 12 when semicolons are used.|
|**`INPUT`** |<code>510 **INPUT** X$,Y2,B4</code>|Allows data to be entered from terminal while program is running.|
|<code>**IF&nbsp;...&nbsp;THEN**</code> |<code>490&nbsp;**IF**&nbsp;A#10&nbsp;**THEN**&nbsp;350</code>|Logical test; transfers control to statement number if "true".|
|**`LET`** |<code>520 **LET** A=C=B=0</code>|Assigns variable a value. LET is optional.|
|**``** |<code>****</code>||
|**``** |<code>****</code>||
|**``** |<code>****</code>||
|**``** |<code>****</code>||
|**``** |<code>****</code>||
|**``** |<code>****</code>||
