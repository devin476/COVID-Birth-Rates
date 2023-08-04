import pandas as pd

#Loops through USA States on Google open Data by location key
#Prints error and error code if iteration is failed
def googleDataCall():
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    googleData = pd.DataFrame()

    for state in states:
        try:
            url = f"https://storage.googleapis.com/covid19-open-data/v3/location/US_{state}.csv"
            state_data = pd.read_csv(url)
            googleData = googleData.append(state_data)
        except Exception as e:
            print(f"Failed to download data for state: {state}. Error: {e}")
    googleData.reset_index(drop=True, inplace=True)
    return(googleData)