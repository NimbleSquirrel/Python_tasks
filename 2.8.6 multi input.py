if __name__ == "__main__":
    # taking multiple inputs separated by ;
    rps_values_by_package = []
    # taking values from input one by one
    rps_values_by_one = []
    # keeps new values to check condition
    new_values = None

    # check conditions
    while new_values != ' ':
        new_values = input("enter value:")
        if new_values != ' ' and ';' in new_values:
            rps_values_by_package.append(list(map(int, new_values.split(';'))))
            # TODO если нам попался [] лиcт, после него нужно завершить ввод и начать вычисления
        elif new_values != ' ':
            rps_values_by_one.append(new_values)

    # convert str data in list to int values
    rps_values_by_one_convert = list(map(int, rps_values_by_one))

    #TODO объединить списки внутри списка через цикл for
    union_inside_list = []
    for value in range(len(rps_values_by_package)):
        for subvalue in range(len(rps_values_by_package[value])):
            union_inside_list.append(rps_values_by_package[value][subvalue])

    #TODO соединить два листа вместе
    union_of_lists = sorted(rps_values_by_one_convert + union_inside_list)
    print(union_of_lists)

    # TODO посчитать среднее значение
    mean_value = divmod(sum(union_of_lists), len(union_of_lists))
    rps_mean_value = mean_value[0]
    print("Среднее значение:", rps_mean_value)

    # TODO посчитать медианное значение
    quotient, remainder = divmod(len(union_of_lists), 2)
    median = union_of_lists[quotient] if remainder else sum(union_of_lists[quotient - 1: quotient + 1]) / 2
    print("Медиана", median)

    # TODO определить если среднгее значение больше медианы
    is_mean_bigger_median = rps_mean_value > median

    load_percentage_difference = None
    # TODO расчитать разницу между средним и медианой в %
    if is_mean_bigger_median:
        load_percentage_difference = (((rps_mean_value - median) / rps_mean_value) * 100)
        print(f"Разница в % между средним:{rps_mean_value} and медианой:{median} = {load_percentage_difference}%")
    else:
        load_percentage_difference = ((median - rps_mean_value) / rps_mean_value) * 100
        print(f"Разница в % между средним:{rps_mean_value} and медианой:{median} = {load_percentage_difference}%")

    # TODO определить тип нагрузки
    if is_mean_bigger_median and load_percentage_difference > 25:
        print("Происходят скачки")

    elif not is_mean_bigger_median or load_percentage_difference > 25:
        print("Происходит снижение")
    else:
        print("Нагрузка стабильна")



