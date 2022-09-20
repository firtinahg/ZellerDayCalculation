# ZellerDayCalculation

 <h2 align="left"> Calculation of the day of given date with the help of Zeller's Rule:</h2>
 
 <h2 align="left"><summary> Zeller's congruence:</summary></h2>
 
 Zeller's congruence is an algorithm devised by Christian Zeller in the 19th century to calculate the day of the week for any Julian or Gregorian calendar date. It can be considered to be based on the conversion between Julian day and the calendar date.
 
 <h2 align="left"><summary>Formula:</summary></h2>
 
 For the Gregorian calendar, Zeller's congruence is:
 
 ![image](https://user-images.githubusercontent.com/57679283/191345851-bbae1329-a835-47b6-9c70-7a2983697906.png)

for the Julian calendar it is:

![image](https://user-images.githubusercontent.com/57679283/191346084-4da2de01-0b8b-40ff-8161-b3625955afeb.png)

where

* h is the day of the week (0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday)

* q is the day of the month

* m is the month (3 = March, 4 = April, 5 = May, ..., 14 = February)

* K the year of the century ![image](https://user-images.githubusercontent.com/57679283/191347778-766c613a-3e02-4b9f-a5fe-378164636190.png).

* J is the zero-based century (actually ![image](https://user-images.githubusercontent.com/57679283/191347930-83ce7eb5-8f9e-4d94-a543-2e7d71985af2.png)) For example, the zero-based centuries for 1995 and 2000 are 19 and 20 respectively (not to be confused with the common ordinal century enumeration which indicates 20th for both cases).

* ![image](https://user-images.githubusercontent.com/57679283/191346383-fe096f2b-8d3d-4496-a1fc-563d1e67e9f8.png) is the floor function or integer part

* mod is the modulo operation or remainder after division

In this algorithm January and February are counted as months 13 and 14 of the previous year. E.g. if it is 2 February 2010, the algorithm counts the date as the second day of the fourteenth month of 2009 (02/14/2009 in DD/MM/YYYY format)

For an ISO week date Day-of-Week d (1 = Monday to 7 = Sunday), use

![image](https://user-images.githubusercontent.com/57679283/191346524-1d65d4ca-66aa-482a-9655-43616e43f732.png)


 <h2 align="left"><summary> Analysis:</summary></h2>
 
 These formulas are based on the observation that the day of the week progresses in a predictable manner based upon each subpart of that date. Each term within the formula is used to calculate the offset needed to obtain the correct day of the week.

For the Gregorian calendar, the various parts of this formula can therefore be understood as follows:

* q represents the progression of the day of the week based on the day of the month, since each successive day results in an additional offset of 1 in the day of the week.

* K represents the progression of the day of the week based on the year. Assuming that each year is 365 days long, the same date on each succeeding year will be offset by a value of ![image](https://user-images.githubusercontent.com/57679283/191348439-92154bf1-0cc2-4fec-afab-4a3ffa4f8fee.png).

* Since there are 366 days in each leap year, this needs to be accounted for by adding another day to the day of the week offset value. This is accomplished by adding ![image](https://user-images.githubusercontent.com/57679283/191348518-c17ad95a-3aa9-45c1-8de7-6716d38be15c.png) to the offset. This term is calculated as an integer result. Any remainder is discarded.

* Using similar logic, the progression of the day of the week for each century may be calculated by observing that there are 36,524 days in a normal century and 36,525 days in each century divisible by 400. Since ![image](https://user-images.githubusercontent.com/57679283/191348675-ccbc5206-0d80-4799-ba27-79b41576bb52.png) and ![image](https://user-images.githubusercontent.com/57679283/191348719-20fdc2c8-44cc-48d5-9a5c-daf743da3c4f.png), the term ![image](https://user-images.githubusercontent.com/57679283/191348758-d0df41f3-59aa-4535-b27f-2e763afff13a.png) accounts for this.

* The term ![image](https://user-images.githubusercontent.com/57679283/191349461-300d2ab4-551c-48b4-bc07-8b96f7c0ab0e.png)  adjusts for the variation in the days of the month. Starting from January, the days in a month are {31, 28/29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}. February's 28 or 29 days is a problem, so the formula rolls January and February around to the end so February's short count will not cause a problem. The formula is interested in days of the week, so the numbers in the sequence can be taken modulo 7. Then the number of days in a month modulo 7 (still starting with January) would be {3, 0/1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3}. Starting in March, the sequence basically alternates 3, 2, 3, 2, 3, but every five months there are two 31-day months in a row (July–August and December–January).[1] The fraction 13/5 = 2.6 and the floor function have that effect; the denominator of 5 sets a period of 5 months.

* The overall function,![image](https://user-images.githubusercontent.com/57679283/191349560-1bfce8f8-9a86-4fec-9b81-060640ff79cb.png) normalizes the result to reside in the range of 0 to 6, which yields the index of the correct day of the week for the date being analyzed.

The reason that the formula differs for the Julian calendar is that this calendar does not have a separate rule for leap centuries and is offset from the Gregorian calendar by a fixed number of days each century.

Since the Gregorian calendar was adopted at different times in different regions of the world, the location of an event is significant in determining the correct day of the week for a date that occurred during this transition period. This is only required through 1929, as this was the last year that the Julian calendar was still in use by any country on earth, and thus is not required for 1930 or later.

The formulae can be used proleptically, but "Year 0" is in fact year 1 BC (see astronomical year numbering). The Julian calendar is in fact proleptic right up to 1 March AD 4 owing to mismanagement in Rome (but not Egypt) in the period since the calendar was put into effect on 1 January 45 BC (which was not a leap year). In addition, the modulo operator might truncate integers to the wrong direction (ceiling instead of floor). To accommodate this, one can add a sufficient multiple of 400 Gregorian or 700 Julian years.

 <h2 align="left"><summary> Examples:</summary></h2>
 
 For 1 January 2000, the date would be treated as the 13th month of 1999, so the values would be:

![image](https://user-images.githubusercontent.com/57679283/191351230-af97ad88-7462-4089-b7cc-b849699c07a5.png)

So the formula evaluates as ![image](https://user-images.githubusercontent.com/57679283/191351278-5918ed3b-e6ee-4856-b396-d7f512086783.png)

(The 36 comes from ![image](https://user-images.githubusercontent.com/57679283/191351394-3231f7d1-d22d-4a57-994a-546d9b9e23f7.png), truncated to an integer.)

However, for 1 March 2000, the date is treated as the 3rd month of 2000, so the values become

![image](https://user-images.githubusercontent.com/57679283/191351448-19d6cddb-fa91-4af4-9c66-410d71a9991b.png)

so the formula evaluates as ![image](https://user-images.githubusercontent.com/57679283/191351498-b2cfae4b-9e45-450d-bdb4-50366eacbd66.png).

<h2> More Info: </h2>

 <p align="center"> Click <a href="https://en.wikipedia.org/wiki/Zeller%27s_congruence" title="Title"> here! </a>.</p>
 

