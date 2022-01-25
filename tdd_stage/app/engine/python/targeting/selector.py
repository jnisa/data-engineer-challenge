

from tdd_stage.app.engine.python.crutches.auxiliars import clean_up


class ElementsSelector:

    def __init__(self, schema, elements, vals, key_cols, assets):

        self.cols_to_del = []
        self.key_cols = key_cols

        for pos, subset in enumerate(elements):

            self.cols_to_del.append(self.target_positions(pos, subset, assets))
        

        self.elements_flt = self.take_down(elements)
        self.schema_flt = self.take_down(schema)
        self.vals_flt = self.take_down(vals)


    def target_positions(self, pos: list, subset: list, dims: list):

        '''
        store the indexes that must be erased because they are useless

        :param pos: index of all the columns listed on the subset
        :param subset: list of all the columns 
        :param dims: data dimension under analysis
        '''

        return [idx for idx, val in enumerate(subset) if val not in self.key_cols[dims[pos]]]


    def take_down(self, vals_set: list):

        '''
        iteratively goes across all the assets and calls the cleaner

        :param vals_set: set of values that will be filtered
        '''

        return [clean_up(vals_set[idx], val) for idx, val in enumerate(self.cols_to_del)]
