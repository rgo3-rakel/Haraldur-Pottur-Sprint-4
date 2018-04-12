import time
import sys
import random
#Importa klösum úr öðrum file-num
from character import Character
from character import ChooseChar
from hangman import Hangman
#from questions import question

class Level:

    def __init__(self):
        self._character = ""
        self.ready = ""
        super().__init__()

    def __del__(self):
       print("destructor")

    def beginning(self): #Dumbledore talar
        print("Velkomin/nn í leikinn svaðilfari!")
        #setja mynd inn

        time.sleep(1)
        level1 = Level1()
        level1.startLevel1()

    def inputWrong (self, value):
        if value == 0:
            sentence = "Heyrðu nú mig! Það má aðeins velja svarmöguleika já/nei, svo reyndu aftur!\n"
        elif value == 1:
            sentence = "Heyrðu nú mig! Það má aðeins velja svarmöguleika (1, 2, 3, 4), svo reyndu aftur!\n"
        elif value == 2:
            sentence = "Heyrðu nú mig! Þú verður að ýta á \"enter\" til að halda áfram, svo reyndu aftur\n"
        else:
            sys.exit()
        return sentence

    def readyInput(self):
        words = ""
        self.ready = input("Ýttu á \"enter\" þegar þú ert tilbúin/nn að halda áfram:\n")
        if self.ready == "":
            return words
        else:
            sentence = self.inputWrong(2)
            print(sentence)
            time.sleep(2)
            self.readyInput()

    def looseLevel(self):
        print("Nú hefur þú brugðist félögum þínum í Hogwarts, þú ert komin/nn aftur á byrjunarreit\n")
        keepGoing = input("Viltu reyna aftur við leikinn? (já/nei)\n ")
        if keepGoing == 'já':
            self.beginning()
        elif keepGoing == 'nei':
            sys.exit()
        else:
            sentence = self.inputWrong(0)
            print(sentence)
            self.looseLevel()
            time.sleep(2)

class Level1(Level):
    def __init__(self):
        self.choice = ""
        super(Level, self).__init__()

    def __del__(self):
       print("destructor")

    def startLevel1(self):
        print("Nú erum við staðsett í Diagon Alley")
        time.sleep(2)
        self.createCharacter()

    def createCharacter(self):
        self.choice = input("Viltu velja karakter? (já/nei) \n")
        #Búum til tilvik af klasanum chooseChar() (þessum object)
        chooseChar = ChooseChar()
        if self.choice == 'já' :
            print ("Velkomin/nn í búningaherbergið")
            time.sleep(2)
            self._character = chooseChar.choice()
            print('Þú ert ' + self._character.getName())
            time.sleep(2)
            print(self._character.getDescription())
            time.sleep(2)
            self.happyChoice()
        elif self.choice == 'nei':
            sys.exit()
        else:
            sentence = self.inputWrong(0)
            print(sentence)
            self.createCharacter()
    #fær inn tilvikið af character til að halda áfram að vinna með það
    def happyChoice(self):
        level2 = Level2(self._character)
        confirm = input('Ertu ánægð/ur með valið? (já/nei)\n')
        if confirm == 'já':
            print("Ertu tilbúin/nn? Nú hefst ferð á vit ævintýranna. \nGakktu nú um borð í lestina sem er við lestarpall 9 3/4 \nsem flytur þig í galdraskólann Hogwarts!\n")
            time.sleep(2)
            self.readyInput()
            print("Velkomin/nn í borð 2! Farðu varlega á vit ævintýranna\n")
            time.sleep(2)
            level2.findWand()
        elif confirm == 'nei':
            print("Nú jæja, þá stenduru frammi fyrir ákvörðun...")
            time.sleep(2)
            self.createCharacter()
        else:
            sentence = self.inputWrong(0)
            print(sentence)
            self.happyChoice()

class Level2(Level):
    def __init__(self, selectedCharacter):
        self._character = selectedCharacter
        self.choiceWand = ""
        self.wand = ""
        self.countWand = 0
        super(Level, self).__init__()

    def __del__(self):
       print("destructor")

    #Setjum upp skeiðklukku og leikmaður hefur ákveðinn langa tíma til að finna 3 sprota
    def findWand(self):
        print("Þú ert nemandi í galdraskólanum en hinn alræmdi Lávarður Valdimar hefur stolið galdrasprotanum þínum og vina þinna. Þið eruð að verða of sein í próf og þurfið að hafa galdrasprotana með ykkur því annars verðið þið rekin úr skólanum. Markmið þitt er að finna sprotana en það er erfiðara en þú heldur og tíminn en naumur. Lávarður Valdimar birtist ef þú ert of lengi að leita og gerir þig brottrækan úr heimi ævintýranna! Þú þarft að finna 3 sprota á gefnum tíma, en ef þú nærð 2 sprotum færðu annað tækifæri til að spreyta þig en annars ertu gerður brottrækur fyrir fullt og allt!\n")

        time.sleep(3)

        self.readyInput()
        words = "Galdrasprotarnir eru faldir undir einni af eftirfarandi 4 töfraskikkjum. Hafðu í huga að þú getur aðeins fundið 1 sprota í einu.\n"
        print(words)
        time.sleep(2)
        self.chooseWand()

    def chooseWand(self):
        level4 = Level4(self._character)
        listi = [1, 2, 3, 4]
        self.wand = random.randint(1,4)
        listi.remove(self.wand)
        self.countWand = 0
        #Setjum af stað skeiðklukku svo leikmaður hafi takmarkaðan tíma
        now = time.time()
        timeLimit = now + 20
        #Gera lykkju sem hættir þegar tíminn rennur út
        while time.time() < timeLimit:
            try:
                self.choiceWand = int(input("Undir hvaða skikkju er töfrasproti? (1, 2, 3, 4)?\n"))
                if self.choiceWand == self.wand:
                    self.countWand = self.countWand + 1
                    print("Vel gert " +  self._character.getName() + ", þú fannst 1 töfrasprota! Núna ertu komin með " + str(self.countWand) + " sprota.")
                    if self.countWand == 1:
                        print("Nú vantar þig aðeins 2 sprota til viðbótar")
                        listi = [1, 2, 3, 4]
                        self.wand = random.randint(1,4)
                        listi.remove(self.wand)

                    elif self.countWand == 2:
                        print("Nú vantar þig aðeins 1 sprota til viðbótar\n")
                        listi = [1, 2, 3, 4]
                        self.wand = random.randint(1,4)
                        listi.remove(self.wand)

                    elif self.countWand == 3:
                        print("Til hamingju, þú hefur fundið alla 3 sprotanna og þar með bjargað þér, " + self._character.getName() + ", og félögum þínum frá brottrekstri.\n")
                        self.readyInput()
                        words = "Gakktu hægt um gleðinnar dyr þegar stígur þín fyrstu skref inn í borð 3. " + self._character.getName() + ", þú ert mætt/ur í lokapróf í Hogwarts...\n"
                        print(words)
                        level4.startLevel4()
                elif self.choiceWand == listi[0] or self.choiceWand == listi[1] or self.choiceWand == listi[2]:
                    print("Því miður, gettu betur! En hafðu hraðar hendur því Lávarður Valdimar nálgast!\n")
                else:
                    sentence = self.inputWrong(1)
                    print(sentence)
            except ValueError:
                sentence = self.inputWrong(1)
                print(sentence)

        if self.countWand == 2:
            print("Tíminn er liðinn!\n Þú náðir aðeins 2 sprotum og skilur einn vin þinn eftir sprotalausan. Reyndu nú aftur og í þetta sinn náðu 3 sprotum!\n")
            time.sleep(3)
            self.readyInput()
            self.chooseWand()

        elif self.countWand == 1 or self.countWand == 0:
            print("Tíminn er liðinn!\n Fjöldi sprota er aðeins: " + str(self.countWand) + " litla flón! Lávarður Valdimar er mættur og gerir þig brottrækan úr heimi ævintýra, óbreytti muggi!\n")
            self.looseLevel()

class Level3(Level):

    def __init__(self, selectedcharacter):
        self._character = selectedcharacter
        super(Level, self).__init__()

#SJÁ Í LEVEL3 file-num

    def __del__(self):
        print ('destructor')

class Level4(Level):
    def __init__(self, selectedCharacter):
        self._character = selectedCharacter
        self._lives = 3
        super(Level, self).__init__()

    def __del__(self):
       print("destructor")

    def startLevel4(self):
        self.readyInput()
        words = "Velkomin í borð númer 4!\n"
        print(words)
        print("Þú hefur nú náð bóklega hluta námsins í Hogwarts og ert kominn skrefinu nær því að útskrifast sem alvöru galdramaður, " + self._character.getName() + ". Til að ljúka burtfararprófi verður lögð fyrir þig verkleg þraut. Þú átt að nýta þér þá galdra sem þér hafa verið kenndir beita sprotanum þínum í að galdra fram rétt orð. \nAthugaðu að hér er aðeins notast við enska stafrófið og lágstafi.\nAðeins velja einn staf í einu\n")
        time.sleep(1)
        self.wordPlay()

    def wordPlay(self):
        lev4 = Hangman(self._lives)
        playerChoice = input("Ertu tilbúin í lokaþraut þína í Hogwarts? (já/nei): \n")
        if playerChoice == "já":
            print("Þú byrjar 3 með \"líf\" eða eins og Dumbledore kallar það \"tækifæri\". Good luck...\n")
            puzzle = lev4.wordPuzzle()

            while puzzle == "still alive":
                self.readyInput()
                puzzle = lev4.wordPuzzle()
            if puzzle == "loss":
                self.readyInput()
                self.looseLevel()

            print("\nThe end! Takk fyrir að spila leikinn Haraldur Pottur og félagar í háska, vertu velkominn aftur!")
            sys.exit()

        elif playerChoice == "nei":
            print("Hér í Hogwarts er ekki liðinn aumingjaskapur svo þú ert hér með gerð/ur brottrækur!")
            time.sleep(3)
            self.looseLevel()
        else:
            sentence = self.inputWrong(0)
            print(sentence)
            self.wordPlay()
