from flask import Flask
from flask_restful import Resource, reqparse, Api
from collegeDataEmail import college_data_email, send_email

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

from base import Movies, db
db.init_app(app)
app.app_context().push()
db.create_all()

class Movies_List(Resource):
    parser = reqparse.RequestParser()
    
    """
    parser.add_argument('min_ACT', type=int, required=False, help='Minimum acceptable ACT Score')
    parser.add_argument('gender_distribution', type=int, required=False, help='Desired gender distribution')
    parser.add_argument('email', type=str, required=True, help='email address of the recipient')
    """
    parser.add_argument('director', type=str, required=False, help='Director of the movie')
    parser.add_argument('genre', type=str, required=False, help='Genre of the movie')
    parser.add_argument('collection', type=int, required=True, help='Gross collection of the movie')
    
    def get(self, movie):
        item = Movies.find_by_title(movie)
        if item:
            return item.json()
        return {'Message': 'Movie is not found'}
    
    def post(self, movie):
        if Movies.find_by_title(movie):
            return {' Message': 'Movie with the  title {} already exists'.format(movie)}
        args = Movies_List.parser.parse_args()
        item = Movies(movie, args['director'], args['genre'], args['collection'])
        item.save_to()
        return item.json()
        
    def put(self, movie):
        args = Movies_List.parser.parse_args()
        item = Movies.find_by_title(movie)
        if item:
            item.collection = args['collection']
            item.save_to()
            return {'Movie': item.json()}
        item = Movies(movie, args['director'], args['genre'], args['collection'])
        item.save_to()
        return item.json()
            
    def delete(self, movie):
        item  = Movies.find_by_title(movie)
        if item:
            item.delete_()
            return {'Message': '{} has been deleted from records'.format(movie)}
        return {'Message': '{} is already not on the list'.format()}


class Email_Data(Resource):
    parser = reqparse.RequestParser()
    
    """
    parser.add_argument('min_ACT', type=int, required=False, help='Minimum acceptable ACT Score')
    parser.add_argument('gender_distribution', type=int, required=False, help='Desired gender distribution')
    parser.add_argument('email', type=str, required=True, help='email address of the recipient')
    """
    #parser.add_argument('director', type=str, required=False, help='Director of the movie')
    parser.add_argument('min_ACT', type=int, required=False, help='Genre of the movie')
    parser.add_argument('recipient_email', type=str, required=True, help='Gross collection of the movie')

     
    def get(self):
        return {'class': 'Email_Data'}


    def post(self):
        args = Email_Data.parser.parse_args()
        
        college_data_email(args['recipient_email'], "personalized.csv", args['min_ACT'])

        return {'output': "sent!"}


class All_Movies(Resource):
    def get(self):
        filename = "schoolNames.csv"
        #cdgmain(filename)
        #send_email("jackdavidweber@gmail.com", filename)
        return {'output': "Nothing for now"}
    
api.add_resource(All_Movies, '/')
api.add_resource(Email_Data, '/send-data')
api.add_resource(Movies_List, '/<string:movie>')

if __name__=='__main__':
    
    app.run(debug=False)
