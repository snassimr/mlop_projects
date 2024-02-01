import sys
sys.path.append('app/src/mlops')
from gcp_utils import gcp_csv_to_df

def transform_data(data):
    '''
    function that converts column headers of an
    input df into lower case
    
    Parameters: 
      data (pd.Dataframe): dataset which we want
                to apply basic transformation on
    Returns:      
      pd.DataFrame() : transformed pandas dataframe
    '''
    
    print('Original column list ->',data.columns)
    data.rename(columns = {col:col.lower() for col in data.columns},inplace = True)
    print('Transformed column list ->',data.columns)
    return data

def read_data(input_bucket_name, input_file_name, output_data_path):
    data = gcp_csv_to_df(input_bucket_name, input_file_name)
    data = transform_data(data)
    data.to_csv(output_data_path)