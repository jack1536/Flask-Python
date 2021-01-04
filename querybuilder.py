"""
Program to convert from JSON that is outputted by collegespreadsheets frontent to SQL query
that can be processed by database.
Below is an example for illustration purposes:

JSON from frontend:
{"filter_dict":
    {"is_in":{"school.region_id":["Mid East (DE, DC, MD, NJ, NY, PA)"]},
    "is_btwn":{
        "latest.admissions.act_scores.midpoint.cumulative":{"min":0,"max":36,"inclusive":true},
        "latest.student.size":{"min":0,"max":50000,"inclusive":true}
    }
},
"recipient_email":"jackdavidweber@gmail.com"}

Expected SQL Query from querybuilder:
SELECT school_name, latest_admissions_act_scores_midpoint_cumulative, latest_student_size, school_region_id
FROM codetran_collegedata.collegescorecard
WHERE latest_admissions_act_scores_midpoint_cumulative BETWEEN 28 AND 34
AND latest_student_size BETWEEN 0 AND 23000
AND school_region_id IN ("Mid East (DE, DC, MD, NJ, NY, PA)")
;
"""


def build_query(tablename, select_cols, filter_dict):
    # SELECT
    select_cols = "`, `".join(select_cols)  # join list items with commas between
    select_cols = select_cols.replace(".",
                                      "_")  # replace . in column names with _
    select_str = "SELECT `" + select_cols + "`"

    # FROM
    from_str = "FROM " + tablename

    # WHERE
    where_list = []

    # WHERE BTWN
    btwn_dict = filter_dict["is_btwn"]
    for k in btwn_dict.keys():
        col = k.replace(".", "_")
        lower = btwn_dict[k]['min']
        upper = btwn_dict[k]['max']
        condition = "`" + col + "`" + " BETWEEN " + str(lower) + " AND " + str(
            upper)
        where_list.append(condition)

    # WHERE IN
    in_dict = filter_dict["is_in"]
    for k in in_dict.keys():
        options = in_dict[k]  # list of options that row value must be in
        if len(options) > 0:
            col = k.replace(".", "_")
            options = '"' + '", "'.join(
                options) + '"'  #  make options into string (SQL format)
            condition = "`" + col + "`" + " IN (" + options + ")"
            print("condition")
            print(condition)
            where_list.append(condition)

    # Put everything together
    query = select_str + " " + from_str

    # if no conditions, return query without WHERE
    if len(where_list) == 0:
        return query

    query = query + " WHERE " + where_list[0]  # add first condition to query
    for i in range(1, len(where_list)):
        query = query + " AND " + where_list[i]

    return query
