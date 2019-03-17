# STTR1 DATA DICTIONARY

|Variable name|Variable type|Meaning|Possible values|
|:---|:---|:---|:---|
|__`A`__||Used as buffer for command input|`0 = SET COURSE`<br>`1 = SHORT RANGE SENSOR SCAN`<br>`2 = LONG RANGE SENSOR SCAN`<br>`3 = FIRE PHASERS`<br>`4 = FIRE PHOTON TORPEDOES`<br>`5 = SHIELD CONTROL`<br>`6 = DAMAGE CONTROL REPORT`<br>`7 = CALL ON LIBRARY COMPUTER`<br>|
|__`A`__||Used as buffer for computer command input|`0 = CUMULATIVE GALACTIC RECORD`<br>`1 = STATUS REPORT`<br>`2 = PHOTON TORPEDO DATA`|
|__`A$`__|__`DIM A$(3)`__|Used as buffer for user input|`"YES"`<br>`"NO"` |
|__`A$`__|__`DIM A$(3)`__|Used as buffer for short range scan objects.|`"___" EMPTY`<br>`"<*>" ENTERPRISE`<br>`"+++" KLINGON`<br>`">!<" STARBASE`<br>`" * " STAR`|
|__`B1`__||Used as buffer for course or torpedo course input|`0 = cancel command`<br>`1-8 =valid course`<br>`others = input course again`|
|__`B3`__||||
|__`B9`__||Number of starbases left.||
|__`C`__|__`DIM C[9,2]`__|||
|__`C1`__||||
|__`C2`__||||
|__`C$`__|__`DIM C$[6]`__|Condition|`DOCKED`<br>`GREEN`<br>`RED`<br>`YELLOW`|
|__`D`__|__`MAT D`__|Damage info, 8 elements.|`D[1]: WARP ENGINE DAMAGE`<br>`D[2]: SHORT RANGE SENSOR DAMAGE`<br>`D[3]: LONG RANGE SENSOR DAMAGE`<br>`D[4]: PHASER CONTROL DAMAGE`<br>`D[5]: PHOTON TUBES DAMAGE`<br>`D[6]: DAMAGE CONTROL DAMAGE`<br>`D[7]: SHIELD CONTROL DAMAGE`<br>`D[8]: COMPUTER DAMAGE`<br>|
|__`D0`__|||`0 = NOT DOCKED?`<br>`1 = DOCKED?`|
|__`D$`__|__`DIM D$[72]`__||`"WARP ENGINESS.R. SENSORSL.R. SENSORSPHASER CNTRLPHOTON TUBESDAMAGE CNTRL"`|
|__`E`__||Units of energy.|<code>&le;3000</code>|
|__`E0`__||Maximum energy.|`3000`|
|__`E$`__|__`DIM E$[24]`__||`"SHIELD CNTRLCOMPUTER"`|
|__`G`__|__`DIM G[8,8]`__|||
|__`H`__||Hit points on Enterprise or on Klingon.||
|__`H8`__||||
|__`I`__||||
|__`J`__||||
|__`K`__|__`DIM G[3,3]`__|Klingon data.|<code>K[I,1],K[I,2]&nbsp;=&nbsp;sector&nbsp;coordinates&nbsp;of&nbsp;Klingon&nbsp;I</code><br><code>K[I,3]&nbsp;=&nbsp;hit&nbsp;points&nbsp;left&nbsp;on&nbsp;Klingon&nbsp;I</code><br>`with I from 1 to 3`|
|__`K3`__||||
|__`K7`__||||
|__`K9`__||Number of Klingons left.||
|__`N`__|__``__|||
|__`N`__|__`DIM N[3]`__|||
|__`P`__||Number of available photon torpedoes.||
|__`P0`__||||
|__`Q1`__||Current quadrant x-coordinate.||
|__`Q2`__||Current quadrant y-coordinate.||
|__`Q$`__|__`DIM Q$[72]`__|||
|__`R1`__||||
|__`R2`__||||
|__`R$`__|__`DIM R$[72]`__|||
|__`S`__||Shields value.|&le; 200: dangerously low|
|__`S1`__||Current sector x-coordinate.||
|__`S2`__||Current sector y-coordinate.||
|__`S3`__||||
|__`S8`__||||
|__`S9`__||||
|__`S$`__|__`DIM S$[48]`__|||
|__`T`__||||
|__`T0`__||Current stardate.||
|__`T7`__||||
|__`T9`__||Number of stardates left.||
|__`W1`__||Used as input buffer for warp factor.|`1-8 = valid warp factor`<br>`others =  input course again`|
|__`X`__||Used as torpedo track x-coordinate.||
|__`X1`__||||
|__`X2`__||||
|__`Y`__||Used as torpedo track y-coordinate.||
|__`Z`__|__`DIM Z[8,8]`__|||
|__`Z1`__||||
|__`Z2`__||||
|__`Z3`__||||
|__`Z$`__|__`DIM Z$[72]`__|||
