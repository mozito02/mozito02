CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
SELECT  salary
FROM (
  SELECT distinct salary, dense_rank() OVER (ORDER BY salary DESC) AS r
  FROM Employee
) AS ranked_salaries
WHERE r = N

  );
END;
