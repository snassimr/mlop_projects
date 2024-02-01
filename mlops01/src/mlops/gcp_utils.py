import pandas as pd
from google.cloud import storage
import os
import io

def gcp_csv_to_df(bucket_name, file_name):
    '''
    function that downloads a csv file located in
    a GCS bucket into the local instance
   
    Parameters: 
      bucket_name (str): name of the GCS bucket
                         that contains the data
      file_name (str): file path of the 
                         csv data           
    Returns:      
      pd.DataFrame() : data loaded in a pandas df
    '''
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    data = blob.download_as_string()
    df = pd.read_csv(io.BytesIO(data))
    print(f'Pulled down file from bucket {bucket_name}, file name: {file_name}')
    return df