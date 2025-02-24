
import sqlite3

def execute_query(sql:str):
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
sql_1 = """
SELECT * FROM tasks 
WHERE user_id = 12;
"""

sql_2 = """ 
SELECT * FROM tasks 
WHERE user_id = 12
AND status_id in 
(SELECT id FROM status WHERE id= 1);
"""

sql_3 = """
 UPDATE tasks
    SET status_id = 2
    WHERE status_id = 1
    AND user_id = 12;
"""

sql_4 = """
SELECT fullname FROM users
WHERE id NOT IN (SELECT user_id FROM tasks);
"""

sql_5 = """
    SELECT * FROM tasks 
WHERE status_id != 3;
"""

sql_6 = """
    INSERT INTO tasks (title, status_id, user_id)
VALUES ("Make a Power BI presentation", '1', 5)
;
"""

sql_7 = """ DELETE FROM tasks WHERE id =5; """

sql_8 = """ SELECT * FROM users WHERE email IN ('shughes@example.org', 'selena82@example.com', 'adamsjacob@example.org');
"""

sql_9 = """UPDATE users
    SET fullname = 'Susan Morten'
    WHERE fullname = 'Susan Matthews'
    ;
"""

sql_10 = """SELECT t.* FROM tasks t INNER JOIN users u on(t.user_id = u.id)
WHERE u.email LIKE '%@example.com';
"""

sql_11 = """SELECT * FROM tasks WHERE description IS NULL;
"""

sql_12 = """SELECT t.id, t.title, t.description, u.fullname FROM tasks t INNER JOIN users u on(t.user_id = u.id)
WHERE t.status_id=2;
"""

sql_12 = """SELECT u.fullname , count(t.title) FROM users u LEFT JOIN tasks t ON t.user_id =u.id 
GROUP BY t.user_id ;
"""

sql_12 = """SELECT s.name, count(t.id) FROM status s LEFT JOIN tasks t ON (t.status_id = s.id)
GROUP BY s.name;
"""

print(execute_query(sql_1))