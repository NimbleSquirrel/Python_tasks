if __name__ == "__main__":

    rps_values = [5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577',
                  '11602', 14116, '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180,
                  '17511', '13203', 13303, '7330', 7186, '10213', '8063', '12283', 15564, 17664, '8996', '12179',
                  '13657', 15817, '16187', '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454,
                  '17589', 5292, '13639', '7335', '11531', '14346', 7493, 15850, '12791', 11288]
    # keeps new values to deine condition
    new_values = None
    # if list was inserted by user
    has_list_inserted = None
    # check conditions
    while new_values != ' ' and new_values != '[':
        new_values = input("enter value:")
        if new_values == ' ':
            break
        if ';' in new_values:
            rps_values += list(map(int, new_values.split(';')))
            continue
        if '[' in new_values:
            rps_values += new_values.strip('][').split(', ')
            has_list_inserted = True
            break
        rps_values.append(int(new_values))
    # convert all str values in list to int
    rps_values_converted = list(map(int, rps_values))
    # if user inserted value was list
    if has_list_inserted:
        new_values_split = new_values.strip('][').split(', ')
        new_values_converted = list(map(int, new_values_split))
        a, b = sorted(new_values_converted)
        rps_values_sorted = sorted(rps_values_converted)
        # keep index to check where numbers will move
        what_is_a_index = rps_values_sorted.index(a)
        what_is_b_index = rps_values_sorted.index(b)
        # slice list by inserted values left and right part
        rps_values_left_slice = rps_values_sorted[:what_is_a_index + 1]
        rps_values_right_slice = rps_values_sorted[what_is_b_index:]
        # unite values from left and right part
        sliced_result = rps_values_left_slice + rps_values_right_slice
        # average value count
        average_and_remainder = divmod(sum(sliced_result), len(sliced_result))
        average = average_and_remainder[0]
        # median value count
        quotient, remainder = divmod(len(sliced_result), 2)
        median = sliced_result[quotient] if remainder else sum(sliced_result[quotient - 1: quotient + 1]) / 2
        # check what value is bigger
        is_average_higher = average > median
        is_median_higher = average < median

        average_and_mean_diff = None
        # difference between average and median in %
        if is_average_higher:
            average_and_mean_diff = (((average - median) / average) * 100)
            #print(f"Разница в % между средним:{average} и медианой:{median} = {round(average_and_mean_diff)}%")
        else:
            average_and_mean_diff = ((median - average) / average) * 100
            #print(f"Разница в % между средним:{average} и медианой:{median} = {round(average_and_mean_diff)}%")

        # determine the type of load
        if is_average_higher and average_and_mean_diff > 25:
            print("Происходят скачки")
        elif is_median_higher and average_and_mean_diff > 25:
            print("Происходят снижения")
        else:
            print("Нагрузка стабильна")
    else:
        # average value count
        average_and_remainder = divmod(sum(rps_values_converted), len(rps_values_converted))
        average = average_and_remainder[0]
        # median value count
        rps_values_sorted = sorted(rps_values_converted)
        quotient, remainder = divmod(len(rps_values_sorted), 2)
        median = rps_values_sorted[quotient] if remainder else sum(rps_values_sorted[quotient - 1: quotient + 1]) / 2
        # check what value is bigger
        is_average_higher = average > median
        is_median_higher = average < median

        average_and_mean_diff = None
        # difference between average and median in %
        if is_average_higher:
            average_and_mean_diff = (((average - median) / average) * 100)
            #print(f"Разница в % между средним:{average} и медианой:{median} = {round(average_and_mean_diff)}%")
        else:
            average_and_mean_diff = ((median - average) / average) * 100
            #print(f"Разница в % между средним:{average} и медианой:{median} = {round(average_and_mean_diff)}%")
        # determine the type of load
        if is_average_higher and average_and_mean_diff > 25:
            print("Происходят скачки")
        elif is_median_higher and average_and_mean_diff > 25:
            print("Происходят снижения")
        else:
            print("Нагрузка стабильна")



