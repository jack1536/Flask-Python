# mysql related imports
from sqlalchemy import create_engine
import urllib.parse
import sql_info
import MySQLdb
from MySQLdb.constants import FIELD_TYPE


def create_sql_alchemy_engine():
    user = urllib.parse.quote_plus(sql_info.get_user())
    passwd = urllib.parse.quote_plus(sql_info.get_password())
    host = urllib.parse.quote_plus(sql_info.get_host())
    port = urllib.parse.quote_plus(str(sql_info.get_port()))
    db = urllib.parse.quote_plus(sql_info.get_db_name())
    url = 'mysql://' + user + ':' + passwd + '@' + host + '/' + db
    return create_engine(url)


def establish_connection():
    """
    Establishes connection with database
    """
    conn = MySQLdb.Connection(
        conv={
            FIELD_TYPE.LONG: int,
            FIELD_TYPE.DECIMAL: int
        },  # FIXME: this does not seem to be working yet TAIGA#10
        host=sql_info.get_host(),
        user=sql_info.get_user(),
        passwd=sql_info.get_password(),
        port=sql_info.get_port(),
        db=sql_info.get_db_name())

    return conn


def execute_query(q):
    # set up sql connection
    conn = establish_connection()

    conn.query(q)
    result = conn.store_result()

    return result


def query_to_json(q):
    result = execute_query(q)
    out = result.fetch_row(how=1, maxrows=0)

    # if query doesn't return anything, return object with empty lists
    if len(out) == 0:
        return {"column_names": [], "rows": []}

    # column names are grabbed from first row
    out = {"column_names": list(out[0].keys()), "rows": list(out)}

    # add the rest of the rows to data
    # l = result.fetch_row(maxrows=0, how=0)
    # out["rows"].extend(l)

    return out
