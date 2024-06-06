import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"


def convert_to_rub(transaction: dict) -> float:
    """Функция конвертации валюты в рубли"""
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if currency == "RUB":
        return amount
    elif currency == "USD" or currency == "EUR":
        try:
            response = requests.get(
                API_URL.format(to="RUB", from_=currency, amount=amount), headers={"apikey": API_KEY}
            )
            response.raise_for_status()
            data = response.json()
            return data["result"]
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при конвертации валюты: {e.response.status_code}")
            return 0.0
    else:
        return 0.0
