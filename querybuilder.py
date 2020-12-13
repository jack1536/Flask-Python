"""
{"filter_dict":
    {"is_in":{"school.region_id":["Mid East (DE, DC, MD, NJ, NY, PA)"]},
    "is_btwn":{
        "latest.admissions.act_scores.midpoint.cumulative":{"min":0,"max":36,"inclusive":true},
        "latest.student.size":{"min":0,"max":50000,"inclusive":true}
    }
},
"recipient_email":"jackdavidweber@gmail.com"}

SELECT school_name, latest_admissions_act_scores_midpoint_cumulative, latest_student_size, school_region_id
FROM codetran_collegedata.collegescorecard
WHERE latest_admissions_act_scores_midpoint_cumulative BETWEEN 28 AND 34
AND latest_student_size BETWEEN 0 AND 23000
AND school_region_id IN ("Mid East (DE, DC, MD, NJ, NY, PA)")
;
"""

def build_query(tablename, select_cols, filter_dict):
    # SELECT
    select_cols = ", ".join(select_cols)  # join list items with commas between
    select_cols = select_cols.replace(".", "_")  # replace . in column names with _
    select_str =  "SELECT " + select_cols

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
        condition = col + " BETWEEN " + str(lower) + " AND " + str(upper)
        where_list.append(condition)
    
    # WHERE IN
    in_dict = filter_dict["is_in"]
    for k in in_dict.keys():
        col = k.replace(".", "_")
        options = in_dict[k]  # list of options that row value must be in
        options = '"' + '", "'.join(options) + '"' #  make options into string (SQL format)
        condition = col +  " IN (" + options + ")"
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





    




    








class QueryBuilder:
    def __init__(self, tablename):
        self.tablename = tablename
        self.btwn_conditions = {}
        self.in_conditions = {}

    def add_btwn_condition(self, col, min, max, inclusive):
        # replace . in col with _
        col = col.replace(".", "_")

        # add into table
        self.btwn_conditions[col] = {min, max, inclusive}
    
    


# qb = QueryBuilder("james_table")
# qb.add_btwn_condition("hello.world", 1, 1, 1)
    