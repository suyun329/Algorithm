<!--# SQL-->
MySQL https://www.hackerrank.com/challenges/full-score/problem
### Top Competitors


Solve - [JOIN]
```sql
select h.hacker_id, h.name
from Submissions s
    inner join Hackers h on s.hacker_id = h.hacker_id
    inner join Challenges c on s.challenge_id = c.challenge_id
    inner join Difficulty d on c.difficulty_level = d.difficulty_level
where d.score = s.score and c.difficulty_level = d.difficulty_level
group by h.hacker_id, h.name
having count(s.hacker_id) > 1
order by count(s.hacker_id) desc, h.hacker_id
```

##### <시행착오>
```sql

```

Status: Success
