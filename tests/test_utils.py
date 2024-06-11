import csv
import unittest
from unittest.mock import mock_open, patch
import json
from src.utils import get_transactions
import pandas as pd





class TestGetTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"transaction": "data1"}, {"transaction": "data2"}]')
    def test_get_transactions_valid_file(self, mock_file):
        expected_data = [{"transaction": "data1"}, {"transaction": "data2"}]
        result = get_transactions("fake_path.json")
        self.assertEqual(result, expected_data)
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data='{}')
    def test_get_transactions_invalid_content(self, mock_file):
        result = get_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data='')
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


def test_get_transactions_csv():
    csv_data = "id,amount\n1,100\n2,200\n"
    with (patch("builtins.open", mock_open(read_data=csv_data)), patch("csv.DictReader") as mock_csv_reader,
          patch("../logs/utils") as mock_logger):
        mock_csv_reader.return_value = csv.DictReader(csv_data.splitlines())
        result = get_transactions("data/transactions.csv")
        assert result == [{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}]
        mock_logger.info.assert_called_with("Открываем CSV файл: transactions.csv")




def test_get_transactions_excel():
    excel_data = {"id": [1, 2], "amount": [100, 200]}
    df = pd.DataFrame(excel_data)
    with patch("pandas.read_excel") as mock_read_excel, patch("utils.logger") as mock_logger:
        mock_read_excel.return_value = df
        result = get_transactions("data/transactions.xlsx")
        assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        mock_logger.info.assert_called_with("Открываем Excel файл: transactions.xlsx")


if __name__ == "__main__":
    unittest.main()

def test_get_transactions_json():
    json_data = json.dumps([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    with patch("builtins.open", mock_open(read_data=json_data)), patch("utils.logger") as mock_logger:
        result = get_transactions("transactions.json")
        assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        mock_logger.info.assert_called_with("Открываем JSON файл: transactions.json")

def test_get_transactions_empty_json():
    json_data = json.dumps({})
    with patch("builtins.open", mock_open(read_data=json_data)), patch("utils.logger") as mock_logger:
        result = get_transactions("transactions.json")
        assert result == []
        mock_logger.info.assert_called_with("Открываем JSON файл: transactions.json")

def test_get_transactions_csv():
    csv_data = "id,amount\n1,100\n2,200\n"
    with patch("builtins.open", mock_open(read_data=csv_data)), patch("csv.DictReader") as mock_csv_reader, patch("utils.logger") as mock_logger:
        mock_csv_reader.return_value = csv.DictReader(csv_data.splitlines())
        result = get_transactions("transactions.csv")
        assert result == [{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}]
        mock_logger.info.assert_called_with("Открываем CSV файл: transactions.csv")

def test_get_transactions_excel():
    excel_data = {"id": [1, 2], "amount": [100, 200]}
    df = pd.DataFrame(excel_data)
    with patch("pandas.read_excel") as mock_read_excel, patch("utils.logger") as mock_logger:
        mock_read_excel.return_value = df
        result = get_transactions("transactions.xlsx")
        assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        mock_logger.info.assert_called_with("Открываем Excel файл: transactions.xlsx")

def test_get_transactions_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError), patch("utils.logger") as mock_logger:
        result = get_transactions("transactions.json")
        assert result == []
        mock_logger.error.assert_called_with("Произошла ошибка: ")

def test_get_transactions_unsupported_file():
    with patch("logs/utils.logger") as mock_logger:
        result = get_transactions("transactions.txt")
        assert result == []
        mock_logger.error.assert_called_with("Неподдерживаемый формат файла: transactions.txt")
