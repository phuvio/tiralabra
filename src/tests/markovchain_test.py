import unittest
from markovchain.markovchain import MarkovChain


class TestMarkovChain(unittest.TestCase):
    def test_next_state_always_same_state(self):
        self._transition_matrix = [[1.0, 0.0, 0.0],
                                   [0.0,  1.0,  0.0],
                                   [0.0,  0.0,  1.0]]
        self._states = ["aurinkoista", "sadetta", "sumua"]
        self._markovchain = MarkovChain(self._transition_matrix, self._states)
        next_state = self._markovchain.next_state("aurinkoista")

        self.assertEqual(next_state, "aurinkoista")

        next_state = self._markovchain.next_state("sadetta")

        self.assertEqual(next_state, "sadetta")

        next_state = self._markovchain.next_state("sumua")

        self.assertEqual(next_state, "sumua")

    def test_next_state_propability(self):
        self._transition_matrix = [[0.5, 0.4, 0.1],
                                   [0.2,  0.4,  0.3],
                                   [0.3,  0.3,  0.4]]
        self._states = ["aurinkoista", "sadetta", "sumua"]
        self._markovchain = MarkovChain(self._transition_matrix, self._states)

        amount = 0
        for _ in range(100000):
            next_state = self._markovchain.next_state("aurinkoista")
            if next_state == "aurinkoista":
                amount += 1

        self.assertAlmostEqual(amount/100000, 0.5, 2)

        amount = 0
        for _ in range(100000):
            next_state = self._markovchain.next_state("aurinkoista")
            if next_state == "sadetta":
                amount += 1

        self.assertAlmostEqual(amount/100000, 0.4, 2)

    def test_future_states(self):
        self._transition_matrix = [[0.5, 0.4, 0.1],
                                   [0.2,  0.5,  0.3],
                                   [0.3,  0.3,  0.4]]
        self._states = ["aurinkoista", "sadetta", "sumua"]
        self._markovchain = MarkovChain(self._transition_matrix, self._states)

        future_states = self._markovchain.generate_states("aurinkoista", 10)

        self.assertEqual(len(future_states), 10)
