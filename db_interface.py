import MySQLdb

host = '162.241.230.118'
user = 'codetran_heroku'
password = 'omPtalTi'
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
    # Example of how to fetch table data:
    conn.query("""SELECT * FROM james_table""")
    result = conn.store_result()

    l  = []
    for i in range(result.num_rows()):
        l.append(result.fetch_row())

    print(l)
    return l
# test_select()