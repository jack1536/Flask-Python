# mysql related imports
from db_interface import establish_connection, create_sql_alchemy_engine
from sqlalchemy import create_engine

# other imports
from step_1_folder.step_1 import step_1_main
import pandas
import urllib.parse
# TODO: call step_1_main and use it to update the SQL database

def generate_engine():
    username = urllib.parse.quote_plus()


def update_db():
    # Get new df from API
    df = step_1_main(1,"simple_raw_data.csv")

    # Establish connection with database
    conn = create_sql_alchemy_engine()

    # Write to database
    df.to_sql(con=conn, name='collegeData', if_exists='replace') # TODO: fix this

update_db()