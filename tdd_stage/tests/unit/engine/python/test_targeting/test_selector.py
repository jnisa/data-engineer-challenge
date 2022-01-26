

import pdb
import unittest
from tdd_stage.app.engine.python.targeting.selector import ElementsSelector


class TestElementsSelector(unittest.TestCase):

    def test_target_position_tc1(self):

        '''
        target_position - 1st Test Case Scenario
        Complexity: 1/4
        '''

        assets = ['dimension_1']
        dtypes = [[int, str, int, str]]
        vals = [[123, '123', 456, '456']]
        key_cols = {'dimension_1': ['column_2', 'column_4']}
        columns = [['column_1', 'column_2', 'column_3', 'column_4']]

        selector = ElementsSelector(dtypes, columns, vals, key_cols, assets)

        expected = [[0, 2]]
        result = selector.cols_to_del

        return self.assertEqual(result, expected)


    def test_take_down_tc1(self):

        '''
        take_down - 1st Test Case Scenario
        Complexity: 1/4
        '''

        assets = ['dimension_1']
        dtypes = [[int, str, int, str]]
        vals = [[[123, '123', 456, '456'], [789, '789', 112, '112']]]
        key_cols = {'dimension_1': ['column_2', 'column_4']}
        columns = [['column_1', 'column_2', 'column_3', 'column_4']]

        selector = ElementsSelector(dtypes, columns, vals, key_cols, assets)

        expected_els = [['column_2', 'column_4']]
        expected_vals = [[['123', '456'], ['789', '112']]]
        expected_schema = [[str, str]]

        expected = (expected_els, expected_schema, expected_vals)

        result = (selector.elements, selector.schema, selector.vals)

        return self.assertEqual(result, expected)