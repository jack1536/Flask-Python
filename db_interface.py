def execute_query(q, sql_connection):
    sql_connection.query(q)
    result = sql_connection.store_result()

    return result


def query_to_json(q, sql_connection):
    result = execute_query(q, sql_connection)
    first_row = result.fetch_row(how=1)

    # if query doesn't return anything, return object with empty lists
    if len(first_row) == 0:
        return {"column_names": [], "rows": []}

    # column names are grabbed from first row
    out = {
        "column_names": list(first_row[0].keys()),
        "rows": [tuple(first_row[0].values())]
    }

    # add the rest of the rows to data
    l = result.fetch_row(maxrows=0, how=0)
    out["rows"].extend(l)

    return out
