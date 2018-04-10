class Level3(Level):
    def __init__(self, selectedcharacter):
        #spurning4 = prof4()
        self._character = selectedcharacter

    def __del__(self):
        print ('destructor')

    def questionGame(self):
        level4 = Level4(self._character)
        print("Þú ert í lokaprófi í Hogwarts og þarf að ná að svara öllum eftirfarandi spurningum rétt, ef þú færð rangt svar ertu fallinn og gerður brottrækur úr skólanum.\n")
        time.sleep(3)

        prof = input("Nú stenduru uppi fyrir vali, þú mátt velja úr 4 mismunandi prófum til þess að leysa. Hvaða próf viltu leysa (1,2,3,4)?")

        if prof == '4':
            print("Þú hefur valið próf sem hentar vel fyrir Guðrúnu\n")
            prof41.read_data41(self)
            time.sleep(3)
            val = input("Hvert er svarið? (1,2,3,4)\n")
            if val == '1' or val == '2' or val == '3':
                print("Nú ert þú í klófestu Lávarðs Valdimars og er " + self._character.getName() + " hér með rekin/nn úr Hogwarts!!")
                time.sleep(6)
                sys.exit()
            if val == '4':
                print("Hárrétt " + self._character.getName() + "!!\n")
                #Kalla hérna á spurningu 2!
                self.spurning4.read_data4_2()
                time.sleep(3)
                val = input("Hvert er svarið? (1,2,3,4)\n")
                if val == '1' or val == '2' or val == '3':
                    print("Nú ert þú í klófestu Lávarðs Valdimars og er " + self._character.getName() + " hér með rekin/nn úr Hogwarts!!")
                    time.sleep(6)
                    sys.exit()
                if val == '4':
                    print("Hárrétt " + self._character.getName() + "!!\n")
                    self.spurning4.read_data4_3()
                    val = input("Hvert er svarið? (1,2,3,4)\n")
                    if val == '1' or val == '2' or val == '3':
                        print("Nú ert þú í klófestu Lávarðs Valdimars og er " + self._character.getName() + " hér með rekin/nn úr Hogwarts!!")
                        time.sleep(6)
                        sys.exit()
                    if val == '4':
                        print("Hárrétt " + self._character.getName() + "!!\n")
                        self.spurning4.read_data4_4()
                        val = input("Hvert er svarið? (1,2,3,4)\n")
                        if val == '1' or val == '2' or val == '4':
                            print("Nú ert þú í klófestu Lávarðs Valdimars og er " + self._character.getName() + " hér með gerður brottrækur úr Hogwarts!!")
                            time.sleep(6)
                            sys.exit()
                        if val == '3':
                            print("Hárrétt " + self._character.getName() + "!!\n")
                            print("Þú hefur nú lokið öllu bóklega námi galdraskólans Hogwarts! Gakktu hægt um gleðinnar dyr og mundu að nýta þér aðeins galdra í neyð.\n")
                            time.sleep(2)
                            self.readyInput()
                        else:
                            sentence = self.inputWrong(1)
                            print(sentence)
                            time.sleep(2)
                            self.questionGame()
                    else:
                        sentence = self.inputWrong(1)
                        print(sentence)
                        time.sleep(2)
                        self.questionGame()
                else:
                    sentence = self.inputWrong(1)
                    print(sentence)
                    time.sleep(2)
                    self.questionGame()

            else:
                sentence = self.inputWrong(1)
                print(sentence)
                time.sleep(2)
                self.questionGame()
