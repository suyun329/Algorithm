<!--# SQL-->
MySQL https://www.hackerrank.com/challenges/weather-observation-station-6/problem
### Weather Observation Station 6

Solve
```sql
select distinct CITY
from STATION
where CITY LIKE 'A%' 
OR CITY LIKE 'E%' 
OR CITY LIKE 'I%' 
OR CITY LIKE 'O%' 
OR CITY LIKE 'U%';
```

##### <시행착오>
```sql
select CITY
from STATION
where CITY LIKE 'A%' 
OR CITY LIKE 'E%' 
OR CITY LIKE 'I%' 
OR CITY LIKE 'O%' 
OR CITY LIKE 'U%';
```

Status: Runtime Error
