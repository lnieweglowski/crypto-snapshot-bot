
# bot.py
import os
import pandas as pd
import plotly.graph_objs as go
from utils import fetch_market_data
from config import COINS, VS_CURRENCY, DAYS

output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

summary_data = []

for coin_id, symbol in COINS.items():
    df = fetch_market_data(coin_id, VS_CURRENCY, DAYS)

    # Fallback do danych offline, jeśli API zwróci pusty DataFrame
    if df.empty:
        try:
            df = pd.read_csv(f"data/mock_{symbol}.csv", parse_dates=["open_time"])
            print(f"📂 Wczytano dane testowe dla {symbol}")
        except Exception as e:
            print(f"❌ Brak danych testowych dla {symbol}: {e}")
            continue  # pomiń tę walutę

    # ... dopiero tutaj dalsze operacje na df ...
    # np. liczenie zmiany %, wykres, podsumowanie, eksport


    change_pct = ((df["close"].iloc[-1] - df["close"].iloc[0]) / df["close"].iloc[0]) * 100
    summary_data.append({
        "symbol": symbol,
        "start": round(df['close'].iloc[0], 2),
        "end": round(df['close'].iloc[-1], 2),
        "change_pct": round(change_pct, 2),
        "min": round(df["close"].min(), 2),
        "max": round(df["close"].max(), 2),
        "avg": round(df["close"].mean(), 2)
    })


    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["open_time"], y=df["close"], mode="lines", name=symbol))

    fig.update_layout(title=f"Cena {symbol} – ostatnie 24h", xaxis_title="Czas", yaxis_title="Cena (USD)")
    fig.write_html(f"{output_dir}/{symbol}_chart.html")

# Generowanie raportu HTML
with open(f"{output_dir}/raport.html", "w", encoding="utf-8") as f:
    f.write("<html><head><title>Raport Crypto</title></head><body>")
    f.write("<h1>📊 Raport zmian kursów (24h)</h1>")
    f.write("<table border='1' cellspacing='0' cellpadding='5'>")
    f.write("<tr><th>Symbol</th><th>Start</th><th>End</th><th>Zmiana %</th><th>Min</th><th>Max</th><th>Średnia</th></tr>")
    for item in summary_data:
        f.write(f"<tr><td>{item['symbol']}</td><td>{item['start']}</td><td>{item['end']}</td>"
                f"<td>{item['change_pct']}%</td><td>{item['min']}</td><td>{item['max']}</td><td>{item['avg']}</td></tr>")
    f.write("</table><br>")
    for symbol in COINS.values():
        f.write(f"<h2>📈 {symbol}</h2>")
        f.write(f"<iframe src='{symbol}_chart.html' width='100%' height='400'></iframe><br><br>")
    f.write("</body></html>")
