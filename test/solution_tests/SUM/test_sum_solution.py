from pytest import raises
from solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

        assert raises(ValueError, SumSolution().compute("1", "3"))

