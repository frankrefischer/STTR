# STTR1 DATA DICTIONARY

|Variable name|Variable type|Meaning|Possible values|
|:---|:---|:---|:---|
|__`A$`__|__`DIM A$(3)`__|Used as buffer for user input|`"YES"`<br>`"NO"` |
|__`A$`__|__`DIM A$(3)`__|Used as buffer for short range scan objects.|`"___" EMPTY`<br>`"<*>" ENTERPRISE`<br>`"+++" KLINGON`<br>`">!<" STARBASE`<br>`" * " STAR`|
|__`B3`__||||
|__`B9`__||Number of starbases.||
|__`C`__|__`DIM C[9,2]`__|||
|__`C$`__|__`DIM C$[6]`__|||
|__`D`__|__`MAT D`__|Damage info, 8 elements.||
|__`D0`__||||
|__`D$`__|__`DIM D$[72]`__||`"WARP ENGINESS.R. SENSORSL.R. SENSORSPHASER CNTRLPHOTON TUBESDAMAGE CNTRL"`|
|__`E`__||||
|__`E0`__||||
|__`E$`__|__`DIM E$[24]`__||`"SHIELD CNTRLCOMPUTER"`|
|__`G`__|__`DIM G[8,8]`__|||
|__`H8`__||||
|__`I`__||||
|__`J`__||||
|__`K`__|__`DIM G[3,3]`__|||
|__`K3`__||||
|__`K7`__||||
|__`K9`__||Number of Klingons to destroy.||
|__`N`__|__`DIM N[3]`__|||
|__`P`__||||
|__`P0`__||||
|__`Q1`__||||
|__`Q2`__||||
|__`Q$`__|__`DIM Q$[72]`__|||
|__`R1`__||||
|__`R$`__|__`DIM R$[72]`__|||
|__`S`__||Shields value.|&le; 200: dangerously low|
|__`S1`__||||
|__`S3`__||||
|__`S9`__||||
|__`S$`__|__`DIM S$[48]`__|||
|__`T`__||||
|__`T0`__||||
|__`T7`__||||
|__`T9`__||Number of stardates in which all Klingons must be destroyed.||
|__`X`__||||
|__`Z`__|__`DIM Z[8,8]`__|||
|__`Z$`__|__`DIM Z$(72)`__|||
|__`Z$`__|__`DIM Z$[72]`__|||
