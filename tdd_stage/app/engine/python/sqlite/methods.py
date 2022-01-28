



def create_table(table_id: str, cols_set: list, dtypes: list):

    '''
    creates a tables in our SQLite serverless database

    :param table_id: name of the table that is about to be created
    :param cols_set: list of the column names that will be added to the table
    :param dtypes: list of the data types of all the columns
    '''

    struct = ["%s %s" %(cols_set[i], dtypes[i]) for i in range(len(cols_set))]
    query = "CREATE A TABLE IF NOT EXISTS %s %s" %(table_id, str(tuple(struct)))

    return query.replace("'","")


def data_load(table_id: str, cols_set: list):

    '''
    load the provided data to the table

    :param table_id: table that will suffer a data load
    :param cols_set: set of cols to complete the query
    '''

    vals_spots = tuple(['?'] * len(cols_set))
    query = "INSERT INTO %s %s VALUES %s" %(table_id, tuple(cols_set), str(vals_spots))

    return query.replace("'", "")