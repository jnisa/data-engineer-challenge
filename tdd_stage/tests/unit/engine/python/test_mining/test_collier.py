

import unittest
from tdd_stage.app.engine.python.mining.collier import collier



class TestSchemaExtractor(unittest.TestCase):

    def test_collier_tc1(self):

        '''
        collier - 1st Test Case Scenario
        Complexity: 1/4
        '''

        map = {'transactions': 0}

        path = [
            ['payment', 'table'],
            ['payment', 'column_values'],
            ['payment', 'column_types'], 
            ['payment', 'column_names']
        ]

        data = [ 
        {
            'payment': [
            {
                'table': 'transactions',
                'type': 'credit card',
                'column_names': ['purchase_location', 'bank_id', 'amount'],
                'column_types': ['string', 'string', 'float'],
                'column_values': ['Lisbon, Baixa-Chiado', 'CGD', '125.99']
            }]
        },
        {
            'payment': [
            {
                'table': 'transactions', 
                'type': 'money',
                'column_names': ['purchase_location', 'bank_id', 'amount'],
                'column_types': ['string', 'string', 'float'],
                'column_values': ['Lisbon, Telheiras', 'null', '12.5']
            }]
        }
        ]

        schema_exp = [['string', 'string', 'float']]
        columns_exp = [['purchase_location', 'bank_id', 'amount']]
        values_exp = [[
            ['Lisbon, Baixa-Chiado', 'CGD', '125.99'],
            ['Lisbon, Telheiras', 'null', '12.5']
        ]]
        expected = (schema_exp, columns_exp, values_exp)

        schema_res, columns_res, values_res = collier(data, len(map), map, path)
        result = (schema_res, columns_res, values_res)

        self.assertEqual(result, expected)