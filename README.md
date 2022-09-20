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

