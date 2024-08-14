import unittest
from zabeg import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        Runner(name='Alex')

        for i in range(10):
            Runner.walk = 50
            self.assertEqual(Runner.walk, 50)

    def test_run(self):
        Runner(name='Pavel')

        for i in range(10):
            Runner.run = 100
            self.assertEqual(Runner.run, 100)

    def test_challenge(self):
        Runner(name='Lena')
        Runner(name='Vova')

        for i in range(10):
            Runner.walk = 50
            Runner.run = 100
            self.assertNotEqual(Runner.walk, 100)
            self.assertNotEqual(Runner.run, 50)
