import pytest

from main import transactions
from src.generators import card_number_generator, transaction_descriptions
from src.processing import filtering_words_by_key, sort_descending
from src.widget import data_masking_function, date_decoding


def test_filtering_words_by_key_executed(executed):
    assert (
        filtering_words_by_key(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
        )
        == executed
    )


def test_filtering_words_by_key_canceled(canceled):
    assert (
        filtering_words_by_key(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        )
        == canceled
    )


def test_sort_descending_increase(increase):
    assert (
        sort_descending(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
        )
        == increase
    )


def test_sort_descending_decreasing(decreasing):
    assert (
        sort_descending(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
        )
        == decreasing
    )


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199 "),
        ("Счет 64686473678894779589", "**9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758 "),
        ("Счет 35383033474447895560", "**5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658 "),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229 "),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353 "),
        ("Счет 73654108430135874305", "**4305"),
    ],
)
def test_data_masking_function(value, expected):
    assert data_masking_function(value) == expected


def test_date_decoding(decoding):
    assert date_decoding("2018-07-11T02:26:18.671407") == decoding


def test_card_number_generator():
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"


# def test_transaction_descriptions():
#     generator = transaction_descriptions(transactions)
#     assert next(generator) == "Перевод организации"
#     assert next(generator) == "Перевод со счета на счет"
#     assert next(generator) == "Перевод со счета на счет"
#     assert next(generator) == "Перевод с карты на карту"
#     assert next(generator) == "Перевод организации"
