

import unittest
from tdd_stage.app.engine.python.parser.extractor import preen
from tdd_stage.app.engine.python.parser.extractor import collier
from tdd_stage.app.engine.python.parser.extractor import jsonb_conv
from tdd_stage.app.engine.python.parser.extractor import circumvent
from tdd_stage.app.engine.python.parser.extractor import new_els_gen
from tdd_stage.app.engine.python.parser.extractor import adapt_feature


class TestExtractor(unittest.TestCase):

    def test_circumvent_tc1(self):

        '''
        circumvent - 1st Test Case Scenario
        Complexity: 1/4
        '''

        data = {'a': 42, 'c': 12, 'b': [{1: 2, 2: 3, 3: 4}]}

        result = circumvent(data, ['a', 'b', 1])
        expected = [42, 2]

        return self.assertEqual(result, expected)


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


    def test_preen_tc1(self):

        '''
        preen - 1st Test Case Scenario
        Complexity: 1/4
        '''

        data = {
            'car_id': 1,
            'features' : {
                'brand': 'Ferrari',
                'model': '812 Superfast',
            },
            'car_id': 2,
            'features': {
                'brand': 'Ferrari',
                'model': 'F8 Spider'
            }
        }

        expected = {
            'car_id': 1,
            'features.brand': 'Ferrari',
            'features.model': '812 Superfast',
            'car_id': 2,
            'features.brand': 'Ferrari',
            'features.model': 'F8 Spider'
        }

        result = preen(data)

        return self.assertEqual(result, expected)


    def test_preen_tc2(self):

        '''
        preen - 2nd Test Case Scenario
        Complexity: 2/4
        '''

        data = {
            'car': {
                'id': 1,
                'features' : {
                    'brand': 'Ferrari',
                    'model': '812 Superfast',
                }
            },
            'car': {
                'id': 2,
                'features': {
                    'brand': 'Ferrari',
                    'model': 'F8 Spider'
                }
            }
        }

        expected = {
            'car.id': 1,
            'car.features.brand': 'Ferrari',
            'car.features.model': '812 Superfast',
            'car.id': 2,
            'car.features.brand': 'Ferrari',
            'car.features.model': 'F8 Spider'
        }

        result = preen(data)

        return self.assertEqual(result, expected)


    def test_new_els_gen_tc1(self):

        '''
        new_els_gen - 1st Test Case Scenario
        Complexity: 1/4
        '''

        parent = 'car'
        subnodes = ['id', 'brand', 'model']

        result = new_els_gen(parent, subnodes)
        expected = ['car_id', 'car_brand', 'car_model']

        return self.assertEqual(result, expected)


    def test_jsonb_conv_tc1(self):

        '''
        jsonb_conv - 1st Test Case Scenario
        Complexity: 1/4
        '''

        jsonb_idx = 3

        data = [
            'feature_1',
            'feature_2',
            'feature_3',
            '{"car_id": 1, "car_brand": "Ferrari", "car_model": null, "car_horse_power": "1000cv", "car_value": null}'
        ]

        expected = {
            'car_id': 1,
            'car_brand': 'Ferrari',
            'car_model': None,
            'car_horse_power': '1000cv',
            'car_value': None
        }

        result = jsonb_conv(data, jsonb_idx)

        return self.assertEqual(result, expected)


    def test_adapt_feature_tc1(self):

        '''
        adapt_feature - 1st Test Case Scenario
        Complexity: 1/4
        '''

        idx = 3
        init_data = ['Ferrari', 'F8 Spider', '500k', '1000']
        new_data = ['2018', '3.5s', 'Italian']

        expected = ['Ferrari', 'F8 Spider', '500k', '2018', '3.5s', 'Italian']
        result = adapt_feature(init_data, new_data, idx)

        return self.assertEqual(result, expected)


    def test_adapt_feature_tc2(self):

        '''
        adapt_feature - 2nd Test Case Scenario
        Complexity: 1/4
        '''

        idx = 2
        init_data = ['Ferrari', 'F8 Spider', '500k', '1000']
        new_data = ['2018', '3.5s', 'Italian']

        expected = ['Ferrari', 'F8 Spider', '2018', '3.5s', 'Italian', '1000']
        result = adapt_feature(init_data, new_data, idx)

        return self.assertEqual(result, expected)


    def test_adapt_feature_tc3(self):

        '''
        adapt_feature - 3rd Test Case Scenario
        Complexity: 1/4
        '''

        idx = 0
        init_data = ['Ferrari', 'F8 Spider', '500k', '1000']
        new_data = ['2018', '3.5s', 'Italian']

        expected = ['2018', '3.5s', 'Italian', 'F8 Spider', '500k', '1000']
        result = adapt_feature(init_data, new_data, idx)

        return self.assertEqual(result, expected)