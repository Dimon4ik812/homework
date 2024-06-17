import os
import unittest
from unittest.mock import Mock, patch

import requests
from dotenv import load_dotenv

from src.external_api import convert_to_rub

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


class TestConvertToRub(unittest.TestCase):

    @patch("requests.get")
    def test_convert_usd_to_rub(self, mock_get):
        mock_get.return_value.json.return_value = {"result": 75.0}
        mock_get.return_value.status_code = 200

        transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}

        result = convert_to_rub(transaction)
        self.assertEqual(result, 75.0)
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1", headers={"apikey": API_KEY}
        )

    @patch("requests.get")
    def test_convert_eur_to_rub(self, mock_get):
        mock_get.return_value.json.return_value = {"result": 85.0}
        mock_get.return_value.status_code = 200

        transaction = {"operationAmount": {"amount": 1, "currency": {"code": "EUR"}}}

        result = convert_to_rub(transaction)
        self.assertEqual(result, 85.0)
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=1", headers={"apikey": API_KEY}
        )

    def test_convert_rub_to_rub(self):
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}

        result = convert_to_rub(transaction)
        self.assertEqual(result, 100)

    def test_convert_other_currency_to_rub(self):
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "GBP"}}}

        result = convert_to_rub(transaction)
        self.assertEqual(result, 0.0)

    @patch("requests.get")
    def test_api_failure(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.RequestException(response=mock_response)
        mock_get.return_value = mock_response

        transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}

        result = convert_to_rub(transaction)
        self.assertEqual(result, 0.0)


if __name__ == "__main__":
    unittest.main()
