import sqlite3


# Создание базы данных и подключение к ней
with sqlite3.connect('sales.db') as con:
    cur = con.cursor()

    # Создание таблицы "Salespeople"
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Salespeople (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sname VARCHAR(255) NOT NULL,
            city VARCHAR(255) NOT NULL,
            comm DECIMAL(10, 2) NOT NULL
        );
    ''')

    # Создание таблицы "Customers"
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cname VARCHAR(255) NOT NULL,
            city VARCHAR(255) NOT NULL,
            rating INTEGER NOT NULL,
            id_sp INTEGER NOT NULL,
            FOREIGN KEY (id_sp) REFERENCES Salespeople(id)
        );
    ''')

    # Загрузка данных из файлов "salespeople.txt" и "Customer.txt" и вставка их в таблицы
    with open('salespeople.txt', 'r', encoding='utf-8') as sp_file:
        for line in sp_file:
            data = line.strip().split(', ')
            sname, city, comm = data[0], data[1], float(data[2])
            cur.execute('INSERT INTO Salespeople (sname, city, comm) VALUES (?, ?, ?)', (sname, city, comm))

    with open('Customer.txt', 'r', encoding='utf-8') as customer_file:
        for line in customer_file:
            data = line.strip().split(', ')
            cname, city, rating, id_sp = data[0], data[1], int(data[2]), int(data[3])
            cur.execute('INSERT INTO Customers (cname, city, rating, id_sp) VALUES (?, ?, ?, ?)', (cname, city, rating, id_sp))

    con.commit()

    print("Таблицы и данные успешно созданы и загружены.")