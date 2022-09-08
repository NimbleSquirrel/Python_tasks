if __name__ == "__main__":
    # taking multiple inputs separated by ;
    rps_values = []
    # keeps new values to check condition
    new_values = None

    # check conditions
    while new_values != ' ':
        new_values = input("enter value:")
        if new_values == ' ':
            break
        if ';' in new_values:
            rps_values += list(map(int, new_values.split(';')))
            continue
        rps_values.append(int(new_values))

    print(rps_values)

    # TODO посчитать среднее значение
    average_and_remainder = divmod(sum(rps_values), len(rps_values))
    average = average_and_remainder[0]
    print("Среднее значение:", average)

    # TODO посчитать медианное значение
    rps_values_sorted = sorted(rps_values)
    quotient, remainder = divmod(len(rps_values), 2)
    median = rps_values_sorted[quotient] if remainder else sum(rps_values_sorted[quotient - 1: quotient + 1]) / 2
    print("Медиана", median)

    # TODO определить если среднгее значение больше медианы
    is_average_higher = average > median

    average_and_mean_diff = None
    # TODO расчитать разницу между средним и медианой в %
    if is_average_higher:
        average_and_mean_diff = (((average - median) / average) * 100)
        print(f"Разница в % между средним:{average} и медианой:{median} = {round(average_and_mean_diff)}%")
    else:
        average_and_mean_diff = ((median - average) / average) * 100
        print(f"Разница в % между средним:{average} и медианой:{median} = {round(average_and_mean_diff)}%")

    # TODO определить тип нагрузки
    # TODO поправить распределение нагрузки
    if is_average_higher and average_and_mean_diff > 25:
        print("Происходят скачки")

    elif not is_average_higher or average_and_mean_diff > 25:
        print("Происходит снижение")
    else:
        print("Нагрузка стабильна")



