CORRECT_CARD = "1710"
CORRECT_PIN = "1510"
authorized = False
for attempt in range(3):
    card = input("Введіть останні 4 цифри картки: ")
    pin = input("Введіть PIN-код: ")
    if card == CORRECT_CARD and pin == CORRECT_PIN:
        print("Авторизація успішна!")
        authorized = True
        break
    else:
        attempts_left = 2 - attempt
        print("Неправильний номер картки або PIN-код.")
        if attempts_left > 0:
            print("Залишилось спроб:", attempts_left)
if not authorized:
    print("Картку заблоковано через підозрілу активність!")
else:
    balance = 1000
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Перевірити баланс")
        print("2. Зняти гроші")
        print("3. Поповнити рахунок")
        print("4. Вийти")
        choose = input("Виберіть дію: ")
        if choose == "1":
            print("Ваш поточний баланс:", balance)
        elif choose == "2":
            amount = float(input("Введіть суму для зняття: "))
            if amount > 0 and amount <= balance:
                balance = balance - amount
                print("Гроші успішно знято.")
                print("Новий баланс:", balance)
            else:
                print("Помилка: некоректна сума або недостатньо коштів.")
        elif choose == "3":
            amount = float(input("Введіть суму поповнення: "))
            if amount > 0:
                balance = balance + amount
                print("Рахунок успішно поповнено.")
                print("Новий баланс:", balance)
            else:
                print("Помилка: сума повинна бути більшою за 0.")
        elif choose == "4":
            print("Дякуємо за користування банкоматом!")
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")