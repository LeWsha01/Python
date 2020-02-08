Вложенные запросы: https://proselyte.net/tutorials/sql/nested-queries/
Функции: https://postgrespro.ru/docs/postgresql/9.6/sql-createfunction
Триггеры: https://postgrespro.ru/docs/postgresql/9.6/plpgsql-trigger
SQL alchemy: https://habr.com/ru/post/470285/, https://habr.com/ru/post/324876/
SQL alchemy doc: https://www.sqlalchemy.org/

Все при помощи SQLAlchemy.
Создать базу данных со следующими таблицами:
CREATE TABLE AGENTS
(
    AGENT_CODE   CHAR(6) NOT NULL PRIMARY KEY,
    AGENT_NAME   CHAR(40),
    WORKING_AREA CHAR(35),
    COMMISSION   FLOAT,
    PHONE_NO     CHAR(15),
    COUNTRY      CHAR(25)
);

CREATE TABLE CUSTOMER
(
    CUST_CODE       VARCHAR(6)  NOT NULL PRIMARY KEY,
    CUST_NAME       VARCHAR(40) NOT NULL,
    CUST_CITY       CHAR(35),
    WORKING_AREA    VARCHAR(35) NOT NULL,
    CUST_COUNTRY    VARCHAR(20) NOT NULL,
    GRADE           INTEGER,
    OPENING_AMT     REAL        NOT NULL,
    RECEIVE_AMT     REAL        NOT NULL,
    PAYMENT_AMT     REAL        NOT NULL,
    OUTSTANDING_AMT REAL        NOT NULL,
    PHONE_NO        CHAR(17)    NOT NULL,
    AGENT_CODE      CHAR(6)     NOT NULL REFERENCES AGENTS
);

CREATE TABLE ORDERS
(
    ORD_NUM         INTEGER     NOT NULL PRIMARY KEY,
    ORD_AMOUNT      REAL        NOT NULL,
    ADVANCE_AMOUNT  REAL        NOT NULL,
    ORD_DATE        DATE        NOT NULL,
    CUST_CODE       VARCHAR(6)  NOT NULL REFERENCES CUSTOMER,
    AGENT_CODE      CHAR(6)     NOT NULL REFERENCES AGENTS,
    ORD_DESCRIPTION VARCHAR(60) NOT NULL
);

Сгенерировать случайные данные для этих таблиц, по 50 записей в каждю.

Запросы с занятия:
SELECT ord_num, ord_amount, ord_date
FROM orders
JOIN agents ON orders.agent_code=agents.agent_code
WHERE agent_name='Mukesh';

SELECT cust_name
FROM orders
JOIN agents ON orders.agent_code=agents.agent_code
JOIN customer on orders.cust_code=customer.cust_code
WHERE agent_name='Mukesh' and orders.ORD_AMOUNT > 1000;

SELECT customer.cust_name
FROM orders
JOIN agents ON orders.agent_code=agents.agent_code
JOIN customer on orders.cust_code=customer.cust_code
WHERE agents.agent_name='Mukesh' and orders.ORD_AMOUNT > 1000
GROUP BY customer.cust_name;

SELECT customer.cust_name, COUNT(*) as "Number of customers"
FROM orders
JOIN agents ON orders.agent_code=agents.agent_code
JOIN customer on orders.cust_code=customer.cust_code
WHERE agents.agent_name='Mukesh' and orders.ORD_AMOUNT > 1000
GROUP BY customer.cust_name;

SELECT agents.agent_name, sum(orders.advance_amount)
FROM orders
JOIN agents ON orders.agent_code=agents.agent_code
GROUP BY agents.agent_name;

SELECT * FROM (
   SELECT agents.agent_name, SUM(orders.advance_amount)
   FROM orders
   JOIN agents ON orders.agent_code=agents.agent_code
   GROUP BY agents.agent_name
) AS result
WHERE agent_name='Mukesh';

SELECT agent_code, commission
FROM agents
WHERE agent_name IN (
   SELECT result.agent_name
   FROM (
            SELECT agents.agent_name, SUM(orders.advance_amount)
            FROM orders
                     JOIN agents ON orders.agent_code = agents.agent_code
            GROUP BY agents.agent_name
        ) AS result
   WHERE result.sum > 3000);

SELECT *
FROM ORDERS
WHERE ord_amount > (SELECT AVG(ord_amount) FROM ORDERS);

Все вышеуказанные запросы нужно сделать средствами ORM и записать их в файл.
