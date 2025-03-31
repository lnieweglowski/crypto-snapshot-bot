
# 🤖 Smart Crypto Snapshot Bot

Automatyczny bot do pobierania kursów kryptowalut (BTC, ETH, DOT) i generowania interaktywnego raportu HTML z wykresami i analizą zmian w ciągu ostatnich 24h.

---

## 🔧 Co potrafi

✅ Pobiera dane z Binance (lub offline z plików CSV)  
✅ Liczy zmianę % kursu, min, max, średnią  
✅ Tworzy wykresy świecowe w Plotly  
✅ Generuje raport HTML z wykresami i tabelą  
✅ Gotowy do rozbudowy (alerty, e-mail, Telegram, dashboard)

---

## 📊 Demo raportu

📄 Przykład gotowego raportu: [`raport.html`](outputs/raport.html)  
💡 Wersja działa również offline – idealna do demo lub rozwoju.

---

## 🚀 Jak uruchomić

1. Zainstaluj wymagane biblioteki:
```bash
pip install pandas plotly requests
```

2. Uruchom bota:
```bash
python bot.py
```

3. Sprawdź katalog `outputs/` – znajdziesz tam `raport.html` oraz wykresy.

---

## 📁 Struktura projektu

```
crypto-snapshot-bot/
├── bot.py              # Główny skrypt
├── config.py           # Lista walut, ustawienia
├── utils.py            # Funkcje pomocnicze
├── data/               # Mock dane offline (CSV)
├── outputs/            # Raporty i wykresy
```

---

## 📬 Kontakt

Masz dane, które warto automatyzować?  
Chcesz własny bot lub raport?

📩 lukasznieweglowski7@gmail.com
