<!--# SQL-->
MySQL https://www.hackerrank.com/challenges/weather-observation-station-11/problem
### Weather Observation Station 11

Solve
```sql
select distinct CITY
from STATION
where CITY REGEXP "^[^a,e,i,o,u]" or CITY REGEXP "[^a,e,i,o,u]$";
```

##### <시행착오>
```sql
select distinct CITY
from STATION
where CITY REGEXP "^[^a,e,i,o,u]" and CITY REGEXP "[^a,e,i,o,u]$";
```

Status: Wrong Answer
