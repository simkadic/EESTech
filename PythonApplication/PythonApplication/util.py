import calendar


def transform_date(dict_value):
    if isinstance(dict_value, str) and len(dict_value.strip()) == 4:
        return [1, 1, int(dict_value)]
    else:
        split_string = dict_value.strip().split(' ')
        month_abbr = split_string[1]
        month_abbr = list(calendar.month_abbr).index(month_abbr)
        split_string[1] = month_abbr
        split_string[0] = int(split_string[0])
        split_string[2] = int(split_string[2])
        print(split_string)
        return split_string
