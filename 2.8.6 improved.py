if __name__ == "__main__":
    rps_values = [5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577',
                  '11602', 14116, '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180,
                  '17511', '13203', 13303, '7330', 7186, '10213', '8063', '12283', 15564, 17664, '8996', '12179',
                  '13657', 15817, '16187', '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454,
                  '17589', 5292, '13639', '7335', '11531', '14346', 7493, 15850, '12791', 11288]

    # keeps new values to define condition
    new_values = None

    # delimiters from list
    delimiters = None
    
    # repeated values count
    duplicate_values = {}

    # convert all str values in list to int
    rps_values = list(map(int, rps_values))

    # check conditions
    while new_values != ' ' and new_values != '[':
        new_values = input("enter value:")
        if new_values == ' ':
            break
        if ';' in new_values:  # a;b;c
            rps_values += list(map(int, new_values.split(';')))
            continue
        if '[' in new_values:  # [a, b]
            delimiters = list(map(int, new_values.strip('][').split(', ')))
            rps_values += delimiters
            break
        rps_values.append(int(new_values))
        
    # sort values from smallest to largest
    rps_values = sorted(rps_values)

    # if user inserted value was a list
    if delimiters is not None:
        first_delimiter, second_delimiter = sorted(delimiters)
        # slice list by inserted values left and right part
        rps_values_left_slice = rps_values[:rps_values.index(first_delimiter) + 1]
        rps_values_right_slice = rps_values[rps_values.index(second_delimiter):]
        # unite values from left and right part
        rps_values = rps_values_left_slice + rps_values_right_slice
        print(rps_values)

    # average value count
    print(rps_values)
    average = divmod(sum(rps_values), len(rps_values))[0]
    print("Среднее:", average)
    
    # median value count
    quotient, remainder = divmod(len(rps_values), 2)
    median = rps_values[quotient] if remainder else sum(rps_values[quotient - 1: quotient + 1]) / 2
    print("Медиана:", median)

    average_and_mean_diff = None
    # difference between average and median in %
    if average > median:
        average_and_mean_diff = ((average - median) / average) * 100
        print(f"Разница в % между средним:{average} и медианой:{median} = {round(average_and_mean_diff)}%")
    else:
        average_and_mean_diff = ((median - average) / average) * 100
        print(f"Разница в % между средним:{average} и медианой:{median} = {round(average_and_mean_diff)}%")

    if average_and_mean_diff <= 25:
        print("Нагрузка стабильна")
    elif average > median:
        print("Происходят скачки")
    else:
        print("Происходят снижения")

    for value in set(rps_values):
        duplicate_values[value] = rps_values.count(value)
    print("Частоты встреченных значений: \n")
    print(duplicate_values)
