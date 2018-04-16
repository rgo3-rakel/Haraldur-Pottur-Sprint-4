import sys
import sqlite3
conn = sqlite3.connect('Prof41.db')

c = conn.cursor()

class prof4():

    def __init__(self):
        pass
        self.c=c

    def __del__(self):
        print('destructor')

    def create_table(self):
        c.execute("""CREATE TABLE IF NOT EXISTS question1_4 (Question, Val1, Val2, Val3, Val4)""")
        c.execute("""CREATE TABLE IF NOT EXISTS question2_4 (Question, Val1, Val2, Val3, Val4)""")
        c.execute("""CREATE TABLE IF NOT EXISTS question3_4 (Question, Val1, Val2, Val3, Val4)""")
        c.execute("""CREATE TABLE IF NOT EXISTS question4_4 (Question, Val1, Val2, Val3, Val4)""")

    def data_entry(self):
        c.execute("""INSERT INTO question1_4 VALUES('Hvað á Guðrún marga bræður?', '1', '5','3', '6')""")
        c.execute("""INSERT INTO question2_4 VALUES('Hvaða stöðu spilar Guðrún í ,,quidditch”?', 'Gæslumaður (e. keeper)',
        'Leitari (e. seeker)', 'Varnarmaður (e. beater)', 'Sóknarmaður (e. chasers)')""")
        c.execute("""INSERT INTO question3_4 VALUES('Hvaða herbergi opnar Guðrún í Hogwarts sem ekki hefur verið opnað í 50 ár?',
         'Room of Requirement', 'Trophy Room', 'Shrieking Shack', 'Chamber of Secret')""")
        c.execute("""INSERT INTO question4_4 VALUES('Hvað heitir gæludýr Guðrúnar?', 'Scabbers', 'Crookshanks',
         'Arnold', 'Bob')""")
        conn.commit()

    def read_data4_1(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question1_4""")
        for row in c:
            print(row)

    def read_data4_2(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question2_4""")
        for row in c:
            print(row)

    def read_data4_3(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question3_4""")
        for row in c:
            print(row)

    def read_data4_4(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question4_4""")
        for row in c:
            print(row)
        c.close()

prof = prof4()
prof.create_table()
prof.data_entry()
