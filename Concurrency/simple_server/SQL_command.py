SELECT_EMPLOYEES_DEP = \
    """
    SELECT emp.first_name as FIRST_NAME, emp.last_name AS LAST_NAME, dep.dept_name AS DEPARTMENT
    FROM employees.employee AS emp
    JOIN employees.department_employee as dep_emp
        ON emp.id = dep_emp.employee_id
    JOIN employees.department as dep
        ON dep.id = dep_emp.department_id
    WHERE dep.dept_name = '{}';
    """