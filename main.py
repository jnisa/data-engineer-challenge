

import pdb
import json
import sqlite3


from tdd_stage.app.engine.python.mining.collier import collier
from tdd_stage.app.engine.python.mining.preen import unfold_jsonb
from tdd_stage.app.engine.python.targeting.selector import ElementsSelector
from tdd_stage.app.engine.python.crutches.auxiliars import get_pipeline_confs



con = sqlite3.connect('metrics.db')
cur = con.cursor()

# Create table - this is an example, you should create a table called metrics or similar
# cur.execute('''CREATE TABLE stocks
#               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data - again, just for illustration
# cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
# con.commit()

# Read the WAL records
with open("./data/1_raw_zone/wal.json", "r") as f:
    records = json.loads(f.read())

# Variables
map, pin_points, key_cols = get_pipeline_confs()
schema, elements, vals = collier(records, len(map), map, pin_points)
tables = list(map.keys())
el_select = ElementsSelector(schema, elements, vals, key_cols, list(tables))

pdb.set_trace()

schema, columns, values = unfold_jsonb(el_select.schema[0], el_select.elements[0], el_select.vals[0])

pdb.set_trace()