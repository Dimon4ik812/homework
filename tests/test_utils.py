import json
import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.logger import setup_logging
from src.utils import get_transactions

logger_1 = setup_logging("masks", "logs/masks.log")
logger = setup_logging("utils", "logs/utils.log")


class TestGetTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"transaction": "data1"}, {"transaction": "data2"}]')
    def test_get_transactions_valid_file(self, mock_file):
        expected_data = [{"transaction": "data1"}, {"transaction": "data2"}]
        result = get_transactions("fake_path.json")
        self.assertEqual(result, expected_data)
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_get_transactions_invalid_content(self, mock_file):
        result = get_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_get_transactions_empty_file(self, mock_file):
        result = get_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_transactions_file_not_found(self, mock_file):
        result = get_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data='{"transaction": "data"}')
    @patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
    def test_get_transactions_json_decode_error(self, mock_json_load, mock_file):
        result = get_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")
        mock_json_load.assert_called_once()

    @patch("builtins.open", mock_open(read_data="id,amount\n1,100\n2,200"))
    @patch("csv.DictReader")
    @patch("src.utils.logger")
    def test_get_transactions_csv(self, mock_logger, mock_csv_reader):
        mock_csv_reader.return_value = [{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}]
        result = get_transactions("data/transactions.csv")
        self.assertEqual(result, [{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}])
        mock_logger.info.assert_called_with("открываем csv файл *")

    @patch("pandas.read_excel")
    @patch("src.utils.logger")
    def test_get_transactions_excel(self, mock_logger, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame({"id": [1, 2], "amount": [100, 200]})
        result = get_transactions("data/transactions.xlsx")
        self.assertEqual(result, [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
        mock_logger.info.assert_called_with("открываем excel файл *")
