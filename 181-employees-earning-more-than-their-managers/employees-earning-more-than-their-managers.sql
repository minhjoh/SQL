/* Write your T-SQL query statement below */
SELECT e1.name as Employee
FROM Employee e1
LEFT JOIN (SELECT id, salary
        FROM Employee
        WHERE id in (SELECT ManagerId
                FROM Employee)) m ON e1.managerId = m.id
WHERE e1.salary > m.salary 