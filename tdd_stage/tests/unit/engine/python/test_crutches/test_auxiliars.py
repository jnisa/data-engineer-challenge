

import unittest
from tdd_stage.app.engine.python.crutches.auxiliars import clean_up
from tdd_stage.app.engine.python.crutches.auxiliars import nested_levls_counter


class TestAuxiliars(unittest.TestCase):

    def test_cleanup_tc1(self):

        '''
        cleanup - 1st Test Case Scenario
        Complexity: 1/4
        '''

        raw_lst = [13, 41, 22, 78, 92, 5]
        targets = [0, 5]

        result = clean_up(raw_lst, targets)
        expected = [41, 22, 78, 92]

        return self.assertEqual(result, expected)


    def test_nested_levls_counter_tc1(self):

        '''
        nested_levls_counter - 1st Test Case Scenario
        Complexity: 1/4
        '''

        raw_lst = [[[1, 2]], [2], [[[10, 2]]]]

        expected = 6
        result = nested_levls_counter(raw_lst)

        self.assertEqual(result, expected)