from dotenv import load_dotenv
load_dotenv()  # loads in .env variables
import os

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
table_name = "codetran_collegedata.collegeData"
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

headers_dict = {
    "ope6_id":
        "ope6_id",
    "school.name":
        "Name",
    "school.state":
        "State",
    "school.zip":
        "Zip",
    "school.ownership":
        "Ownership",
    "school.region_id":
        "Region",
    "school.price_calculator_url":
        "price_calculator_url",
    "school.institutional_characteristics.level":
        "Years",
    "school.degrees_awarded.predominant":
        "school.degrees_awarded.predominant",
    "school.degrees_awarded.highest":
        "Highest Degree",
    "school.carnegie_basic":
        "school.carnegie_basic",
    "school.carnegie_undergrad":
        "school.carnegie_undergrad",
    "school.carnegie_size_setting":
        "school.carnegie_size_setting",
    "school.degree_urbanization":
        "school.degree_urbanization",
    "latest.student.size":
        "Size",
    "school.online_only":
        "school.online_only",
    "school.minority_serving.historically_black":
        "HBCU",
    "school.religious_affiliation":
        "school.religious_affiliation",
    "school.online_only":
        "school.online_only",
    "latest.student.part_time_share":
        "latest.student.part_time_share",
    "latest.student.grad_students":
        "latest.student.grad_students",
    "latest.student.demographics.women":
        "Single-Sex",
    "latest.completion.completion_rate_4yr_100nt":
        "latest.completion.completion_rate_4yr_100nt",
    "latest.completion.completion_rate_4yr_150nt":
        "latest.completion.completion_rate_4yr_150nt",
    "latest.admissions.admission_rate.overall":
        "latest.admissions.admission_rate.overall",
    "latest.admissions.sat_scores.25th_percentile.critical_reading":
        "latest.admissions.sat_scores.25th_percentile.critical_reading",
    "latest.admissions.sat_scores.75th_percentile.critical_reading":
        "latest.admissions.sat_scores.75th_percentile.critical_reading",
    "latest.admissions.sat_scores.25th_percentile.math":
        "latest.admissions.sat_scores.25th_percentile.math",
    "latest.admissions.sat_scores.75th_percentile.math":
        "latest.admissions.sat_scores.75th_percentile.math",
    "latest.admissions.sat_scores.average.overall":
        "latest.admissions.sat_scores.average.overall",
    "latest.admissions.act_scores.25th_percentile.cumulative":
        "latest.admissions.act_scores.25th_percentile.cumulative",
    "latest.admissions.act_scores.75th_percentile.cumulative":
        "latest.admissions.act_scores.75th_percentile.cumulative",
    "latest.admissions.act_scores.midpoint.cumulative":
        "Midpoint ACT",
    "latest.cost.tuition.in_state":
        "latest.cost.tuition.in_state",
    "latest.cost.tuition.out_of_state":
        "latest.cost.tuition.out_of_state",
    "latest.aid.pell_grant_rate":
        "latest.aid.pell_grant_rate",
    "latest.cost.net_price.public.by_income_level.0-30000":
        "latest.cost.net_price.public.by_income_level.0-30000",
    "latest.cost.net_price.private.by_income_level.0-30000":
        "latest.cost.net_price.private.by_income_level.0-30000",
    "latest.cost.net_price.public.by_income_level.30001-48000":
        "latest.cost.net_price.public.by_income_level.30001-48000",
    "latest.cost.net_price.private.by_income_level.30001-48000":
        "latest.cost.net_price.private.by_income_level.30001-48000",
    "latest.cost.net_price.public.by_income_level.48001-75000":
        "latest.cost.net_price.public.by_income_level.48001-75000",
    "latest.cost.net_price.private.by_income_level.48001-75000":
        "latest.cost.net_price.private.by_income_level.48001-75000",
    "latest.cost.net_price.public.by_income_level.75001-110000":
        "latest.cost.net_price.public.by_income_level.75001-110000",
    "latest.cost.net_price.private.by_income_level.75001-110000":
        "latest.cost.net_price.private.by_income_level.75001-110000",
    "latest.cost.net_price.public.by_income_level.110001-plus":
        "latest.cost.net_price.public.by_income_level.110001-plus",
    "latest.cost.net_price.private.by_income_level.110001-plus":
        "latest.cost.net_price.private.by_income_level.110001-plus",
    "school.operating":
        "school.operating",
}

context_dict = {
    "school.carnegie_basic": {
        -2:
            'Not applicable',
        0:
            '(Not classified)',
        1:
            'Associates Colleges: High Transfer-High Traditional',
        2:
            'Associates Colleges: High Transfer-Mixed Traditional/Nontraditional',
        3:
            'Associates Colleges: High Transfer-High Nontraditional',
        4:
            'Associates Colleges: Mixed Transfer/Vocational & Technical-High Traditional',
        5:
            'Associates Colleges: Mixed Transfer/Vocational & Technical-Mixed Traditional/Nontraditional',
        6:
            'Associates Colleges: Mixed Transfer/Vocational & Technical-High Nontraditional',
        7:
            'Associates Colleges: High Vocational & Technical-High Traditional',
        8:
            'Associates Colleges: High Vocational & Technical-Mixed Traditional/Nontraditional',
        9:
            'Associates Colleges: High Vocational & Technical-High Nontraditional',
        10:
            'Special Focus Two-Year: Health Professions',
        11:
            'Special Focus Two-Year: Technical Professions',
        12:
            'Special Focus Two-Year: Arts & Design',
        13:
            'Special Focus Two-Year: Other Fields',
        14:
            'Baccalaureate/Associates Colleges: Associates Dominant',
        15:
            'Doctoral Universities: Highest Research Activity',
        16:
            'Doctoral Universities: Higher Research Activity',
        17:
            'Doctoral Universities: Moderate Research Activity',
        18:
            'Masters Colleges & Universities: Larger Programs',
        19:
            'Masters Colleges & Universities: Medium Programs',
        20:
            'Masters Colleges & Universities: Small Programs',
        21:
            'Baccalaureate Colleges: Arts & Sciences Focus',
        22:
            'Baccalaureate Colleges: Diverse Fields',
        23:
            'Baccalaureate/Associates Colleges: Mixed Baccalaureate/Associates',
        24:
            'Special Focus Four-Year: Faith-Related Institutions',
        25:
            'Special Focus Four-Year: Medical Schools & Centers',
        26:
            'Special Focus Four-Year: Other Health Professions Schools',
        27:
            'Special Focus Four-Year: Engineering Schools',
        28:
            'Special Focus Four-Year: Other Technology-Related Schools',
        29:
            'Special Focus Four-Year: Business & Management Schools',
        30:
            'Special Focus Four-Year: Arts, Music & Design Schools',
        31:
            'Special Focus Four-Year: Law Schools',
        32:
            'Special Focus Four-Year: Other Special Focus Institutions',
        33:
            'Tribal Colleges',
    },
    'school.carnegie_undergrad': {
        -2: 'Not applicable',
        0: 'Not classified (Exclusively Graduate)',
        1: 'Two-year, higher part-time',
        2: 'Two-year, mixed part/full-time',
        3: 'Two-year, medium full-time',
        4: 'Two-year, higher full-time',
        5: 'Four-year, higher part-time',
        6: 'Four-year, medium full-time, inclusive, lower transfer-in',
        7: 'Four-year, medium full-time, inclusive, higher transfer-in',
        8: 'Four-year, medium full-time, selective, lower transfer-in',
        9: 'Four-year, medium full-time , selective, higher transfer-in',
        10: 'Four-year, full-time, inclusive, lower transfer-in',
        11: 'Four-year, full-time, inclusive, higher transfer-in',
        12: 'Four-year, full-time, selective, lower transfer-in',
        13: 'Four-year, full-time, selective, higher transfer-in',
        14: 'Four-year, full-time, more selective, lower transfer-in',
        15: 'Four-year, full-time, more selective, higher transfer-in',
    },
    'school.carnegie_size_setting': {
        -2: 'Not applicable',
        0: '(Not classified)',
        1: 'Two-year, very small',
        2: 'Two-year, small',
        3: 'Two-year, medium',
        4: 'Two-year, large',
        5: 'Two-year, very large',
        6: 'Four-year, very small, primarily nonresidential',
        7: 'Four-year, very small, primarily residential',
        8: 'Four-year, very small, highly residential',
        9: 'Four-year, small, primarily nonresidential',
        10: 'Four-year, small, primarily residential',
        11: 'Four-year, small, highly residential',
        12: 'Four-year, medium, primarily nonresidential',
        13: 'Four-year, medium, primarily residential',
        14: 'Four-year, medium, highly residential',
        15: 'Four-year, large, primarily nonresidential',
        16: 'Four-year, large, primarily residential',
        17: 'Four-year, large, highly residential',
        18: 'Exclusively graduate/professional',
    },
    "school.region_id": {
        0: 'U.S. Service Schools',
        1: 'New England (CT, ME, MA, NH, RI, VT)',
        2: 'Mid East (DE, DC, MD, NJ, NY, PA)',
        3: 'Great Lakes (IL, IN, MI, OH, WI)',
        4: 'Plains (IA, KS, MN, MO, NE, ND, SD)',
        5: 'Southeast (AL, AR, FL, GA, KY, LA, MS, NC, SC, TN, VA, WV)',
        6: 'Southwest (AZ, NM, OK, TX)',
        7: 'Rocky Mountains (CO, ID, MT, UT, WY)',
        8: 'Far West (AK, CA, HI, NV, OR, WA)',
        9: 'Outlying Areas (AS, FM, GU, MH, MP, PR, PW, VI)',
    },
    "school.religious_affiliation": {
        -2: 'Not applicable',
        22: 'American Evangelical Lutheran Church',
        24: 'African Methodist Episcopal Zion Church',
        27: 'Assemblies of God Church',
        28: 'Brethren Church',
        30: 'Roman Catholic',
        33: 'Wisconsin Evangelical Lutheran Synod',
        34: 'Christ and Missionary Alliance Church',
        35: 'Christian Reformed Church',
        36: 'Evangelical Congregational Church',
        37: 'Evangelical Covenant Church of America',
        38: 'Evangelical Free Church of America',
        39: 'Evangelical Lutheran Church',
        40: 'International United Pentecostal Church',
        41: 'Free Will Baptist Church',
        42: 'Interdenominational',
        43: 'Mennonite Brethren Church',
        44: 'Moravian Church',
        45: 'North American Baptist',
        47: 'Pentecostal Holiness Church',
        48: 'Christian Churches and Churches of Christ',
        49: 'Reformed Church in America',
        50: 'Episcopal Church, Reformed',
        51: 'African Methodist Episcopal',
        52: 'American Baptist',
        53: 'American Lutheran',
        54: 'Baptist',
        55: 'Christian Methodist Episcopal',
        57: 'Church of God',
        58: 'Church of Brethren',
        59: 'Church of the Nazarene',
        60: 'Cumberland Presbyterian',
        61: 'Christian Church (Disciples of Christ)',
        64: 'Free Methodist',
        65: 'Friends',
        66: 'Presbyterian Church (USA)',
        67: 'Lutheran Church in America',
        68: 'Lutheran Church - Missouri Synod',
        69: 'Mennonite Church',
        71: 'United Methodist',
        73: 'Protestant Episcopal',
        74: 'Churches of Christ',
        75: 'Southern Baptist',
        76: 'United Church of Christ',
        77: 'Protestant, not specified',
        78: 'Multiple Protestant Denomination',
        79: 'Other Protestant',
        80: 'Jewish',
        81: 'Reformed Presbyterian Church',
        84: 'United Brethren Church',
        87: 'Missionary Church Inc',
        88: 'Undenominational',
        89: 'Wesleyan',
        91: 'Greek Orthodox',
        92: 'Russian Orthodox',
        93: 'Unitarian Universalist',
        94: 'Latter Day Saints (Mormon Church)',
        95: 'Seventh Day Adventists',
        97: 'The Presbyterian Church in America',
        99: 'Other (none of the above)',
        100: 'Original Free Will Baptist',
        101: 'Ecumenical Christian',
        102: 'Evangelical Christian',
        103: 'Presbyterian',
        105: 'General Baptist',
        106: 'Muslim',
        107: 'Plymouth Brethren',
    },
    "school.ownership": {
        1: 'Public',
        2: 'Private nonprofit',
        3: 'Private for-profit',
    },
    "school.operating": {
        0: 'Not currently certified as an operating institution',
        1: 'Currently certified as operating',
    },
    "school.online_only": {
        0: 'Not distance-education only',
        1: 'Distance-education only',
    },
    "school.minority_serving.historically_black": {
        0: 'No',
        1: 'Yes',
    },
    "school.degrees_awarded.predominant": {
        0: 'Not classified',
        1: 'Predominantly certificate-degree granting',
        2: 'Predominantly associates-degree granting',
        3: 'Predominantly bachelors-degree granting',
        4: 'Entirely graduate-degree granting',
    },
    "school.degrees_awarded.highest": {
        0: 'Non-degree-granting',
        1: 'Certificate degree',
        2: 'Associate degree',
        3: 'Bachelors degree',
        4: 'Graduate degree',
    },
    "school.institutional_characteristics.level": {
        1: '4-year',
        2: '2-year',
        3: 'Less-than-2-year',
    },
}


def get_user():
    return user


def get_password():
    return password


def get_table_name():
    return table_name


def get_host():
    return host


def get_port():
    return port


def get_db_name():
    return db_name


def get_where_cols():
    # TODO: combine with select_cols, headers_dict, context_dict (SEE Ticket#25)
    return where_cols


def get_select_cols():
    return select_cols


def get_headers_dict():
    return headers_dict


def get_context_dict():
    return context_dict


def get_all_info():
    return {
        "table_name": table_name,
        "where_cols": where_cols,
        "select_cols": select_cols
    }
