import requests
import pandas as pd
url = "https://data.gov.sg/api/action/datastore_search?resource_id=ad854cc4-f9a3-4208-a9e5-cb8d7fb0a76c&q=2019"
result = requests.get(url).json()
# Try out the following codes
# Try to understand the result and figure out how is the data
print(result.keys())
print(result['result'].keys())
print(result['result']['records'])

df = pd.DataFrame(result['result']['records'])
print(df)
