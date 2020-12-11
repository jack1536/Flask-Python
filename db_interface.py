from dotenv import load_dotenv
load_dotenv()
import MySQLdb
import os


host = '162.241.230.118'
user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
port = 3306
db = 'codetran_collegedata'

conn = MySQLdb.Connection(
    host=host,
    user=user,
    passwd=password,
    port=port,
    db=db
)


def test_select():
    print("test select started")

    # Example of how to fetch table data:
    conn.query("""SELECT * FROM james_table""")
    result = conn.store_result()

    l  = []
    for i in range(result.num_rows()):
        l.append(result.fetch_row())

    print("returned list", l)
    return l
