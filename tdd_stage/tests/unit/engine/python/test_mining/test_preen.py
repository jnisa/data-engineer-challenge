

import unittest
from tdd_stage.app.engine.python.mining.preen import preen


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


    def test_adapt_assets_tc1(self):

        '''
        adapt_assets - 1st Test Case Scenario
        Complexity: 1/4
        '''

        elements = ['car']
        expected_elements = ['car.id', 'car.features.brand', 'car.features.model']

        dtypes = ['jsonb']
        expected_dtypes = [int, str, str]

        data = {
            'car': {
                'id': 1,
                'features' : {
                    'brand': 'Ferrari',
                    'model': '812 Superfast',
                }
            }
        }

        expected = {
            'car.id': 1,
            'car.features.brand': 'Ferrari',
            'car.features.model': '812 Superfast'
        }


        return self.assertEqual()