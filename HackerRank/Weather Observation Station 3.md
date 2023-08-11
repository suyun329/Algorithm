<!--# SQL-->
MySQL https://www.hackerrank.com/challenges/weather-observation-station-3/problem
### Weather Observation Station 3

Solve
```sql
select distinct CITY
from STATION
where ID%2=0;
```

```sql
select CITY
from STATION
where ID%2=0
group by CITY;
```

##### <시행착오>
```sql
select distinct CITY
from STATION
where ID/2=0;
```

Status: no response on stdout
