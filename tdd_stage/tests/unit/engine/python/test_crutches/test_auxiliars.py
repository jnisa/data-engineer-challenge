

import unittest
from tdd_stage.app.engine.python.crutches.auxiliars import clean_up


class TestAuxiliars(unittest.TestCase):

    def test_cleanup_tc1(self):

        '''
        cleanup - 1st Test Case Scenario
        Complexity: 1/4
        '''

        raw_lst = [13, 41, 22, 78, 92, 5]
        targets = [0, 5]

        result = clean_up(raw_lst, targets)
        expected = [41, 22, 78, 5]

        return self.assertEqual(result, expected)