import psycopg2


def task_2(cursor):
    cursor.execute('''
            CREATE TABLE shops
            (
                "id" SERIAL NOT NULL,
                "name" VARCHAR(30) NOT NULL ,
                "address" VARCHAR(100) DEFAULT NULL,
                "staff_amount" INTEGER NOT NULL,
                PRIMARY KEY(id)
            );
            CREATE TABLE departments
            (
                "id" SERIAL PRIMARY KEY,
                "sphere" VARCHAR(30) NOT NULL,
                "staff_amount" INTEGER NOT NULL ,
                "shop" INTEGER REFERENCES Shops(id)
            );
            CREATE TABLE items
            (
                "id" SERIAL PRIMARY KEY,
                "name" VARCHAR(30) NOT NULL,
                "descriptions" TEXT DEFAULT NULL,
                "price" INTEGER,
                "department" INTEGER REFERENCES Departments(id)
            )
''')


def task_3(cursor):
    cursor.execute('''
    INSERT INTO shops (name, address, "staff amount")
    VALUES ('Auchan', null, 250), ('IKEA', 'Vilnius, Lithuania.', 500);
    INSERT INTO departments (sphere, staff_amount, shop)
    VALUES ('Furniture', 250, 1), ('Furniture', 300, 2), ('Dishes', 200, 1);
    INSERT INTO items (name, descriptions, price, department)
    VALUES ('Table', 'Cheap wooden table', 300, 1), ('Table', null, 750, 2),
        ('Bed', 'Amazing wooden bed', 1200, 2), ('Cup', null, 10, 3),
        ('Plate', 'Glass plate', 20, 3)
''')


def task_4(cursor):
    result1 = list(cursor.execute
                   ('''
                    SELECT *
                    FROM items
                    WHERE descriptions IS NOT NULL
                    '''))

    result2 = list(cursor.execute
                   ('''
                    SELECT sphere
                    FROM departments
                    WHERE departments.staff_amount > 200
                    ''')
                   )

    result3 = list(cursor.execute
                   ('''
                    SELECT address
                    FROM shops
                    WHERE shops.name ILIKE 'i%';
                    ''')
                   )
    result4 = list(cursor.execute
                   ('''
                    SELECT DISTINCT name
                    FROM items
                    JOIN departments d on items.department = d.id
                    WHERE d.sphere = 'Furniture';
                    ''')
                   )
    print(result1)


with psycopg2.connect(dbname='my_db_psql', user='user', password='', host='localhost') as conn:
    with conn.cursor() as cur:
        task_2(cur)
        # # task_3(cur)
        # task_4(cur)