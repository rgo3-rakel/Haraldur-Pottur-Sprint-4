import unittest
from unittest import mock
from unittest.mock import patch
import sys
import random
import os
import io
from io import StringIO
from subprocess import call

from level import Level
from level import Level1
from level import Level2
from character import Character
from character import ChooseChar
from character import HermioneGranger
from hangman import Hangman

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.lev = Level()

    def test_1(self):
        self.assertEqual(self.lev.inputWrong(0), 'Heyrðu nú mig! Það má aðeins velja svarmöguleika já/nei, svo reyndu aftur!\n')
        self.assertEqual(self.lev.inputWrong(2), 'Heyrðu nú mig! Þú verður að ýta á \"enter\" til að halda áfram, svo reyndu aftur\n')

    def test_2(self):
        self.assertEqual(self.lev.readyInput(), "")
        self.assertEqual(self.lev.ready, "")





#Hvernig fer ég að því að test-a hvort að fallið fari inn í annað fall?
#Nánast enginn föllin hafa return gildi, hvernig útfæri ég það? -> ef mock, þá hvernig fæ ég það til að virka?
#Hvernig tækla ég random breyturnar?
#Ég enda alltaf á því að fara inn í miðjan leikinn þegar í unittestinu! hvernig kemst ég framhjá því??



class TestLevel2(unittest.TestCase):
    def setUp(self):
        selectedCharacter = HermioneGranger()
        self.lev2 = Level2(selectedCharacter)

class TestLevel4(unittest.TestCase):
    def setUp(self):
        selectedCharacter = HermioneGranger()
        self.lev2 = Level2(selectedCharacter)

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.char = Character()

    def test_3(self):
        self.char = Character()
        self.char.setName("Haraldur Pottur")
        self.char.setDescription("Hinn útvaldi! Haraldur Pottur er 16 ára galdrastrákur sem hefur ekki átt sjö dagana sæla. Hann hefur barist við sjálfan Lávarð Valdimar og býr hann því að mikilli reynslu. Haraldur er fljótur á fótum og ræður við galdra sem fáir jafnaldrar hans þora að kljást við.\n")
        self.assertEqual(self.char.getName(), "Haraldur Pottur")
        self.assertEqual(self.char.getDescription(), "Hinn útvaldi! Haraldur Pottur er 16 ára galdrastrákur sem hefur ekki átt sjö dagana sæla. Hann hefur barist við sjálfan Lávarð Valdimar og býr hann því að mikilli reynslu. Haraldur er fljótur á fótum og ræður við galdra sem fáir jafnaldrar hans þora að kljást við.\n")

class TestHangman(unittest.TestCase):
    def setUp(self):
        self.a = Hangman(3)

    def test_4(self):
        self.assertEqual(self.a.rightGuess("ron", "___", "r"), "r__")

    def test_5(self):
        f = open("eitthvad.txt")
        sys.stdin = f
        self.a._lives = 3
        self.assertEqual(self.a.wordPuzzle(), "still alive")
        f.close

    def test_6(self):
        sys.stdin = open("eitthvad.txt")
        self.a._lives = 1
        self.assertEqual(self.a.wordPuzzle(), "loss")
        f.close

unittest.main()
