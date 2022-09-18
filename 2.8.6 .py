def cast_to_int(strings: list[str]) -> list[int]:
    return list(map(int, [symbol for symbol in strings if symbol.isdigit()]))

def get_filtered_data(data: list[int], delimiters: list[int]):
    """
    Find all values in the interval obtained by delimiters
    [left slice, right slice]
    :param data: rps_values fetched to int and sorted from smallest to largest
    :param delimiters: list with 2 values for slice
    :return: data
    """
    first_delimiter, second_delimiter = sorted(delimiters)
    # slice list by inserted values left and right part
    data = data[slice(first_delimiter, second_delimiter + 1)]
    # unite values from left and right part
    return data


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
    data = sorted(data)
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

def determine_load_type():
    if calc_average_and_mean_diff(average, median) <= 25:
        return print("Нагрузка стабильна")
    elif average > median:
        return print("Происходят скачки")
    else:
        return print("Происходят снижения")

if __name__ == "__main__":
    rps_values = [5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577',
                  '11602', 14116, '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180,
                  '17511', '13203', 13303, '7330', 7186, '10213', '8063', '12283', 15564, 17664, '8996', '12179',
                  '13657', 15817, '16187', '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454,
                  '17589', 5292, '13639', '7335', '11531', '14346', 7493, 15850, '12791', 11288]

    # convert all str values in list to int
    rps_values = list(map(int, rps_values))

    new_values: list[int] = []

    delimiters = None

    while True:
        new_value = input("enter values:")
        if new_value.strip() == '':  # break input
            break
        if ';' in new_value:  # a;b;c
            new_values += cast_to_int(new_value.split(';'))
            continue
        if '[' in new_value:  # [a, b] or [a,b]
            delimiters = cast_to_int(new_value.strip('][').split(','))
            if len(delimiters) != 2:
                delimiters = None
                break
        if new_value.isdigit():
            new_values.append(int(new_value))

    if delimiters is not None:
        rps_values = get_filtered_data(rps_values, delimiters)
        rps_values += new_values
        print(rps_values)

        average = calc_average(rps_values)
        median = calc_median(rps_values)

        determine_load_type()

        # подсчет частоты встречающихся значений
        frequency = {}
        for value in rps_values:
            frequency[value] = frequency.get(value, 0) + 1
        print(frequency)
    elif new_values:
        rps_values += new_values
        print(rps_values)

        average = calc_average(rps_values)
        median = calc_median(rps_values)

        determine_load_type()

        # подсчет частоты встречающихся значений
        frequency = {}
        for value in rps_values:
            frequency[value] = frequency.get(value, 0) + 1
        print(frequency)
