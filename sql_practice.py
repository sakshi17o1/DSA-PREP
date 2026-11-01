import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.executescript("""
CREATE TABLE departments (dept_id INTEGER, dept_name TEXT);
CREATE TABLE employees (emp_id INTEGER, name TEXT, salary INTEGER, dept_id INTEGER);

INSERT INTO departments VALUES (1,'IT'),(2,'HR'),(3,'Sales'),(4,'Finance');
INSERT INTO employees VALUES
(1,'Asha',50000,1),(2,'Ravi',60000,1),(3,'Neha',60000,2),
(4,'Karan',45000,3),(5,'Simran',70000,1),(6,'Amit',45000,3),
(7,'Pooja',55000,2),(8,'Rohit',52000,NULL),(9,'Ravi',48000,3);
""")

def run(q):
    for row in cur.execute(q).fetchall():
        print(row)
    print("-" * 30)
#Q1. Salary > 50000 wale employees

run("SELECT * FROM employees WHERE salary > 50000")

#Q2. Second highest salary

run("SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees)")

#Q3. Employee ka naam aur department ka naam (INNER JOIN)

run("""
SELECT e.name , d.dept_name FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;
""")

#Q4. Woh departments jisme koi employee nahi (LEFT JOIN)

run("""
SELECT d.dept_name 
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;
""")

#Q5. Har department mein kitne employees (Finance ke saath)

run("""
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id;
""")

#Q6. Woh departments jisme 2 se zyada employees (HAVING)

run("""
SELECT d.dept_name, COUNT(*) AS TOTAL 
FROM employees e 
JOIN departments d ON d.dept_id = e.dept_id 
GROUP BY d.dept_id
HAVING COUNT(e.emp_id) > 2;
""")

#Q7. Department-wise average salary, zyada se kam

run("""
SELECT d.dept_name, AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d ON d.dept_id = e.dept_id
GROUP BY d.dept_id
ORDER BY avg_salary DESC;
""")

#Q8. Average salary se zyada kamane wale (subquery)

run("""
SELECT name, salary FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
""")

#Q9. Duplicate naam dhoondho

run("""
SELECT name, COUNT(*) AS name_count
FROM employees
GROUP BY name
HAVING COUNT(*) > 1;
""")

#Q10. Har department mein sabse zyada salary wala (window function)

run("""
SELECT dept_name, name, salary
FROM (
    SELECT d.dept_name, e.name, e.salary,
        RANK() OVER (PARTITION BY d.dept_id ORDER BY e.salary DESC) AS salary_rank
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    )
    WHERE salary_rank = 1
""")

#Q11. ROW_NUMBER vs RANK vs DENSE_RANK 

run("""
SELECT dept_name, name, salary,
    ROW_NUMBER() OVER (PARTITION BY d.dept_id ORDER BY e.salary DESC) AS row_num,
    RANK() OVER (PARTITION BY d.dept_id ORDER BY e.salary DESC) AS rank_num,
    DENSE_RANK() OVER (PARTITION BY d.dept_id ORDER BY e.salary DESC) AS dense_rank_num
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
""")

run("""
SELECT name, salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn,
    RANK()       OVER (ORDER BY salary DESC) AS r,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dr
FROM employees;
""")

#Q12. Third highest salary (DENSE_RANK se)

run("""
SELECT DISTINCT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rank_num
    FROM employees
) ranked
WHERE rank_num = 3;
""")

#Q13. Jinka department nahi hai (NULL)

run("""
SELECT name, salary
FROM employees
WHERE dept_id IS NULL;
""")