

import pdb
import json
import sqlite3


from tdd_stage.app.engine.python.mining.collier import collier
from tdd_stage.app.engine.python.mining.preen import unfold_jsonb
from tdd_stage.app.engine.python.targeting.selector import ElementsSelector



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
with open("./wal.json", "r") as f:
    records = json.loads(f.read())

# Variables

dims = 4

map = {
    'event_v2_data': 0,
    'transaction': 1,
    'transaction_request': 2,
    'payment_instrument_token_data': 3
}
pin_points = [['change', 'table'], ['change', 'columnvalues'], ['change', 'columntypes'], ['change', 'columnnames']]
schema, elements, vals = collier(records, dims, map, pin_points)
key_cols = {
    'event_v2_data': ['event_id', 'flow_id', 'transaction_id', 'transaction_lifecycle_event', 'created_at', 'error_details'],
    'transaction': ['transaction_type', 'transaction_id', 'processor_merchant_account_id', 'amount', 'currency_code'],
    'transaction_request': ['flow_id', 'vault_options', 'token_id'],
    'payment_instrument_token_data': ['token_id', 'payment_instrument_type', 'vault_data', 'three_d_security_authentication']
}
tables = list(map.keys())

el_select = ElementsSelector(schema, elements, vals, key_cols, list(tables))

schema, columns, values = unfold_jsonb(el_select.schema[0], el_select.elements[0], el_select.vals[0])
pdb.set_trace()