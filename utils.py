import requests
import pandas as pd

def fetch_market_data(coin_id, vs_currency, days):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
        params = {"vs_currency": vs_currency, "days": days, "interval": "hourly"}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if "prices" in data:
                df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
                df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
                return df
            else:
                print(f"⚠️ Brak 'prices' w odpowiedzi dla {coin_id}")
        else:
            print(f"❌ Błąd API ({response.status_code}) dla {coin_id}")
    except Exception as e:
        print(f"❌ Wyjątek przy {coin_id}: {e}")

    # Zwracamy pusty DataFrame jeśli coś poszło nie tak
    return pd.DataFrame(columns=["timestamp", "price"])
