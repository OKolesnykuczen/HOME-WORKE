def get_bounded_int(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))

            if min_val <= value <= max_val:
                return value

            print(f"Введіть число від {min_val} до {max_val}.")
        except ValueError:
            print("Помилка! Введіть число.")


def print_contracts(contracts):
    if not contracts:
        print("Список контрактів порожній.")
        return

    for contract in contracts:
        print(
            f'ID: {contract["id"]} | '
            f'{contract["title"]} | '
            f'Нагорода: {contract["reward"]} монет | '
            f'Статус: {contract["status"]}'
        )


def add_contract(contracts):
    title = input("Введіть назву контракту: ").strip()

    for contract in contracts:
        if contract["title"].strip().lower() == title.lower():
            print("Контракт з такою назвою вже існує.")
            return

    reward = get_bounded_int(
        "Введіть нагороду (1-10000): ",
        1,
        10000
    )

    if contracts:
        new_id = max(contract["id"] for contract in contracts) + 1
    else:
        new_id = 1

    new_contract = {
        "id": new_id,
        "title": title,
        "reward": reward,
        "status": "активний"
    }

    contracts.append(new_contract)

    print(f"Контракт додано! ID: {new_id}")


def complete_contract(contracts):
    if not contracts:
        print("Список контрактів порожній.")
        return

    contract_id = get_bounded_int(
        "Введіть ID контракту: ",
        1,
        1000000
    )

    for contract in contracts:
        if contract["id"] == contract_id:
            contract["status"] = "виконано"
            print("Контракт виконано!")
            return

    print("Контракт з таким ID не знайдено.")


def guild_statistics(contracts):
    if not contracts:
        return 0, 0, "Немає контрактів"

    completed = 0
    active_rewards = []

    for contract in contracts:
        if contract["status"] == "виконано":
            completed += 1
        elif contract["status"] == "активний":
            active_rewards.append(contract["reward"])

    completed_percent = completed / len(contracts) * 100

    if active_rewards:
        average_reward = sum(active_rewards) / len(active_rewards)
    else:
        average_reward = 0

    most_expensive = max(
        contracts,
        key=lambda contract: contract["reward"]
    )

    return completed_percent, average_reward, most_expensive["title"]


def main():
    contracts = [
        {
            "id": 1,
            "title": "Захистити місто",
            "reward": 500,
            "status": "активний"
        },
        {
            "id": 2,
            "title": "Перемогти дракона",
            "reward": 2000,
            "status": "виконано"
        },
        {
            "id": 3,
            "title": "Знайти артефакт",
            "reward": 1000,
            "status": "активний"
        }
    ]

    while True:
        print("\n=== ГІЛЬДІЯ НАЙМАНЦІВ ===")
        print("1. Показати всі контракти")
        print("2. Додати контракт")
        print("3. Виконати контракт")
        print("4. Показати статистику")
        print("0. Вийти")

        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            print_contracts(contracts)

        elif choice == "2":
            add_contract(contracts)

        elif choice == "3":
            complete_contract(contracts)

        elif choice == "4":
            completed_percent, average_reward, most_expensive = guild_statistics(contracts)

            print("\n=== СТАТИСТИКА ===")
            print(f"Виконано контрактів: {completed_percent:.1f}%")
            print(f"Середня нагорода активних: {average_reward:.1f} монет")
            print(f"Найдорожчий контракт: {most_expensive}")

        elif choice == "0":
            print("Програму завершено.")
            break

        else:
            print("Неправильний пункт меню. Спробуйте ще раз.")


main()