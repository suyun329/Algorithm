<!--# SQL-->
MySQL https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
### Average Population of Each Continent


Solve - [JOIN]
```sql
select country.continent, floor(avg(city.population))
from city
    inner join country on country.code = city.countrycode
group by country.continent
```

##### <시행착오>
```sql

```

Status: Success
