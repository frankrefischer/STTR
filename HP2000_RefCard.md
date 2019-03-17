# Quick Reference to HP 2000 Time-Shared BASIC

Reference for all commands used in STTR1.

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
|**``** |<code>****</code>||
|**``** |<code>****</code>||
|**``** |<code>****</code>||
|**``** |<code>****</code>||
|**``** |<code>****</code>||
