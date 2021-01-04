# mysql related imports
from db_interface import establish_connection, create_sql_alchemy_engine
from sqlalchemy import create_engine

# other imports
from api_to_df import main_api_to_df
import sql_info
# TODO: call api_to_df and use it to update the SQL database


def update_db():
    # Get new df from API
    df = main_api_to_df(27)

    # Establish connection with database
    conn = create_sql_alchemy_engine()

    # Write to database
    df.to_sql(con=conn,
              name=sql_info.get_short_table_name(),
              if_exists='replace')  # TODO: fix this


update_db()
