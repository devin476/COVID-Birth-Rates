import pandas as pd
from concurrent.futures import ThreadPoolExecutor

#Loops through USA States on Google open Data by location key and downloads data concurrently 
#Prints error and error code if iteration is failed
def googleDataCall(state):
    try:
        url = f"https://storage.googleapis.com/covid19-open-data/v3/location/US_{state}.csv"
        state_data = pd.read_csv(url)
        return state_data
    except Exception as e:
        print(f"Failed to download data for state: {state}. Error: {e}")
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
with ThreadPoolExecutor() as executor:
    googleDl = list(executor.map(googleDataCall, states))
googleData = pd.concat(googleDl, ignore_index=True)
print(googleData)

