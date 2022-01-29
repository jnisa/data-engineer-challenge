


import unittest

from tdd_stage.app.engine.python.sqlite.methods import sql_join
from tdd_stage.app.engine.python.sqlite.methods import data_load
from tdd_stage.app.engine.python.sqlite.methods import data_prep
from tdd_stage.app.engine.python.sqlite.methods import create_table


class TestSQLiteMethods(unittest.TestCase):

    def test_data_prep_tc1(self):

        '''
        data_prep - 1st Test Case Scenario
        Complexity: 1/4
        '''

        vals_set = [
            ['abc', 1, 'def'], 
            ['ghi', 2, 'jkl'], 
            ['mno', 3, 'pqr']
        ]

        result = data_prep(vals_set)
        expected = [['abc', 'ghi', 'mno'], [1, 2, 3], ['def', 'jkl', 'pqr']]

        return self.assertEqual(result, expected)


    def test_create_table_tc1(self):

        '''
        create_table - 1st Test Case Scenario
        Complexity: 1/4
        '''

        table_id = 'test_table_1'
        cols_set = ['column_1', 'column_2', 'column_3', 'column_4']
        dtypes_set = ['str', 'int', 'bool', 'str']

        expected = "CREATE TABLE IF NOT EXISTS test_table_1 (column_1 str, column_2 int, column_3 bool, column_4 str)"
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


    def test_sql_join_tc1(self):

        '''
        sql_join - 1st Test Case Scenario
        Complexity: 1/4
        '''

        result = sql_join('table1', 'table2', 'id', 'id', 'left', 'new_table_1')
        expected = "CREATE TABLE new_table_1 AS SELECT * FROM table1 LEFT JOIN table2 ON table1.id = table2.id"

        return self.assertEqual(result, expected)

