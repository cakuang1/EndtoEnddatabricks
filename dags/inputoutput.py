import boto3
import pandas as pd
from datetime import datetime, timedelta
import typing
import os
from dotenv import load_dotenv
load_dotenv()



## Helpeer file for everything IO related (S3 data retrieval,snowflake import)

bucketname = os.environ.get('BUCKET_NAME')

pathprefix = 's3://' + bucketname

def imp_file(directory,filename):
    """    
    Imports CSV file from S3 into a pandas dataframe


    Arguments : 
        bucketname (str) : The bucket name
        filename (str): The filename
        directory(str): There directory where the file is located   

    Returns : 
        pd.Dataframe: Dataframe from the 
    """
    path = pathprefix +  '/' + directory + '/' + filename + '.csv'

    df = pd.read_csv(path)

    return df




def save_file(directory,filename,df):
    """        
    Saves pandas data frame into


    Arguments : 
        bucketname (str) : The bucket name
        directory(str): There directory where the file is located   
        filename (str): The filename

    Returns : 
        None
    """

    path = pathprefix +  '/' + directory + '/' + filename + '.csv'
    df.to_csv(path,index=False)
    return None


def listfiles(directory):
    """
    Given some prefix after the bucket name, list all files in that directory

    Args:
        prefix (str): folder or directory to search, relative to the bucket name.
    Returns:
        List[str]: list of strings corresponding to the immediate files in the directory specified.
    """
    s3 = boto3.resource('s3')

    prefix = directory
    bucket = s3.Bucket(bucket_name)
    holder = []
    for obj in bucket.objects.filter(Prefix=prefix):
        holder.append(obj.key)
    return holder

def getdate():

    """
    
    Gives the current date in string form
    
    
    """
    today = datetime.now().date()
    # Subtract one day to get the date before today
    yesterday = today - timedelta(days=1)
    dateparameter = yesterday.strftime('%Y-%m-%d')

    return dateparameter




