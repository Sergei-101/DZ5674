# 1. Напишите функцию для транспонирования матрицы
# Пример:
# [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

list_1 = [[1, 2, 3], [4, 5, 6]]
res = zip(list_1[0], list_1[1])
res2 = list(map(list, res))
print(f"{list_1} -> {res2}")

# 2 Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента.
# (речь идет про **kwargs)

def new_dict(**kwargs):
    res_dict = {}
    for key, value in kwargs.items():
        res_dict[key] = value
    print(res_dict)

new_dict(name="Sergei", last_name = "Pupkin", has_car=True, age=38)

# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

def main():
    MODES = """Действия:
    пополнение - 1
    снятие - 2
    остаток на счету - 3
    все операции по счёту - 4
    выйти - 5
    """

    LUXURY_LIMIT = 5_000_000
    TAX_LUXURY = 0.9
    TAX_OUTCOME = 0.015
    MAX_TAX_OUT = 600
    MIN_TAX_OUT = 30
    MONEY_DIV = 50
    BONUS_FOR_OPERATION = 1.03
    balance = 0
    operations_count = 0
    operation_list = []
    print(MODES)
    while True:
        choose = input(f"Выберите действие - ")
        taxes(operations_count, balance, BONUS_FOR_OPERATION, LUXURY_LIMIT, TAX_LUXURY)
        if choose == '1':
            adding_funds(MONEY_DIV, balance, operation_list, operations_count)
        elif choose == '2':
            withdrawal(MONEY_DIV, balance, TAX_OUTCOME, MAX_TAX_OUT, MIN_TAX_OUT, operations_count, operation_list)
        elif choose == '3':
            print(f"Остаток денег на счёту - {balance}")
        elif choose == '4':
            print(operation_list)
        elif choose == '5':
            break

        else:
            print(f'Incorrect')



def adding_funds(MONEY_DIV, balance, operation_list, operations_count):
    income = int(input("Введите сумму пополнения - "))
    if income % MONEY_DIV == 0:
        balance += income
        print(f"Сумма зачислена успешна {income}, на счёту - {balance}")
        operation_list.append(income)
    else:
        print('incorrect summ')
    operations_count += 1

def withdrawal(MONEY_DIV, balance, TAX_OUTCOME, MAX_TAX_OUT, MIN_TAX_OUT, operations_count, operation_list):
    outcome = int(input("Введите сумму снятия - "))
    if outcome % MONEY_DIV == 0:
        comission = balance * TAX_OUTCOME
        if comission >= MAX_TAX_OUT:
            comission = MAX_TAX_OUT
        elif comission <= MIN_TAX_OUT:
            comission = MIN_TAX_OUT
        balance -= comission
        balance -= outcome
        operations_count += 1
        operation_list.append(int(f"-{outcome}"))
    else:
        print('incorrect summ')
def taxes(operations_count, balance, BONUS_FOR_OPERATION, LUXURY_LIMIT, TAX_LUXURY):
    if operations_count == 3:
        balance *= BONUS_FOR_OPERATION
        print('Бонус за 3 операции')
        operations_count = 0
    if balance >= LUXURY_LIMIT:
        balance *= TAX_LUXURY
        print('Раскулачивание')
main()