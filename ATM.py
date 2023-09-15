# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

def balance(money):
    print(f"Ваш баланс равен: {money}")


def payment(money):  # пополнение баланса

     deposit = int(input("Введите число кратное 50, чтобы пополнить счет: "))
    while  deposit % 50 != 0:
         deposit = int(input("Вы ошиблись, введите число кратное 50 : "))
    return  deposit


def withdraw_money(money):  # снятие средств

    comission = 0.015
     deposit = int(input("Введите число кратное 50, чтобы снять деньги со счета: "))
    while  deposit % 50 != 0:
         deposit = int(input("Вы ошиблись, введите число кратное 50 : "))
    if  deposit * comission < 30:
        total_com = 30
    elif  deposit * comission > 600:
        total_com = 600
    else:
        total_com =  deposit * comission
    print(f"Вы сняли с вашего счета { deposit} + комиссия {total_com}")
    return  deposit + total_com


balans_lst = []  # все балансы
action = 0  # выбор
money = 1000000  # начальная сумма
count = 0  # счетчик действий
while action != 4:
    balans_lst.append(money)
    action = int(
        input("Введите цифру 1 - Пополнить, 2 - Снять, 3 - вывести список всех предыдущих балансов, 4 - выйти : "))
    if action == 1:
        money =  deposit(money) + money
    balance(money)
    money = (money)
    if action == 4:
        (balans_lst)
    if action == 2:
        TAKE = withdraw_money(money)
        money = money - TAKE
        if money < 0:
            print("Вы попытались обмануть банкомат? У вас нет столько денег на счету! Попытка не удалась :(")
            money += TAKE
            print(f"На счет вернулось {TAKE} включая комиссию.")
