import datetime
import requests
import json
import pandas as pd
import sql_info
import os

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def url_end_generator(fields):
    """
    :param fields: a list of strings representing the fields to include when pulling the api
    """
    """
    next few lines create url with correct pagenumbers and fields.
    It also applies various limitations on the data.
    
    Note that ranges are inclusive For example, the range 3..7 matches both 3 and 7, as well as the numbers in between.
    
    school.degrees_awarded.highest=3,4 is a limitation which limits the output to schools whose highest degree awarded 
    is either a bachelors (i.e. Pomona College) or a graduate degree (i.e. Vanderbilt University). Within the API, 
    bachelor's and graduate degrees are represented by 3 and 4, respectively. No degrees granted, certificate degrees, 
    and associate degrees are all excluded and are represented by 0, 1, and 2, respectively 
    """
    limitations = "&school.degrees_awarded.highest=3,4"

    # school.operating=1 is a limitation allowing only schools that are currently operating to be outputed.
    limitations += "&school.operating=1"

    # limitation not allowing schools that have a less than four year completion rate (Not working)
    # limitations += "&latest.completion.completion_rate_less_than_4yr_150nt=None"
    print('\nfields', fields)
    url = limitations + "&_fields="
    for field in fields:
        url += field + ","
    url += "&api_key=IGlx37HV88IkLl14qDgb1siyF2bPjrNZ9DXwFZKQ"
    #url = url.replace('\r','')
    print("end", url)
    return url


def api_to_df(url, object_of_interest):
    """
    Method from https://stackoverflow.com/questions/45787597/parsing-json-data-from-an-api-to-pandas
    :param url: api url
    :param object_of_interest: object that we are interested in. for college data use 'results'
    :return: pandas dataframe for the api
    """
    data = requests.get(url)\
                         .json()[object_of_interest]
    df = pd.DataFrame.from_dict(data)
    return df


def page_flipper(pagenumber, url_start, url_end):
    print("start", url_start)
    url = url_start + str(pagenumber) + url_end
    print("url", url)
    return url


def multi_api_to_df(pages, object_of_interest, url_start, url_end):
    """
    Method from https://stackoverflow.com/questions/45787597/parsing-json-data-from-an-api-to-pandas
    :param url: api url
    :param object_of_interest: object that we are interested in. for college data use 'results'
    :param url: number of pages in the multipage api
    :return: pandas dataframe for the api
    """
    df = api_to_df(page_flipper(0, url_start, url_end), 'results')
    for i in range(1, pages):
        df = pd.concat([
            df,
            api_to_df(page_flipper(i, url_start, url_end), object_of_interest),
        ],
                       sort=True)

    return df


def generate_raw_df(field_list, pgs):
    url_start = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?_per_page=100&page='
    url_end = url_end_generator(field_list)
    object_of_interest = 'results'
    df = multi_api_to_df(pgs, object_of_interest, url_start,
                         url_end)  #there are 27 pages under above limitations
    return df


def organize_columns(df, field_list):
    """
    Notice that when df is generated from api, columns are in the wrong order. 
    We restore the original order of the csv file.
    """
    return df[field_list]


def give_context(d, df):
    """
    Now, we fix columns that use numbers to describe text
    """
    dft = df
    for key in d:
        dft = dft.replace({key: d[key]})

    return dft


def sex_column_helper(dem_float):
    if dem_float == 0:
        return "Single-Sex: Men"
    elif dem_float == 1:
        return "Single-Sex: Women"
    elif dem_float > 0 and dem_float < 1:
        return "Co-Educational"
    else:
        return "Not Listed"


def sex_column(df):
    dft = df
    dft["latest.student.demographics.women"] = dft[
        "latest.student.demographics.women"].apply(sex_column_helper)
    return dft


def main_api_to_df(api_pages=50):
    """
    Main Function to take college scorecard api and convert it to a dataframe to be manipulated
    api_pages tells the function how many pages of colleges there are so that it goes through
    that many pages. Each page has 100 colleges. 
    Going through more pages takes more time (not a problem if run infrequently)
    Going through not enough pages will result in data being missed.
    """

    # Get useful objects
    headers_dict = sql_info.get_headers_dict()
    context_dict = sql_info.get_context_dict()
    field_list = headers_dict.keys()

    # Generate
    df = generate_raw_df(field_list, api_pages)

    # Clean data
    df = organize_columns(df, field_list)
    df = give_context(
        context_dict, df
    )  # note that context_dict will prob come in as json and then need to be converted eventually
    df = sex_column(df)  # creates a column that breaks down single-sex vs coed

    # Replace Header Names
    df.rename(headers_dict, axis=1, inplace=True)

    # return dataframe
    return df
