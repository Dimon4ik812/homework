import unittest
from unittest.mock import mock_open, patch
import json
from src.utils import get_transactions


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

if __name__ == "__main__":
    unittest.main()