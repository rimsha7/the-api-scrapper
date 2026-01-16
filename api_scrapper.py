import requests
import pandas as pd
from datetime import datetime
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "ids": "bitcoin, ethereum, cardano"
}
response = requests.get(url,params=params)
data = response.json()
cleaned_data = []
for coin in data:
    cleaned_data.append({
        "coin_name" : coin["name"],
        "price_usd" : coin["current_price"],
        "market_cap_usd" : coin["market_cap"]
    })
df = pd.DataFrame(cleaned_data)
print(df[["coin_name", "price_usd"]])
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"crypto_data_{timestamp}.csv"
df.to_csv(file_name, index= False)
print("Data saved successfully", file_name)