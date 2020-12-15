from flask import Flask
from flask_restful import Resource, reqparse, Api
from flask_cors import CORS
from querybuilder import build_query
from db_interface import query_to_json

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config[
    'PROPAGATE_EXCEPTIONS'] = True  # TODO: figure out if this is what I want


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
        column_names = query_to_json(q)['column_names']

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
        return {"table": query_to_json(q)}


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
