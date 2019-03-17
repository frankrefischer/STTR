# Quick Reference to HP 2000 Time-Shared BASIC

Reference for all commands used in STTR1.

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
|__`*`__ |<code>130 C5 = (A*B)*N2</code>|Multiply|
|__`/`__ |<code>140 PRINT T5/4<code>|Divide|
|__`+`__ |<code>150 P = R1/10<code>|Add|
|__`-`__ |<code>160 X3 = R3 - P<code>|Subtract|
|__`=`__ |<code>170 IF D = E THEN 600<code>|_expression_ __"equals"__ _expression_|
|__`<>`__ |<code>180 IF D6<>(2*D) THEN 700<code>|_expression_ __"does not equal"__ _expression_|
|__`>`__ |<code>190 IF X>10 THEN 620<code>|_expression_ __"is greater than"__ _expression_|
|__`<`__ |<code>200 IF R8<P7 THEN 640 <code>|_expression_ __"is less than"__ _expression_|
|__`>=`__ |<code>210 IF R8>=P7 THEN 710<code>|_expression_ __"is greater than or equal to"__ _expression_
|__`<=`__ |<code>220 IF X2<=10 THEN 650<code>|_expression_ __"is less than or equal to"__ _expression_

## STATEMENTS

|Full Name|Example|Purpose|
|:---|:---|:---|
|**`REM`** |<code>630 **REM** ANY TEXT</code>|Inserts non-executable remarks in a program.||
|**`GOSUB`** |<code>470 **GOSUB** 800</code>|Begins executing the subroutine at specified statement (see `RETURN`)|
|**`PRINT`** |<code>540 **PRINT** A,B,C$</code>|Prints the specified values; 5 fields per line when commas are used as separators, 12 when semicolons are used.|
|**`INPUT`** |<code>510 **INPUT** X$,Y2,B4</code>|Allows data to be entered from terminal while program is running.|
|<code>**IF&nbsp;...&nbsp;THEN**</code> |<code>490&nbsp;**IF**&nbsp;A#10&nbsp;**THEN**&nbsp;350</code>|Logical test; transfers control to statement number if "true".|
|**``** |<code>****</code>||
