# Quick Reference to HP 2000 Time-Shared BASIC

Reference for all commands used in STTR1.

## FUNCTIONS
_Functions return a numeric result; they may be used as expressions or parts of expressions. PRINT is used for examples only; other statement types may be used._

|Full Name|Example&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Purpose|
|:---|:---|:---|
|__`DEF FN`__ |<code>__DEF FNA__(X)=(M*X)+B</code>|Allows the programmer to define functions; the function label (A) must be a letter from A to Z; the argument(X) is a dummy variable.|
|__`ABS(X)`__|<code>310 PRINT __ABS(X)__</code>|Gives the absolute value of the expression (X).|
|__`INT(X)`__|<code>330 PRINT __INT(X)__</code>|Gives the largest integer &le; the expression (X).|
|__`RND(X)`__|<code>350 PRINT __RND(X)__</code>|Generates a random number greater than or equal to 0 and less than 1; the argument (X) may have any value. A negative argument is used to restart a sequence of random numbers.|
|__`SQR(X)`__|<code>360 PRINT __SQR(X)__</code>|Gives the square root of the expression (X); expression must have a positive value.|
|__`TIM(X)`__|<code>460 PRINT __TIM(X)__</code>|Gives current minute (X=0) or day (X=1).|

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
|__`>=`__ |<code>210 IF R8>=P7 THEN 710<code>|_expression_ __"is greater than or equal to"__ _expression_
|__`<=`__ |<code>220 IF X2<=10 THEN 650<code>|_expression_ __"is less than or equal to"__ _expression_

## STATEMENTS

|Full Name|Example|Purpose|
|:---|:---|:---|
|__`REM`__ |<code>630 __REM__ ANY TEXT</code>|Inserts non-executable remarks in a program.||
|__`GOSUB`__ |<code>470 __GOSUB__ 800</code>|Begins executing the subroutine at specified statement (see `RETURN`)|
|__`PRINT`__ |<code>540 __PRINT__ A,B,C$</code>|Prints the specified values; 5 fields per line when commas are used as separators, 12 when semicolons are used.|
|__`INPUT`__ |<code>510 __INPUT__ X$,Y2,B4</code>|Allows data to be entered from terminal while program is running.|
|<code>__IF&nbsp;...&nbsp;THEN__</code> |<code>490&nbsp;**IF**&nbsp;A#10&nbsp;**THEN**&nbsp;350</code>|Logical test; transfers control to statement number if "true".|
|__`END`__ |<code>390 __END__</code>||
|__`FOR...NEXT`__ |<code>440 __FOR__ J=1 __TO__ N <...> __NEXT__ J</code>|Executes statements between FOR and NEXT the specified number of times (a loop), incrementing the variable by 1.|
|__`GOTO`__ |<code>450 __GOTO__ 900</code>|Transfers control (jumps) to specified statement number.|
|__`GOTO...OF`__ |<code>460 __GOTO__ _n_ __OF__ 100,10,20</code>|Transfers control to the _n_th statement of the statements listed after "OF".|
|__`IF...THEN`__ |<code>___</code>||
|__`IMAGE`__ |<code>___</code>||
