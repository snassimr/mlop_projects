def get_data_description(data):
    '''
    function that displays basic stats of an
    input pandas df
    
    Parameters: 
      data (pd.Dataframe): dataset which we want
                to apply basic transformation on
    Returns:      
      None
    '''
    
    print('Dataset stats ->',data.describe())
    return None

def display_stats(input_file_path):
    
    import pandas as pd

    data = pd.read_csv(input_file_path)
    get_data_description(data)

