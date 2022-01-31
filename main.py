

import pdb
import json
import sqlite3


from tdd_stage.app.engine.python.sqlite.client import *
from tdd_stage.app.engine.python.parser.extractor import collier
from tdd_stage.app.engine.python.parser.extractor import unfold_jsonb
from tdd_stage.app.engine.python.parser.selector import ElementsSelector
from tdd_stage.app.engine.python.utils.resources import get_pipeline_confs
from tdd_stage.app.engine.python.utils.resources import map_postsql_dtypes



con = sqlite3.connect('metrics.db')
cur = con.cursor()


# Read the WAL records
with open("./data/1_raw_zone/wal.json", "r") as f:
    records = json.loads(f.read())

# Data Transformations
map, pin_points, key_cols, out_cols = get_pipeline_confs()
schema, elements, vals = collier(records, len(map), map, pin_points)
schema = [map_postsql_dtypes(t_set) for t_set in schema]
el_select = ElementsSelector(schema, elements, vals, key_cols, list(map.keys()))

# Replacement of a table name to avoid SQLite conflicts
tables = list(map.keys())
tables[1] = 'transaction_dim'

# Unfold jsonb data types, Create Tables and Loading of Data
for idx, tab in enumerate(tables):
    schema, columns, values = unfold_jsonb(el_select.schema[idx], el_select.elements[idx], el_select.vals[idx])
    cur.execute(create_table(tab, columns, schema))
    cur.executemany(data_load(tab, columns), [tuple(val) for val in values])
    con.commit()

# Perform the Joins
cur.execute(sql_join('transaction_request', 'payment_instrument_token_data', 'token_id', 'token_id', 'inner', 'join_dim1'))
cur.execute(sql_join('event_v2_data', 'join_dim1', 'flow_id', 'flow_id', 'inner', 'join_dim2'))
cur.execute(sql_join('join_dim2', 'transaction_dim', 'transaction_id', 'transaction_id', 'inner', 'join_dim3'))
cur.execute(drop_columns('join_dim3', out_cols, 'expected_dim'))
con.commit()
con.close()
