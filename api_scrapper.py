import requests
import pandas as pd
from datetime import datetime
import os
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
#print upto 2 decimal places
df["price_usd"] = df["price_usd"].round(2)
print(df[["coin_name", "price_usd"]])
# create output directory if not exists
os.makedirs("output", exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"output/crypto_data_{timestamp}.csv"
df.to_csv(file_name, index= False, float_format="%.2f")
print("Data saved successfully", file_name)