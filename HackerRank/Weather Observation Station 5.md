<!--# SQL-->
MySQL https://www.hackerrank.com/challenges/weather-observation-station-5/problem
### Weather Observation Station 5

Solve
```sql
select CITY, length(CITY)
from STATION
order by length(CITY), CITY
limit 1;

select CITY, length(CITY)
from STATION
order by length(CITY) desc, CITY
limit 1;
```

##### <시행착오>
```sql
select CITY, length(CITY)
from STATION
order by length(CITY), 2
limit 1;

select CITY, length(CITY)
from STATION
order by length(CITY) desc, 2
limit 1;
```

Status: Wrong Answer
<br>
Expected Output<br>
Amo 3
Marine On Saint Croix 21
<br><br>
This code Output<br>
Roy 3
Marine On Saint Croix 21
