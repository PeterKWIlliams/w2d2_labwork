import unittest
from src.train import Train
from src.person_train import PersonTrain

class TestTrain(unittest.TestCase):
    def setUp(self):
        self.train = Train(5, "Waverly", "Glasgow", 20)
        self.person1 = PersonTrain("Khaleesi", 27, 1000, "Glasgow", "Waverly", 5)
        self.person2 = PersonTrain("James", 40, 20, "Waverly", "Glasgow", 2)

    def test_purchase_ticket(self):
        self.assertEqual(0, self.take_cash(self.person2.balance))