

import pdb
from tdd_stage.app.engine.python.crutches.auxiliars import clean_up
from tdd_stage.app.engine.python.crutches.auxiliars import nested_levls_counter


class ElementsSelector:

    def __init__(self, schema, elements, vals, key_cols, assets):

        self.cols_to_del = []
        self.key_cols = key_cols

        for pos, subset in enumerate(elements):

            self.cols_to_del.append(self.target_positions(pos, subset, assets))

        self.elements = self.take_down(elements, len(assets))
        self.schema = self.take_down(schema, len(assets))
        self.vals = self.take_down(vals, len(assets))
        

    def target_positions(self, pos: list, subset: list, dims: list):

        '''
        store the indexes that must be erased because they are useless

        :param pos: index of all the columns listed on the subset
        :param subset: list of all the columns 
        :param dims: data dimension under analysis
        '''

        return [idx for idx, val in enumerate(subset) if val not in self.key_cols[dims[pos]]]


    def take_down(self, vals_set: list, dims_num: int):

        '''
        iteratively goes across all the assets and calls the cleaner

        :param vals_set: set of values that will be filtered
        :param dims_num: number of data dimensions
        '''

        if nested_levls_counter(vals_set) > dims_num:
            ans = [[clean_up(r, val) for r in vals_set[idx]] for idx, val in enumerate(self.cols_to_del)]

        else:
            ans = [clean_up(vals_set[idx], val) for idx, val in enumerate(self.cols_to_del)]

        return ans
