

import unittest
from tdd_stage.app.engine.python.mining.preen import preen
from tdd_stage.app.engine.python.mining.preen import new_els_gen
from tdd_stage.app.engine.python.mining.preen import jsonb_conv
from tdd_stage.app.engine.python.mining.preen import adapt_feature


class TestPreen(unittest.TestCase):

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