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

def query_to_dict_of_lists(q):
    result = execute_query(q)

    return result.fetch_row(maxrows=0, how=1)










# execute_query("""SELECT * FROM james_table""")
# execute_query("SELECT * FROM james_table")
# execute_query("SELECT school_name, latest_student_size FROM codetran_collegedata.collegescorecard WHERE latest_admissions_act_scores_midpoint_cumulative BETWEEN 32 AND 36 AND latest_student_size BETWEEN 0 AND 50000")
query_to_dict_of_lists("SELECT school_name, latest_student_size FROM codetran_collegedata.collegescorecard WHERE latest_admissions_act_scores_midpoint_cumulative BETWEEN 32 AND 36 AND latest_student_size BETWEEN 0 AND 50000")
# test_select()