
import boto3
import pandas as pd
import snowflake.connector
import os
from inputoutput import imp_file,getdate
from dotenv import load_dotenv
load_dotenv()




snowflake_user = os.environ.get('snowflake_user')
snowflake_password = os.environ.get('snowflake_password')
snowflake_account = os.environ.get('snowflake_account')
snowflake_database = os.environ.get('ddtosfpipeline')
snowflake_schema = os.environ.get('snowflake_schema')


# connect to Snowflake and create new table
snowflake_conn = snowflake.connector.connect(
        user=snowflake_user,
        password=snowflake_password,
        account=snowflake_account,
        database=snowflake_database,
        schema=snowflake_schema
)



direc = 'redditgold'
date = getdate()


def perform_data_quality_check(df):
    # Data Completeness Check

    missing_values = df.isnull().sum()
    condition1 = missing_values > 0
    duplicate_rows = df.duplicated()
    condtion2 = 




    if missing_values.sum() > 0:
        print("Warning: Missing values detected!")
        print(missing_values)
    duplicate_rows = df.duplicated()
    if duplicate_rows.any():
        print("Warning: Duplicate records detected!")
        print(df[duplicate_rows])
    
    if condition1 and condition2:
        # Write DataFrame to Snowflake table
        df.to_sql(table_name, conn, schema='<your_schema>', if_exists='append', index=False)
        print("Data loaded into Snowflake.")
    else:
        print("Data quality conditions not met. Snowflake table not updated.")






df = imp_file(direc,date)




# Remove missing values




# load data into Snowflake table using pandas DataFrame
df.to_sql("REDDIT", snowflake_conn, schema=snowflake_schema, if_exists='append', index=False)









# close Snowflake connection






snowflake_conn.close()








filename = str(sys.argv[1])


def main():

    )