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
|__`E`__|`integer`|Current units of energy; initialized to __`E0`__.|`0-3000`|
|__`E0`__|`integer`|Maximum energy.|`3000`|
|__`E$`__|__`DIM E$[24]`__||`"SHIELD CNTRLCOMPUTER"`|
|__`G`__|__`DIM G[8,8]`__|||
|__`H`__||Hit points on Enterprise or on Klingon.||
|__`H8`__||Mysterious. Checked for H8 = 1 but set to 0. Looks like its a useless variable|´0´|
|__`I`__||||
|__`J`__||||
|__`K`__|__`DIM G[3,3]`__|Klingon data.|<code>K[I,1],K[I,2]&nbsp;=&nbsp;sector&nbsp;coordinates&nbsp;of&nbsp;Klingon&nbsp;I</code><br><code>K[I,3]&nbsp;=&nbsp;hit&nbsp;points&nbsp;left&nbsp;on&nbsp;Klingon&nbsp;I</code><br>`with I from 1 to 3`|
|__`K3`__||||
|__`K7`__||||
|__`K9`__||Number of Klingons left.||
|__`N`__|__``__|||
|__`N`__|__`DIM N[3]`__|||
|__`P`__||Number of available photon torpedoes.|`0-10`|
|__`P0`__||Never used. Looks like it should be the maximum number of torpedoes.|`10`|
|__`Q1`__|`integer`|Current quadrant x-coordinate; initialized to random value.|`1-8`|
|__`Q2`__|`integer`|Current quadrant y-coordinate; initialized to random value.|`1-8`|
|__`Q$`__|__`DIM Q$[72]`__|||
|__`R1`__||||
|__`R2`__||||
|__`R$`__|__`DIM R$[72]`__|||
|__`S`__||Number of energy units on shields.|<code>&lt; 0: enterprise destroyed</code><br><code>&le; 200: dangerously low</code>|
|__`S1`__|`integer`|Current sector x-coordinate; initialized to random value.|`1-8`|
|__`S2`__|`integer`|Current sector y-coordinate; initialized to random value.|`1-8`|
|__`S3`__||||
|__`S8`__||||
|__`S9`__||Initial hit points for Klingons.|`200`|
|__`S$`__|__`DIM S$[48]`__|||
|__`T`__|`integer`|Start stardate initialized to __`T0`__.|from `T0` to `T0+T9`|
|__`T0`__|`integer`|Current stardate; initialized to a random value from 2000 to 3900.|´2000-3900´|
|__`T7`__||||
|__`T9`__|`integer`|Number of stardates, in which player must succeed.|30|
|__`W1`__||Used as input buffer for warp factor.|`1-8 = valid warp factor`<br>`others =  input course again`|
|__`X`__||Used as torpedo track x-coordinate.||
|__`X1`__||||
|__`X2`__||||
|__`Y`__||Used as torpedo track y-coordinate.||
|__`Z`__|__`DIM Z[8,8]`__|||
|__`Z1`__||||
|__`Z2`__||||
|__`Z3`__||||
|__`Z$`__|__`DIM Z$[72]`__||String with 70 whitespaces.|
