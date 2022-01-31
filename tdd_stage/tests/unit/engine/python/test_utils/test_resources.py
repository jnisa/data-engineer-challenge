


import unittest
from tdd_stage.app.engine.python.utils.resources import clean_up
from tdd_stage.app.engine.python.utils.resources import first_ele
from tdd_stage.app.engine.python.utils.resources import check_outliers
from tdd_stage.app.engine.python.utils.resources import nested_levls_counter


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


    def test_first_ele_tc1(self):

        '''
        first_ele - 1st Test Case Scenario
        Complexity: 1/4
        '''

        data = [1, 1, 1, 'abc', 1, 'def']

        expected = 'abc'
        result = first_ele(data, 1)

        return self.assertEqual(result, expected)


    def test_check_outliers_tc1(self):

        '''
        check_outliers - 1st Test Case Scenario
        Complexity: 1/4
        '''

        data = [
            [1, None],
            [2, None],
            [3, 1],
            [4, None],
        ]

        result = check_outliers(None, data, 1)
        expected = True

        return self.assertEqual(result, expected)


    def test_check_outliers_tc2(self):

        '''
        check_outliers - 2nd Test Case Scenario
        Complexity: 1/4
        '''

        data = [
            [1, None],
            [2, None],
            [3, None],
            [4, None],
        ]

        result = check_outliers(None, data, 1)
        expected = False

        return self.assertEqual(result, expected)


    def test_check_outliers_tc3(self):

        '''
        check_outliers - 3rd Test Case Scenario
        Complexity: 1/4
        '''

        data = [
            [1, 'abc'],
            [2, 1],
            [3, 2],
            [4, 'abc'],
        ]

        result = check_outliers('abc', data, 1)
        expected = True

        return self.assertEqual(result, expected)

