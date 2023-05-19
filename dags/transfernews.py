


import pandas as pd
import snowflake.connector
import os
from inputoutput import imp_file,getdate
from dotenv import load_dotenv
from snowflake.connector.pandas_tools import write_pandas
load_dotenv()


snowflake_user = os.environ.get('snowflake_user')
snowflake_password = os.environ.get('snowflake_password')
snowflake_account = os.environ.get('snowflake_account')
snowflake_database = os.environ.get('snowflake_database')
snowflake_schema = os.environ.get('snowflake_schema')




# connect to Snowflake and create new table
snowflake_conn = snowflake.connector.connect(
        user=snowflake_user,
        password=snowflake_password,
        account=snowflake_account,
        database=snowflake_database,
        schema=snowflake_schema
)


direc = 'newsgold'
date = getdate()



def perform_data_quality_check(df):
    # Data Completeness Check

    null_values = df.isnull()
    condition1 = null_values.any().any()

    print(condition1)
    duplicate_rows = df.duplicated(subset=['submission'])
    condition2 = duplicate_rows.any()
    print(condition2)

    if condition1:
        print("Warning: Missing values detected!")
    if condition2 :
        duplicate_rows = df.duplicated()
        print(df[duplicate_rows])
        print("Warning: Duplicate records detected!")
        df.drop_duplicates(inplace=True)
        print("Dropped Duplicates")

    if condition1:
        print("Data quality conditions not met. Snowflake table not updated.")
    else:
        #Write DataFrame to Snowflake table
        print(df)
        write_pandas(snowflake_conn,df,"REDDIT",quote_identifiers = False)
        print("Data loaded into Snowflake.")






df = imp_file(direc,date)
df.rename(columns={'date': 'INGESTDATE'}, inplace=True)
print(df)

# Loads if data quality tests are passed


perform_data_quality_check(df)


snowflake_conn.close()
