table_name = "codetran_collegedata.collegescorecard"
host = '162.241.230.118'
port = 3306
db_name = 'codetran_collegedata'

select_cols = ["Name", "State"]

where_cols = {
    "Region": [
        'U.S. Service Schools',
        'New England (CT, ME, MA, NH, RI, VT)',
        'Mid East (DE, DC, MD, NJ, NY, PA)',
        'Great Lakes (IL, IN, MI, OH, WI)',
        'Plains (IA, KS, MN, MO, NE, ND, SD)',
        'Southeast (AL, AR, FL, GA, KY, LA, MS, NC, SC, TN, VA, WV)',
        'Southwest (AZ, NM, OK, TX)',
        'Rocky Mountains (CO, ID, MT, UT, WY)',
        'Far West (AK, CA, HI, NV, OR, WA)',
        'Outlying Areas (AS, FM, GU, MH, MP, PR, PW, VI)',
    ],
    "Ownership": [
        'Public',
        'Private nonprofit',
        'Private for-profit',
    ],
    "Highest Degree": [
        'Non-degree-granting',
        'Certificate degree',
        'Associate degree',
        'Bachelors degree',
        'Graduate degree',
    ],
    "Years": [
        '4-year',
        '2-year',
        'Less-than-2-year',
    ],
    "HBCU": [
        'No',
        'Yes',
    ],
    "Single-Sex": [
        "Single-Sex: Men",
        "Single-Sex: Women",
        "Co-Educational",
    ],
    "Midpoint ACT": [0, 36],
    "Size": [0, 50000]
}


def get_table_name():
    return table_name


def get_host():
    return host


def get_port():
    return port


def get_db_name():
    return db_name


def get_where_cols():
    return where_cols


def get_select_cols():
    return select_cols


def get_all_info():
    return {
        "table_name": table_name,
        "where_cols": where_cols,
        "select_cols": select_cols
    }
