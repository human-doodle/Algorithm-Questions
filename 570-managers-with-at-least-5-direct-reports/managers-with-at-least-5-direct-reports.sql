# Write your MySQL query statement below
with cte as
(SELECT managerID, count(*)
FROM Employee
Group by managerID
HAVING count(*)>=5)
SELECT Employee.name
from cte 
JOIN Employee
where cte.managerID = Employee.ID