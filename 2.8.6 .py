from typing import Tuple

def parse_args() -> Tuple[list[int], list[int] | None]:
    """
    Get input values from user, add them into rps_values list
    :return: new_values, delimiters
    """
    new_value = None  # keeps new values to define condition

    new_values: list[int] = []

    delimiters = None  # keeps values as list

    # check conditions
    while new_value != ' ' and new_value != '[':
        new_value = input("enter value:")
        if new_value == ' ':  # break input
            break
        if ';' in new_value:  # a;b;c
            new_values += list(map(int, new_value.split(';')))
            continue
        if '[' in new_value:  # [a, b]
            delimiters = list(map(int, new_value.strip('][').split(', ')))
            new_values += delimiters
            break
        new_values.append(int(new_value))

    return (new_values, delimiters)

def get_filtered_data(data: list[int], delimiters: list[int]):
    """
    Find all values in the interval obtained by delimiters
    [left slice, right slice]
    :param data: rps_values fetched to int and sorted from smallest to largest
    :param delimiters: list with 2 values for slice
    :return: data_left_slice + data_right_slice
    """
    first_delimiter, second_delimiter = sorted(delimiters)
    # slice list by inserted values left and right part
    data_left_slice = data[:data.index(first_delimiter) + 1]
    data_right_slice = data[data.index(second_delimiter):]
    # unite values from left and right part
    return data_left_slice + data_right_slice

def calc_average(data: list[int]) -> int:
    """
    Calculate average value
    :param data: rps_values
    :return: average
    """
    average, _ = divmod(sum(data), len(data))
    return average

def calc_median(data: list[int]) -> int | float:
    """
    Calculate median value
    :param data: rps_values
    :return: median
    """
    quotient, remainder = divmod(len(data), 2)
    return data[quotient] if remainder else sum(data[quotient - 1: quotient + 1]) / 2

def calc_average_and_mean_diff(average: int | float, median: int | float) -> float:
    """
    Calculate difference between average and median in %
    :param average:
    :param median:
    :return: difference between average and median
    """
    return (abs(average - median) / average) * 100


if __name__ == "__main__":
    rps_values = [5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577',
                  '11602', 14116, '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180,
                  '17511', '13203', 13303, '7330', 7186, '10213', '8063', '12283', 15564, 17664, '8996', '12179',
                  '13657', 15817, '16187', '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454,
                  '17589', 5292, '13639', '7335', '11531', '14346', 7493, 15850, '12791', 11288]

    duplicate_values = {}

    # convert all str values in list to int
    rps_values = list(map(int, rps_values))

    new_values, delimiters = parse_args()
    rps_values += new_values
    rps_values = sorted(rps_values)

    if delimiters is not None:
        rps_values = get_filtered_data(rps_values, delimiters)

    average = calc_average(rps_values)
    median = calc_median(rps_values)

    # determine the type of load
    if calc_average_and_mean_diff(average, median) <= 25:
        print("Нагрузка стабильна")
    elif average > median:
        print("Происходят скачки")
    else:
        print("Происходят снижения")

    for value in set(rps_values):
        duplicate_values[value] = rps_values.count(value)
    print("Частоты встреченных значений: \n")
    print(duplicate_values)