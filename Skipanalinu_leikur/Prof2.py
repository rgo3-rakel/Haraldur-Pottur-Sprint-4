import sqlite3
conn = sqlite3.connect('Prof21.db')

c = conn.cursor()

class prof2():

    def __init__(self):
        pass

    def __del__(self):
        print('destructor')

    def create_table(self):
        c.execute("""CREATE TABLE IF NOT EXISTS question2_1 (Question, Val1, Val2, Val3, Val4)""")
        c.execute("""CREATE TABLE IF NOT EXISTS question2_2 (Question, Val1, Val2, Val3, Val4)""")
        c.execute("""CREATE TABLE IF NOT EXISTS question2_3 (Question, Val1, Val2, Val3, Val4)""")
        c.execute("""CREATE TABLE IF NOT EXISTS question2_4 (Question, Val1, Val2, Val3, Val4)""")

    def data_entry(self):
        c.execute("""INSERT INTO question2_1 VALUES('Við hvað starfa foreldrar Hermínu Guðmundsdóttur?', 'Verkfræðingar', 'Kennarar',
         'Lögfræðingar', 'Tannlæknar')""")
        c.execute("""INSERT INTO question2_2 VALUES('Hvaða vera ræðst á Hermínu á stelpuklósettinu fyrsta árið í Hogwarts?', 'Draugur',
         'Mús', 'Tröll', 'Hippogriff')""")
        c.execute("""INSERT INTO question2_3 VALUES('Hver fer með Hermínu á jólaballið?', 'Victor Krum', 'Neville Longbottom',
        'Ron Weasley', 'Draco Malfoy')""")
        c.execute("""INSERT INTO question2_4 VALUES('Hvern slær Hermína í andlitið?', 'Victor Krum', 'Neville Longbottom',
         'Ron Weasley', 'Draco Malfoy')""")
        conn.commit()

    def read_data2_1(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question2_1""")
        for row in c:
            print(row)

    def read_data2_2(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question2_2""")
        for row in c:
            print(row)

    def read_data2_3(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question2_3""")
        for row in c:
            print(row)

    def read_data2_4(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question2_4""")
        for row in c:
            print(row)
        c.close()

prof = prof2()
prof.create_table()
prof.data_entry()
