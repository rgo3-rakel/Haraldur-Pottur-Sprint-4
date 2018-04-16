import sqlite3
conn = sqlite3.connect('Prof11.db')

c = conn.cursor()

class prof1():

    def __init__(self):
        pass

    def __del__(self):
        print('destructor')

    def create_table(self):
        c.execute("""CREATE TABLE IF NOT EXISTS question1_1 (Question, Val1, Val2, Val3, Val4)""")
        c.execute("""CREATE TABLE IF NOT EXISTS question2_1 (Question, Val1, Val2, Val3, Val4)""")
        c.execute("""CREATE TABLE IF NOT EXISTS question3_1 (Question, Val1, Val2, Val3, Val4)""")
        c.execute("""CREATE TABLE IF NOT EXISTS question4_1 (Question, Val1, Val2, Val3, Val4)""")

    def data_entry(self):
        c.execute("""INSERT INTO question1_1 VALUES('Hvað heitir mamma Haralds Potts?', 'Claudia', 'Lily', 'Petunia', 'Molly')""")
        c.execute("""INSERT INTO question2_1 VALUES('Hver sótti Harald á 11 ára afmælisdeginum hans?', 'Albus Percival Wulfric Brian Dumbledore', 'Gilderoy Lockhart',
        'Hagrid', 'Arthur Weasley')""")
        c.execute("""INSERT INTO question3_1 VALUES('Hver er guðfaðir Haralds?', 'Albus Percival Wulfric Brian Dumbledore', 'Arthur Weasley', 'Lucius Malfoy',
        'Sirius Black')""")
        c.execute("""INSERT INTO question4_1 VALUES('Hvaða stöðu spilar Haraldur í ,,quidditch”?', 'Gæslumaður (e. keeper)', 'Leitari (e. seeker)',
         'Varnarmaður (e. beater)', 'Sóknarmaður (e. chasers)')""")
        conn.commit()

    def read_data1_1(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question1_1""")
        for row in c:
            print(row)

    def read_data1_2(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question2_1""")
        for row in c:
            print(row)

    def read_data1_3(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question3_1""")
        for row in c:
            print(row)

    def read_data1_4(self):
        c.execute(""" SELECT Question, Val1, Val2, Val3, Val4 FROM question4_1""")
        for row in c:
            print(row)
        c.close()

prof = prof1()
prof.create_table()
prof.data_entry()
