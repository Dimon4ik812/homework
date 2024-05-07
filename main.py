from src.processing import filtering_words_by_key, sort_descending

input_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

check_first_func = filtering_words_by_key(input_data)
for i in check_first_func:
    print(i)


check_second_func = sort_descending(input_data)
for i in check_second_func:
    print(i)
