from django.test import TestCase


class TestCaseOne(TestCase):

    def test_one(self):
        self.assertTrue(True)

    def test_two(self):
        self.assertTrue(False)
