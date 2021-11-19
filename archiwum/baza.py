import sqlite3

def zapis_do_bazy():
    conn = sqlite3.connect('example.sqlite')

    c = conn.cursor()

    c.execute('CREATE TABLE klienci(data TEXT, klient_id INTEGER, obroty REAL)')

    c.execute("INSERT INTO klienci VALUES('2020-05-06',01,1875.60)")
    c.execute("INSERT INTO klienci VALUES('2019-02-01',02,66675.20)")

    conn.commit()
    conn.close()

def odczyt_z_bazy():
    conn = sqlite3.connect('example.sqlite')

    c = conn.cursor()

    for i in c.execute('SELECT * FROM klienci ORDER BY obroty'):
        print(i)


#odczyt_z_bazy()