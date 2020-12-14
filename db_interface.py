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


def execute_query(q):
    conn.query(q)
    result = conn.store_result()

    # l  = []
    # for i in range(result.num_rows()):
    #     l.append(result.fetch_row())

    # l = result.fetch_row(maxrows=0, how=1)

    # print("returned list", l)
    return result


# {'school_name': 'Columbia University in the City of New York', 'latest_student_size': Decimal('8216.0')}

def query_to_json(q):
    result = execute_query(q)
    result_temp = result

    first_row = result.fetch_row(how=1)
    if len(first_row) == 0:
        return {"column_names": [], "data": []}

    # column names are grabbed from first row TODO: catch error if no data is returned
    out = {
        "column_names": list(first_row[0].keys()),
        "data": [tuple(first_row[0].values())]  
        }

    # add the rest of the rows to data
    l = result.fetch_row(maxrows=0, how=0)
    out["data"].extend(l)

    return out










# execute_query("""SELECT * FROM james_table""")
# execute_query("SELECT * FROM james_table")
# execute_query("SELECT school_name, latest_student_size FROM codetran_collegedata.collegescorecard WHERE latest_admissions_act_scores_midpoint_cumulative BETWEEN 32 AND 36 AND latest_student_size BETWEEN 0 AND 50000")
query_to_json("SELECT school_name, latest_student_size FROM codetran_collegedata.collegescorecard WHERE latest_admissions_act_scores_midpoint_cumulative BETWEEN 34 AND 30 AND latest_student_size BETWEEN 0 AND 50000")
# test_select()