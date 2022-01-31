


def data_prep(vals_set: list):

    '''
    prepares data before making the insert into a new dimension

    :param vals_set: set of values that are about to be reshaped
    '''

    vals_struct = [[] for _ in range(len(vals_set[0]))]
    
    for rec in vals_set:
        for idx, val in enumerate(rec):
            vals_struct[idx].append(val)

    return vals_struct


def create_table(table_id: str, cols_set: list, dtypes: list):

    '''
    creates a tables in our SQLite serverless database

    :param table_id: name of the table that is about to be created
    :param cols_set: list of the column names that will be added to the table
    :param dtypes: list of the data types of all the columns
    '''

    struct = ["%s %s" %(cols_set[i], dtypes[i]) for i in range(len(cols_set))]
    query = "CREATE TABLE IF NOT EXISTS %s %s" %(table_id, str(tuple(struct)))

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


def sql_join(tab1: str, tab2: str, c1: str, c2: str, join_type: str, new_table: str):

    '''
    performs a join between two dimensions

    :param tab1: first table of the join operation
    :param tab2: second table of the join operation
    :param c1: column that will be targeted on the join from 1st table
    :param c2: column that will be targeted on the join from 2nd table
    :param join_type: type of join to be performed
    :param new_table: outcome table from the select command
    '''

    join_map = {
        'left': 'LEFT JOIN',
        'inner': 'INNER JOIN',
        'left outer': 'LEFT OUTER JOIN',
        'cross': 'CROSS JOIN'
    }

    attr1 = '.'.join([tab1, c1])
    attr2 = '.'.join([tab2, c2])

    query = "CREATE TABLE %s AS SELECT * FROM %s %s %s ON %s = %s" %(
        new_table, tab1, join_map[join_type], tab2, attr1, attr2 
    ) 

    return query.replace("'", "")


def drop_columns(table_id: str, select_cols: list, new_table: str):

    '''
    drop columns that are useless to the final answer

    :param table_id: table that will be the center of this operation
    :param select_cols: columns that must be kept
    :param drop_cols: set of columns that will be dropped 
    '''

    query = "CREATE TABLE %s AS SELECT %s FROM %s" %(
        new_table, 
        ', '.join(select_cols), 
        table_id
    )

    return query.replace("'", "")
