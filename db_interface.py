from dotenv import load_dotenv
load_dotenv()
import MySQLdb
from MySQLdb import _mysql
import os
from MySQLdb.constants import FIELD_TYPE


host = '162.241.230.118'
user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
port = 3306
db = 'codetran_collegedata'
my_conv = { FIELD_TYPE.LONG: int, FIELD_TYPE.DECIMAL: int}

conn = MySQLdb.Connection(
    conv = my_conv, # FIXME: this does not seem to be working yet TAIGA#10
    host=host,
    user=user,
    passwd=password,
    port=port,
    db=db
)

def execute_query(q):
    conn.query(q)
    result = conn.store_result()

    return result


def query_to_json(q):
    result = execute_query(q)
    first_row = result.fetch_row(how=1)

    # if query doesn't return anything, return object with empty lists
    if len(first_row) == 0:
        return {"column_names": [], "rows": []}

    # column names are grabbed from first row
    out = {
        "column_names": list(first_row[0].keys()),
        "rows": [tuple(first_row[0].values())]  
        }

    # add the rest of the rows to data
    l = result.fetch_row(maxrows=0, how=0)
    out["rows"].extend(l)

    return out


