


import unittest

from tdd_stage.app.engine.python.sqlite.methods import create_table
from tdd_stage.app.engine.python.sqlite.methods import data_load


class TestSQLiteMethods(unittest.TestCase):

    def test_create_table_tc1(self):

        '''
        create_table - 1st Test Case Scenario
        Complexity: 1/4
        '''

        table_id = 'test_table_1'
        cols_set = ['column_1', 'column_2', 'column_3', 'column_4']
        dtypes_set = ['str', 'int', 'bool', 'str']

        expected = "CREATE A TABLE IF NOT EXISTS test_table_1 (column_1 str, column_2 int, column_3 bool, column_4 str)"
        result = create_table(table_id, cols_set, dtypes_set)

        return self.assertEqual(result, expected)


    def test_data_load_tc1(self):

        '''
        data_load - 1st Test Case Scenario
        Complexity: 1/4
        '''

        table_id = 'test_table_1'
        cols_set = ['column_1', 'column_2', 'column_3']

        expected = "INSERT INTO test_table_1 (column_1, column_2, column_3) VALUES (?, ?, ?)" 
        result = data_load(table_id, cols_set)

        return self.assertEqual(result, expected)