import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"

currency_code = [
    "VEF",
    "KZT",
    "JOD",
    "ALL",
    "JPY",
    "HRK",
    "TJS",
    "AMD",
    "XPF",
    "USD",
    "AOA",
    "HTG",
    "ARS",
    "BSD",
    "TZS",
    "CHF",
    "LBP",
    "ZMW",
    "KRW",
    "GMD",
    "XOF",
    "HUF",
    "PLN",
    "CZK",
    "OMR",
    "BAM",
    "GTQ",
    "GYD",
    "CNY",
    "PYG",
    "YER",
    "PKR",
    "HNL",
    "ETB",
    "KGS",
    "PEN",
    "MKD",
    "RSD",
    "IQD",
    "VND",
    "CAD",
    "QAR",
    "MGA",
    "EUR",
    "XAF",
    "XCD",
    "KPW",
    "KES",
    "UAH",
    "SZL",
    "LTL",
    "IDR",
    "BRL",
    "JMD",
    "NGN",
    "CLP",
    "WST",
    "ZWL",
    "CUP",
    "CRC",
    "LKR",
    "NAD",
    "AZN",
    "AFN",
    "MAD",
    "UZS",
    "LAK",
    "CDF",
    "BYR",
    "BOB",
    "NIO",
    "BTN",
    "SYP",
    "MDL",
    "COP",
    "MYR",
    "KHR",
    "MXN",
    "PAB",
    "AUD",
    "UYU",
    "EGP",
    "MMK",
    "BBD",
    "BGN",
    "NOK",
    "ANG",
    "TMT",
    "GHS",
    "ZAR",
    "IRR",
    "TND",
    "DKK",
    "NZD",
    "ILS",
    "DOP",
    "BWP",
    "PHP",
    "UGX",
    "MNT",
    "SEK",
    "SOS",
    "THB",
    "FJD",
]


def convert_to_rub(transaction: dict) -> float:
    """Функция конвертации валюты в рубли"""
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if currency == "RUB":
        return amount
    elif currency in currency_code:
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
