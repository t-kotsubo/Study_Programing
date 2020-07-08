```
CREATE VIEW emp_dept 
AS
SELECT E.*, D.dept_name
FROM employee E
LEFT JOIN department D
ON E.dept_no = D.dept_no;

```

```
select emp_name
from employee as E
WHERE E.dept_no IN (
SELECT dept_no
FROM department as D
WHERE D.dept_name = '営業部'
);

```

```
SELECT emp_name from employee AS E
WHERE EXISTS (
SELECT * FROM department AS D
WHERE D.dept_name = '営業部'
AND
E.dept_no = D.dept_no
);
```

```
SELECT emp_name FROM employee AS E
WHERE NOT EXISTS (
SELECT * FROM department AS D
WHERE D.dept_no = E.dept_no
);
```



```
SELECT emp_name FROM employee AS E
WHERE E.dept_no NOT IN (
SELECT dept_no FROM
department AS D
) AND E.dept_no is not null
```

```
select E.emp_name, D.dept_name from employee as E
where E.dept_no in (
select dept_no from department as D
where E.dept_no = D.dept_no
);
```

```
SELECT E.emp_name,
(SELECT D.dept_name from department AS D
WHERE E.dept_no = D.dept_no 
)
FROM employee AS E;

SELECT E.EMP_NAME, 
(SELECT D.DEPT_NAME FROM DEPARTMENT D
WHERE E.DEPT_NO = D.DEPT_NO)  FROM EMPLOYEE E; 

SELECT E.emp_name AS 従業員名,
(SELECT D.dept_name
FROM department AS D
WHERE E.dept_no = D.dept_no) AS 部署名
FROM employee AS E;
```

演習2-6

```
SELECT E.dept_no FROM employee AS E
WHERE E.dept_no in (
SELECT E.dept_no FROM E
WHERE E.dept_no = E.dept_no
GROUP BY E.dept_no
HAVING COUNT(E.dept_no) >=2
)
```

