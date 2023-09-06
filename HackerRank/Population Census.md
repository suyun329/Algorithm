<!--# SQL-->
MySQL https://www.hackerrank.com/challenges/asian-population/problem
### Population Census
<JOIN>

Solve
```sql
select sum(city.population)
from city
    inner join country on country.code = city.countrycode
where country.continent = 'asia'
```

##### <시행착오>
```sql

```

Status: Success
