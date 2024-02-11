import random
from datetime import datetime, timedelta

def generate_license_number():
    start_date = datetime(2010, 1, 1)
    end_date = datetime.now()
    random_date = start_date + (end_date - start_date) * random.random()
    return f'{random_date.strftime("%y%m%d")}/{random_date.year + random.randint(1, 5)}'

def generate_random_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']
    return f'{"".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))}@{random.choice(domains)}'

def generate_random_logo():
    return f'https://example.com/images/logo{random.randint(1, 10)}.png'

sql_file = 'init_db.sql'
with open(sql_file, 'w') as f:
    for _ in range(1000):
        license_number = generate_license_number()
        name = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10))
        name_en = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10))
        status = random.choice(['Operational', 'Closed'])
        email = generate_random_email()
        rating_score = round(random.uniform(0, 5), 2)
        rating_count = random.randint(1, 500)
        comments_count = random.randint(1, 1000)
        popularity = random.randint(1, 2000)
        city = random.randint(1, 10)
        logo = generate_random_logo()

        insert_statement = f"INSERT INTO app_supplier (name, name_en, license_number, status, logo, email, rating_score, rating_count, comments_count, popularity, city) VALUES ('{name}', '{name_en}', '{license_number}', '{status}', '{logo}', '{email}', {rating_score}, {rating_count}, {comments_count}, {popularity}, {city});\n"
        f.write(insert_statement)
