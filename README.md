# ZellerDayCalculation

 <h2 align="center"> Calculation of the day of given date with the help of Zeller's Rule</h2>
 
 Formula
For the Gregorian calendar, Zeller's congruence is

{\displaystyle h=\left(q+\left\lfloor {\frac {13(m+1)}{5}}\right\rfloor +K+\left\lfloor {\frac {K}{4}}\right\rfloor +\left\lfloor {\frac {J}{4}}\right\rfloor -2J\right){\bmod {7}},}{\displaystyle h=\left(q+\left\lfloor {\frac {13(m+1)}{5}}\right\rfloor +K+\left\lfloor {\frac {K}{4}}\right\rfloor +\left\lfloor {\frac {J}{4}}\right\rfloor -2J\right){\bmod {7}},}
for the Julian calendar it is

{\displaystyle h=\left(q+\left\lfloor {\frac {13(m+1)}{5}}\right\rfloor +K+\left\lfloor {\frac {K}{4}}\right\rfloor +5-J\right){\bmod {7}},}{\displaystyle h=\left(q+\left\lfloor {\frac {13(m+1)}{5}}\right\rfloor +K+\left\lfloor {\frac {K}{4}}\right\rfloor +5-J\right){\bmod {7}},}
where

h is the day of the week (0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday)
q is the day of the month
m is the month (3 = March, 4 = April, 5 = May, ..., 14 = February)
K the year of the century ({\displaystyle year{\bmod {1}}00}{\displaystyle year{\bmod {1}}00}).
J is the zero-based century (actually {\displaystyle \lfloor year/100\rfloor }\lfloor year/100\rfloor ) For example, the zero-based centuries for 1995 and 2000 are 19 and 20 respectively (not to be confused with the common ordinal century enumeration which indicates 20th for both cases).
{\displaystyle \lfloor ...\rfloor }{\displaystyle \lfloor ...\rfloor } is the floor function or integer part
mod is the modulo operation or remainder after division
In this algorithm January and February are counted as months 13 and 14 of the previous year. E.g. if it is 2 February 2010, the algorithm counts the date as the second day of the fourteenth month of 2009 (02/14/2009 in DD/MM/YYYY format)

For an ISO week date Day-of-Week d (1 = Monday to 7 = Sunday), use

{\displaystyle d=((h+5){\bmod {7}})+1}{\displaystyle d=((h+5){\bmod {7}})+1}
Analysis
These formulas are based on the observation that the day of the week progresses in a predictable manner based upon each subpart of that date. Each term within the formula is used to calculate the offset needed to obtain the correct day of the week.

For the Gregorian calendar, the various parts of this formula can therefore be understood as follows:

{\displaystyle q}q represents the progression of the day of the week based on the day of the month, since each successive day results in an additional offset of 1 in the day of the week.
{\displaystyle K}K represents the progression of the day of the week based on the year. Assuming that each year is 365 days long, the same date on each succeeding year will be offset by a value of {\displaystyle 365{\bmod {7}}=1}{\displaystyle 365{\bmod {7}}=1}.
Since there are 366 days in each leap year, this needs to be accounted for by adding another day to the day of the week offset value. This is accomplished by adding {\displaystyle \left\lfloor {\frac {K}{4}}\right\rfloor }\left\lfloor {\frac  {K}{4}}\right\rfloor  to the offset. This term is calculated as an integer result. Any remainder is discarded.
Using similar logic, the progression of the day of the week for each century may be calculated by observing that there are 36,524 days in a normal century and 36,525 days in each century divisible by 400. Since {\displaystyle 36525{\bmod {7}}=6}{\displaystyle 36525{\bmod {7}}=6} and {\displaystyle 36524{\bmod {7}}=5}{\displaystyle 36524{\bmod {7}}=5}, the term {\displaystyle \left\lfloor {\frac {J}{4}}\right\rfloor -2J}\left\lfloor {\frac  {J}{4}}\right\rfloor -2J accounts for this.
The term {\displaystyle \left\lfloor {\frac {13(m+1)}{5}}\right\rfloor }\left\lfloor {\frac  {13(m+1)}{5}}\right\rfloor  adjusts for the variation in the days of the month. Starting from January, the days in a month are {31, 28/29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}. February's 28 or 29 days is a problem, so the formula rolls January and February around to the end so February's short count will not cause a problem. The formula is interested in days of the week, so the numbers in the sequence can be taken modulo 7. Then the number of days in a month modulo 7 (still starting with January) would be {3, 0/1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3}. Starting in March, the sequence basically alternates 3, 2, 3, 2, 3, but every five months there are two 31-day months in a row (July–August and December–January).[1] The fraction 13/5 = 2.6 and the floor function have that effect; the denominator of 5 sets a period of 5 months.
The overall function, {\displaystyle \operatorname {mod} \,7}{\displaystyle \operatorname {mod} \,7}, normalizes the result to reside in the range of 0 to 6, which yields the index of the correct day of the week for the date being analyzed.
The reason that the formula differs for the Julian calendar is that this calendar does not have a separate rule for leap centuries and is offset from the Gregorian calendar by a fixed number of days each century.

Since the Gregorian calendar was adopted at different times in different regions of the world, the location of an event is significant in determining the correct day of the week for a date that occurred during this transition period. This is only required through 1929, as this was the last year that the Julian calendar was still in use by any country on earth, and thus is not required for 1930 or later.

The formulae can be used proleptically, but "Year 0" is in fact year 1 BC (see astronomical year numbering). The Julian calendar is in fact proleptic right up to 1 March AD 4 owing to mismanagement in Rome (but not Egypt) in the period since the calendar was put into effect on 1 January 45 BC (which was not a leap year). In addition, the modulo operator might truncate integers to the wrong direction (ceiling instead of floor). To accommodate this, one can add a sufficient multiple of 400 Gregorian or 700 Julian years.

Examples
For 1 January 2000, the date would be treated as the 13th month of 1999, so the values would be:

{\displaystyle q=1}{\displaystyle q=1}
{\displaystyle m=13}{\displaystyle m=13}
{\displaystyle K=99}{\displaystyle K=99}
{\displaystyle J=19}{\displaystyle J=19}
So the formula evaluates as {\displaystyle (1+36+99+24+4-38){\bmod {7}}=126{\bmod {7}}=0={\text{Saturday}}}{\displaystyle (1+36+99+24+4-38){\bmod {7}}=126{\bmod {7}}=0={\text{Saturday}}}.

(The 36 comes from {\displaystyle (13+1)\times 13/5=182/5}{\displaystyle (13+1)\times 13/5=182/5}, truncated to an integer.)

However, for 1 March 2000, the date is treated as the 3rd month of 2000, so the values become

{\displaystyle q=1}{\displaystyle q=1}
{\displaystyle m=3}{\displaystyle m=3}
{\displaystyle K=0}{\displaystyle K=0}
{\displaystyle J=20}{\displaystyle J=20}
so the formula evaluates as {\displaystyle (1+10+0+0+5-40){\bmod {7}}=-24{\bmod {7}}=4={\text{Wednesday}}}{\displaystyle (1+10+0+0+5-40){\bmod {7}}=-24{\bmod {7}}=4={\text{Wednesday}}}.

Implementations in software
Basic modification
Further information: Modulo operation § Variants of the definition
The formulas rely on the mathematician's definition of modulo division, which means that −2 mod 7 is equal to positive 5. Unfortunately, in the truncating way most computer languages implement the remainder function, −2 mod 7 returns a result of −2. So, to implement Zeller's congruence on a computer, the formulas should be altered slightly to ensure a positive numerator. The simplest way to do this is to replace − 2J by + 5J and − J by + 6J. So the formulas become:

{\displaystyle h=\left(q+\left\lfloor {\frac {13(m+1)}{5}}\right\rfloor +K+\left\lfloor {\frac {K}{4}}\right\rfloor +\left\lfloor {\frac {J}{4}}\right\rfloor +5J\right){\bmod {7}},}{\displaystyle h=\left(q+\left\lfloor {\frac {13(m+1)}{5}}\right\rfloor +K+\left\lfloor {\frac {K}{4}}\right\rfloor +\left\lfloor {\frac {J}{4}}\right\rfloor +5J\right){\bmod {7}},}
for the Gregorian calendar, and

{\displaystyle h=\left(q+\left\lfloor {\frac {13(m+1)}{5}}\right\rfloor +K+\left\lfloor {\frac {K}{4}}\right\rfloor +5+6J\right){\bmod {7}},}{\displaystyle h=\left(q+\left\lfloor {\frac {13(m+1)}{5}}\right\rfloor +K+\left\lfloor {\frac {K}{4}}\right\rfloor +5+6J\right){\bmod {7}},}
for the Julian calendar.

One can readily see that, in a given year, March 1 (if that is a Saturday, then March 2) is a good test date; and that, in a given century, the best test year is that which is a multiple of 100.

Common simplification
Zeller used decimal arithmetic, and found it convenient to use J and K in representing the year. But when using a computer, it is simpler to handle the modified year Y and month m, which are Y - 1 and m + 12 during January and February:

{\displaystyle h=\left(q+\left\lfloor {\frac {13(m+1)}{5}}\right\rfloor +Y+\left\lfloor {\frac {Y}{4}}\right\rfloor -\left\lfloor {\frac {Y}{100}}\right\rfloor +\left\lfloor {\frac {Y}{400}}\right\rfloor \right){\bmod {7}},}{\displaystyle h=\left(q+\left\lfloor {\frac {13(m+1)}{5}}\right\rfloor +Y+\left\lfloor {\frac {Y}{4}}\right\rfloor -\left\lfloor {\frac {Y}{100}}\right\rfloor +\left\lfloor {\frac {Y}{400}}\right\rfloor \right){\bmod {7}},}
for the Gregorian calendar (in this case there is no possibility of overflow because {\displaystyle \left\lfloor Y/4\right\rfloor \geq \left\lfloor Y/100\right\rfloor }{\displaystyle \left\lfloor Y/4\right\rfloor \geq \left\lfloor Y/100\right\rfloor }), and

{\displaystyle h=\left(q+\left\lfloor {\frac {13(m+1)}{5}}\right\rfloor +Y+\left\lfloor {\frac {Y}{4}}\right\rfloor +5\right){\bmod {7}},}{\displaystyle h=\left(q+\left\lfloor {\frac {13(m+1)}{5}}\right\rfloor +Y+\left\lfloor {\frac {Y}{4}}\right\rfloor +5\right){\bmod {7}},}
for the Julian calendar.

The algorithm above is mentioned for the Gregorian case in RFC 3339, Appendix B, albeit in an abridged form that returns 0 for Sunday.
