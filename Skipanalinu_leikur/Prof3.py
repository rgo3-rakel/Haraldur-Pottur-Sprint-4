import sqlite3
conn = sqlite3.connect('Prof31.db')

c = conn.cursor()

class prof3():

    def __init__(self):
        pass

    def __del__(self):
        print('destructor')

    def create_table(self):
        c.execute("""CREATE TABLE IF NOT EXISTS question3_1 (Question, Val1, Val2, Val3, Val4)""")
        c.execute("""CREATE TABLE IF NOT EXISTS question3_2 (Question, Val1, Val2, Val3, Val4)""")
        c.execute("""CREATE TABLE IF NOT EXISTS question3_3 (Question, Val1, Val2, Val3, Val4)""")
        c.execute("""CREATE TABLE IF NOT EXISTS question3_4 (Question, Val1, Val2, Val3, Val4)""")

    def data_entry(self):
        c.execute("""INSERT INTO question3_1 VALUES('Hvað heitir rottan hans Rúnars?', 'Frankie', 'Scabbers',
         'Oscar', 'Dobbie')""")
        c.execute("""INSERT INTO question3_2 VALUES('Hvaða stöðu spilar Rúnar í ,,quidditch”?', 'Gæslumaður (e. keeper)',
        'Leitari (e. seeker)', 'Varnarmaður (e. beater)', 'Sóknarmaður (e. chasers)')""")
        c.execute("""INSERT INTO question3_3 VALUES('Hvaða dýr hræðist Rúnar mest?', 'Dreka', 'Könguló',
        'Hippogriff', 'Mýs')""")
        c.execute("""INSERT INTO question3_4 VALUES('Hverju safnar Rúnar?', 'Chocolate Frogs', 'Bertie Bott’s Every Flavored Beans',
         'Frímerkjum', ',,Quidditch” spil')""")
        conn.commit()

    def read_data3_1(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question3_1""")
        for row in c:
            print(row)

    def read_data3_2(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question3_2""")
        for row in c:
            print(row)

    def read_data3_3(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question3_3""")
        for row in c:
            print(row)

    def read_data3_4(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question3_4""")
        for row in c:
            print(row)
        c.close()

prof = prof3()
prof.create_table()
prof.data_entry()
