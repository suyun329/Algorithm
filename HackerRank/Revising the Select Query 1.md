<!--# SQL-->
MySQL https://www.hackerrank.com/challenges/revising-the-select-query/problem
### Revising the Select Query 1 

Solve
```sql
select *
from CITY
where COUNTRYCODE='USA' and POPULATION>100000;
```

### <시행착오>
```sql
select *
from CITY
where COUNTRYCODE=USA and POPULATION>100000;
```

Status:Runtime Error
