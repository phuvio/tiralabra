import numpy as np


class MarkovChain:
    """Luokka, joka kuvaa Markovin ketjua

    Args:
        object (_type_): _description_
    """

    def __init__(self, transition_matrix, states):
        """Luokan konstruktori, joka luo uuden Markovin ketjun matriisin

        Args:
            transition_matrix: 2D-array
                2D-array, joka kuvaa Markovin ketjun tilojen muutosten todennäköisyyttä
            states: 1D-array
                1D-array, joka kuvaa Markovin ketjun tiloja.
                Tilojen pitää olla samassa järjestyksessä kuin transition_matrix:ssa.
        """
        self.transition_matrix = np.atleast_2d(transition_matrix)
        self.states = states
        self.index_dict = {
            self.states[index]: index for index in range(len(self.states))}
        self.states_dict = {index: self.states[index]
                            for index in range(len(self.states))}

    def next_state(self, current_state):
        """Palauttaa järjestelmän seuraavan tilan

        Args:
            current_state: str
                järjestelmän nykyinen tila
        """
        return np.random.choice(
            self.states,
            p=self.transition_matrix[self.index_dict[current_state], :]
        )

    def generate_states(self, current_state, number=10):
        """Luo järjestelmän seuraavan tilan

        Args:
            current_state: str
                Järjestelmän nykyinen tila
            no: int
                Järjestelmän tulevien generoitavien tilojen määrä
        """
        future_states = []
        for _ in range(number):
            next_state = self.next_state(current_state)
            future_states.append(next_state)
            current_state = next_state
        return future_states
