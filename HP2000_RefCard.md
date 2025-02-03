# Quick Reference to HP 2000 Time-Shared BASIC

Reference for all commands used in STTR1.

## SIMPLE VARIABLE

A letter from A to Z; or a letter immediately followed by a number (from 0 to 9).  
Examples: A0, B, M5, C2, Z9, D

Variables are used to represent numeric values.

There are two other types of variables, string variables and array variables.

## FORMATTED OUTPUT

The following format specifiers are used in STTR1:

|Format specifier|Meaning|
|:---|:---|
|__D__|one digit|
|__3D__|3 digits, left padded with spaces|
|__4D__|4 digits, left padded with spaces|
|__5D__|5 digits, left padded with spaces|
|__6D__|6 digits, left padded with spaces|
|__8X__|8 spaces|
|__9X__|9 spaces|
|__11X__|11 spaces|
|__15X__|15 spaces|
|__3A__|3 characters of a string; left padded with whitespace?|
|__6A__|6 characters of a string; left padded with whitespace?|
|__3(3D," :")__|3 times: 3 digits followed by " :"|
|__8(X,3A)__|8 times: 1 space followed by 3 characters of a string|
|__8(3X,3D)__|8 times: 3 characters of a string followed by 3 digits|


## FUNCTIONS
_Functions return a numeric result; they may be used as expressions or parts of expressions. PRINT is used for examples only; other statement types may be used._

|Full Name|Example&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Purpose|
|:---|:---|:---|
|__`DEF FN`__ |<code>__DEF FNA__(X)=(M*X)+B</code>|Allows the programmer to define functions; the function label (A) must be a letter from A to Z; the argument(X) is a dummy variable.|
|__`ABS(X)`__|<code>310 PRINT __ABS(X)__</code>|Gives the absolute value of the expression (X).|
|__`INT(X)`__|<code>330 PRINT __INT(X)__</code>|Gives the largest integer &le; the expression (X).|
|__`RND(X)`__|<code>350 PRINT __RND(X)__</code>|Generates a random number greater than or equal to 0 and less than 1; the argument (X) may have any value. A negative argument is used to restart a sequence of random numbers.|
|__`SQR(X)`__|<code>360 PRINT __SQR(X)__</code>|Gives the square root of the expression (X); expression must have a positive value.|
|__`TIM(X)`__|<code>460 PRINT __TIM(X)__</code>|Gives current minute (X=0) 0-59 or hour (X=1) 0-23.|

## MATRICES
_NOTES:_
1. _Absolute maximum matrix size is 4900 elements._
2. _Matrix variables must be a single letter from A to Z._

|Name|Sample Statement|Purpose|
|:---|:---|:---|
|__`DIM`__|<code>10 __DIM__ A (10,20)</code>|Allocates space for a matrix of the specified dimensions.|
|__`MAT ZER`__|<code>__MAT__  B=__ZER__</code>|Sets all elements of the specified matrix equal to 0.|

## STRINGS
_NOTES:_
1. _A string is 1 to 72 characters enclosed in quotes; it may be assigned to a string variable (an A to Z letter followed by a $)._
2. _Each string variable used in a program must be dimensional (with a DIM statement) if it has a length of more than one character. The DIM sets the physical or maximum length of a string._
3. _Substrings are described by subscripted string variables. For example, if A$ = "ABCDEF", A$(2,2) = B, A$(1,4) = "ABCD" and A$(3) = "CDEF"._

|Full Name/Symbol|Example (Abbreviation)|Purpose|
|:---|:---|:---|
|__`DIM`__ |<code>10 __DIM__ A$ (27)</code>|Declares maximum string length in characters.|
|__`=`__ |<code>20 A$="**TEXT1</code>|Assigns the character string in quotes to a string variable.|
|__`=`__ |<code>105&nbsp;IF&nbsp;A$=C$&nbsp;THEN&nbsp;600</code>|Allows comparison of strings, and substrings and transfer to a specified statement if the comparison is true. Comparison is made in ASCII codes, character by character, left to right until a difference is found.|
|__`INPUT`__ |<code>205 __INPUT__ N$</code>|Accepts as many characters as the string can hold (followed by a _return_). The characters need not be in quotation marks.|

## OPERATORS

_NOTE: The numeric values used in logical evaluation are:_
* _"true" = any nonzero number_
* _"false" = 0_

|Symbol|Sample Statement|Purpose/Meaning/Type|
|:---|:---|:---|
|__`=`__ |<code>100 A = B = C = 0</code>|Assignment operator; assigns a value to a variable.|
|__`^`__|<code>120 PRINT X^2</code>|Exponentiate (as in X²).|
|__`*`__ |<code>130 C5 = (A*B)*N2</code>|Multiply|
|__`/`__ |<code>140 PRINT T5/4<code>|Divide|
|__`+`__ |<code>150 P = R1/10<code>|Add|
|__`-`__ |<code>160 X3 = R3 - P<code>|Subtract|
|__`=`__ |<code>170 IF D = E THEN 600<code>|_expression_ __"equals"__ _expression_|
|__`<>`__ |<code>180 IF D6<>(2*D) THEN 700<code>|_expression_ __"does not equal"__ _expression_|
|__`>`__ |<code>190 IF X>10 THEN 620<code>|_expression_ __"is greater than"__ _expression_|
|__`<`__ |<code>200 IF R8<P7 THEN 640 <code>|_expression_ __"is less than"__ _expression_|
|__`>=`__ |<code>210 IF R8>=P7 THEN 710<code>|_expression_ __"is greater than or equal to"__ _expression_|
|__`<=`__ |<code>220 IF X2<=10 THEN 650<code>|_expression_ __"is less than or equal to"__ _expression_|

## STATEMENTS

|Full Name|Example|Purpose|
|:---|:---|:---|
|__`END`__ |<code>390 __END__</code>|Terminates the program; the last statement in a program must be an END statement.|
|__`FOR...NEXT`__ |<code>440 __FOR__ J=1 __TO__ N</code>|Executes statements between FOR and NEXT the specified number of times (a loop), incrementing the variable by 1.|
|__`GOTO`__ |<code>450 __GOTO__ 900</code>|Transfers control (jumps) to specified statement number.|
|__`GOTO...OF`__ |<code>460 __GOTO__ _n_ __OF__ 100,10,20</code>|Transfers control to the _n_th statement of the statements listed after "OF".|
|__`GOSUB`__ |<code>470 __GOSUB__ 800</code>|Begins executing the subroutine at specified statement (see `RETURN`)|
|__`IF...THEN`__ |<code>490 __IF__ A<>10 THEN 350</code>|Logical test; transfers control to statement if "true".|
|__`IMAGE`__ |<code>500 __IMAGE__ 6D,AA,SD,5DE</code>|Used to specify the format of a PRINT USING statement.|
|__`INPUT`__ |<code>510 __INPUT__ X$,Y2,B4</code>|Allows data to be entered from terminal while program is running.|
|<code>__IF&nbsp;...&nbsp;THEN__</code> |<code>490&nbsp;**IF**&nbsp;A#10&nbsp;**THEN**&nbsp;350</code>|Logical test; transfers control to statement number if "true".|
|__`NEXT`__|<code>530 __NEXT__ J</code>|Marks the end of the FOR loop.|
|__`PRINT`__ |<code>540&nbsp;__PRINT__&nbsp;A,B,C$</code>|Prints the specified values; 5 fields per line when commas are used as separators, 12 when semicolons are used.|
||<code>550 __PRINT__</code>|Causes the terminal to advance one line.|
||<code>580&nbsp;__PRINT&nbsp;USING__&nbsp;"3A";A$</code><br><code>590&nbsp;__PRINT&nbsp;USING__&nbsp;A$;A,B4</code><br><code>600&nbsp;__PRINT&nbsp;USING__&nbsp;200;N,A$</code>|Prints the specified data according to the specified format. The format can be a string, a string variable or the statement number of an image statement containing the format string (200). The format is optionally followed by a semicolon and an expression list (A,B4).|
|__`REM`__ |<code>630 __REM__ ANY TEXT</code>|Inserts non-executable remarks in a program.||
|__`RETURN`__ |<code>660 __RETURN__</code>|Subroutine exit; transfers control to the statement following the matching GOSUB.|

The PRINT statement provides a simple and direct means for BASIC programs to display values on your terminal.  
The items to be printed (print list) are evaluated and displayed in sequential order from left to right in one or more lines. Each item in the print list is separated from the following one by either a semicolon or a comma.  
A semicolon serves only to separate items in the print list; the first character of the following item's value is printed immediately after the last character of the preceding item's value.  
A new line is begun whenever the next value will not fit on the remainder of the current line.

A comma serves another purpose besides separating print list items.  
Each line on the terminal is divided into four consecutive fields of 15 character positions and a final field of 12 character positions (72 character positions per line).  
When a comma follows an item which did not completely fill the last of the one or more fields its value occupies, blanks are added to complete that field.  
Thus the value of an item following a comma always begins at the start of a field.  
If the previously completed field was the last one in the current line, the next item's value will be printed on a new line.  
Since most values occupy less than fifteen character positions, the usual effect is a table of five columns per line.

If a comma or semicolon follows the last item in the print list, the print list of the next PRINT statement executed will be printed as a continuation of the current line.  
Otherwise, the current line is completed and the next PRINT statement will begin printing values on the next line.  
A PRINT statement with no item list either completes the previous line, if it ended with a comma or semicolon, or skips the current line.  
This is frequently used to produce a blank line.
