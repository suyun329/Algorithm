<!--# SQL-->
MySQL https://www.hackerrank.com/challenges/weather-observation-station-8/problem
### Weather Observation Station 8

Solve
```sql
select distinct CITY
from STATION
where CITY REGEXP "^[a,e,i,o,u]" and CITY REGEXP "[a,e,i,o,u]$";
```

##### <시행착오>
```sql
select distinct CITY
from STATION
where CITY REGEXP "^[a,e,i,o,u]" and "[a,e,i,o,u]$";
```

Status: no response on stdout
