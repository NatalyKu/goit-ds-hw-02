import faker
import random
import sqlite3

NUMBER_TASKS = 300
NUMBER_USERS = 20

def generate_fake_data(number_tasks, number_users) -> tuple:
    fake_tasks = []
    fake_users = []
    fake_emails = []

    fake_data = faker.Faker()

    def generate_tasks():
        verbs = ['analyze', 'predict', 'visualize', 'preprocess', 'model', 'train', 'evaluate', 'optimize', 'deploy', 'extract']
        nouns = ['dataset', 'algorithm', 'model', 'feature', 'prediction', 'visualization', 'metric', 'pipeline', 'experiment', 'analysis']
        adjectives = ['accurate', 'scalable', 'robust', 'efficient', 'reliable', 'interpretable', 'complex', 'optimized', 'automated', 'insightful']
        return f"{random.choice(verbs).capitalize()} {random.choice(adjectives)} {random.choice(nouns)}"
    
    for _ in range(number_tasks):
        fake_tasks.append(generate_tasks())

    for _ in range(number_users):
        fake_users.append(fake_data.name())

    for _ in range(number_users):
        fake_emails.append(fake_data.email())

    return fake_tasks, fake_users, fake_emails

tasks, users, emails = generate_fake_data(NUMBER_TASKS, NUMBER_USERS)
print(tasks)
print(users)
print(emails)

def prepare_data(tasks, users, emails) -> tuple:
    for_tasks = [(task, "Description", random.randint(1, 3), random.randint(1, NUMBER_USERS)) for task in tasks]
    for_users = list(zip(users, emails))
    for_status = [(1, 'new'), (2, 'in progress'), (3, 'completed')]

    return for_tasks, for_users, for_status

for_tasks, for_users, for_status = prepare_data(tasks, users, emails)

def insert_data_to_db(for_users, for_tasks, for_status):
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        
        sql_to_users = """INSERT INTO users(fullname, email) VALUES (?, ?)"""
        cur.executemany(sql_to_users, for_users)

        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id) VALUES (?, ?, ?, ?)""" 
        cur.executemany(sql_to_tasks, for_tasks)

        sql_to_status = """INSERT INTO status(id, name) VALUES (?, ?)""" 
        cur.executemany(sql_to_status, for_status)
        
        con.commit()

insert_data_to_db(for_users, for_tasks, for_status)