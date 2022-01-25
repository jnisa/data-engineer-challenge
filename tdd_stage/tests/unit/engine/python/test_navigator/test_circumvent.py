

import unittest
from tdd_stage.app.engine.python.navigator.circumvent import circumvent


class TestCircumvent(unittest.TestCase):

    def test_circumvent_tc1(self):

        '''
        circumvent - 1st Test Case Scenario
        Complexity: 1/4
        '''

        data = {'a': 42, 'c': 12, 'b': [{1: 2, 2: 3, 3: 4}]}

        result = circumvent(data, ['a', 'b', 1])
        expected = [42, 2]

        return self.assertEqual(result, expected)