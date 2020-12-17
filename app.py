# flask imports
from flask import Flask
from flask_restful import Resource, reqparse, Api
from flask_cors import CORS

# mysql related imports
import MySQLdb
from MySQLdb.constants import FIELD_TYPE
from dotenv import load_dotenv
load_dotenv()  # loads in .env variables
import os

# other imports
from querybuilder import build_query
from db_interface import query_to_json


# Start flask app
app = Flask(__name__)
CORS(app)
api = Api(app)
app.config[
    'PROPAGATE_EXCEPTIONS'] = True  # TODO: figure out if this is what I want

# set up sql connection
conn = MySQLdb.Connection(
    conv={FIELD_TYPE.LONG: int, FIELD_TYPE.DECIMAL: int},  # FIXME: this does not seem to be working yet TAIGA#10
    host='162.241.230.118',
    user=os.environ['MYSQL_USER'],
    passwd=os.environ['MYSQL_PASSWORD'],
    port=3306,
    db='codetran_collegedata')


class College_Data(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('recipient_email',
                        type=str,
                        required=True,
                        help='email to send attachement to')
    parser.add_argument('filter_dict',
                        type=dict,
                        required=True,
                        help='dictionary with all of filter information')

    def get(self):
        # make a call for one row of data in order to extract column names
        q = 'SELECT * FROM codetran_collegedata.collegescorecard WHERE school_name="Pomona College"'
        column_names = query_to_json(q, sql_connection=conn)['column_names']

        return {
            'class': 'Email_Data',
            'tablename': "codetran_collegedata.collegescorecard",
            'column_names': column_names
        }

    def post(self):
        args = College_Data.parser.parse_args()

        # build query
        tablename = "codetran_collegedata.collegescorecard"
        select_col = ["school_name", "school_state"]
        q = build_query(tablename, select_col, args['filter_dict'])
        return {"table": query_to_json(q, sql_connection=conn)}


class Test(Resource):
    """
    Provides a resource to check whether the basic restful api is working without
    making calls to database and lots of possibilities for problems
    """

    def get(self):
        return {'output': "basic restful api is working"}


api.add_resource(College_Data, '/', '/send-data')
api.add_resource(Test, '/test_api')

if __name__ == '__main__':

    app.run(debug=True)  # TODO: turn debug off
