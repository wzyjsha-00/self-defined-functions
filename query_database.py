"""
# Subject: connect and query database
# Author: wzyjsha@gmail.com
# Data: 16/01/2022
# Version: 1.0.0
"""


import pymysql
import pandas as pd


def query_database(database, username, password, hostname, query, port=3306):
    """
    Input: database, username, passward, hostname: str
    Output: pd.Dataframe with display all columns

    """

    conn = pymysql.connect(db=database, user=username, password=password, host=hostname, port=port)
    cur = conn.cursor(pymysql.cursors.DictCursor) # return query containing fields
    cur.execute(query)
    query_result = pd.DataFrame(cur.fetchall())
    
    pd.set_option('display.max_columns', None)  # set to display all columns
    
    return query_result
