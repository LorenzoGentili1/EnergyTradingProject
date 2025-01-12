from entsoe import EntsoePandasClient
import pandas as pd

# Temporary solution: Store API key directly in the script (for testing only)
api_key = "bc3d1479-15cc-42c6-9687-5c0d59b5f891"
#crete the EntsoePandasClient instance
client = EntsoePandasClient(api_key=api_key)

def fetch_generation_data(country_code:str, start_date:str, end_date:str) -> pd.DataFrame:
    """
    Ferch generation data from the Entsoe API
    Return a DataFram with energy generation data
    """
    start_date= pd.Timestamp(start_date, tz='Europe/Zurich')
    end_date = pd.Timestamp(end_date, tz='Europe/Zurich')

    # Create the EntsoePandasClient instance
    generation_data = client.query_generation(country_code, start=start_date, end=end_date)

    #conver the data to a DataFrame
    generation_df = pd.DataFrame(generation_data)
    #reset the index
    generation_df.reset_index(inplace=True)
    generation_df = generation_df.rename(columns={'index':"timestamp"})
    return generation_df

