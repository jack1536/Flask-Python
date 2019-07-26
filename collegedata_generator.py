import requests
import json
import pandas as pd
"""
https://github.com/18F/open-data-maker/blob/api-docs/API.md
"""

def process(filename):
    """
    Takes csv file, opens it and creates a list of lists (lol).
    :param filename: string representing the name of the file needed to be processes
    :return: a list of lists (lol) where each nested list represents a row from the dataset.
    """
    file_in = open(filename, "r")
    lol = []
    for line in file_in:
        line = line[:-1]
        lol.append(line.split(","))

    return lol

def column_to_list(lol, index):
    """
    Converts a column within a list of lists to a list
    :param lol: list of list returned from process
    :param index: index of the column that should be turned into a list
    :return: a list containing the values of each row at the given index
    """
    nl = []
    for l in lol:
        # in the csv i had to replace "," with "|". This switches it back.
        temp = l[index].replace("|",",")
        nl.append(temp)
    return nl[1:]  # excludes header for the column

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
    """
    if(len(minACT)!=0):
        limitations += "&latest.admissions.act_scores.midpoint.cumulative__range=" + minACT + ".."

    if (len(genderDist)>0): 
        if (genderDist == "1"):
            limitations += "&latest.student.demographics.women__range=0..1"
        elif (genderDist == "2"):
            limitations += "&latest.student.demographics.women=1"
        elif (genderDist == "3"):
            limitations += "&latest.student.demographics.men=1"
    #Note that ranges are inclusive
    
    
    if(len(schoolSize)>0):
        if(schoolSize == "1"):
            limitations += "&latest.student.size__range=..5000"
        if(schoolSize == "2"):
            limitations += "&latest.student.size__range=5001..9999"
        if(schoolSize == "3"):
            limitations += "&latest.student.size__range=10000.."
    """

    


    url = limitations + "&_fields="
    for field in fields:
        url += field + ","
    url += "&api_key=IGlx37HV88IkLl14qDgb1siyF2bPjrNZ9DXwFZKQ"
    
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
    url = url_start + str(pagenumber) + url_end
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
    for i in range(1,pages):
        df = pd.concat([df, api_to_df(page_flipper(i, url_start, url_end), object_of_interest)])
    
    return df


def cdgmain():
    field_list = column_to_list(process("useful_fields.csv"), 3)
    url_start = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?_per_page=100&page='
    url_end = url_end_generator(field_list)
    object_of_interest= 'results'
    df = multi_api_to_df(3, object_of_interest, url_start, url_end)
    final_csv = df.to_csv(sep=',', encoding='utf-8')
    #print(final_csv)
    return final_csv

"""if __name__=='__main__':
    cdgmain()"""