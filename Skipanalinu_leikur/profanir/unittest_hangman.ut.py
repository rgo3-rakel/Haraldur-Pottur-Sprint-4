import unittest
from unittest import mock
from unittest.mock import patch
import sys
import random
import os
import io
from io import StringIO
from subprocess import call

from hangman import Hangman

class TestHangman(unittest.TestCase):
    call(['clear'])
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
        f = open("eitthvad.txt")
        sys.stdin = f
        self.a._lives = 1
        self.assertEqual(self.a.wordPuzzle(), "loss")
        f.close

if __name__ == '__main__':
    unittest.main()
