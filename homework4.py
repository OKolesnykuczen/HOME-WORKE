quests = [
    {"title": "Знайти стародавній меч", "reward": 100, "status": "в процесі"},
    {"title": "Перемогти дракона", "reward": 500, "status": "виконано"},
    {"title": "Зібрати 10 трав", "reward": 50, "status": "в процесі"}
]


def print_quests(quests):
    for quest in quests:
        if quest["status"] == "виконано":
            mark = "[x]"
        else:
            mark = "[ ]"

        print(f'{mark} {quest["title"]} — нагорода: {quest["reward"]} монет')


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Помилка! Введіть число.")


def add_quest(quests):
    title = input("Введіть назву нового квесту: ")
    reward = get_int_input("Введіть нагороду в монетах: ")

    quest = {
        "title": title,
        "reward": reward,
        "status": "в процесі"
    }

    quests.append(quest)
    print("Квест додано!")


def complete_quest(quests, title):
    for quest in quests:
        if quest["title"].lower() == title.lower():
            quest["status"] = "виконано"
            return True

    return False


def calculate_total_reward(quests):
    total = 0

    for quest in quests:
        if quest["status"] == "виконано":
            total += quest["reward"]

    return total


def main():
    print("=== ЖУРНАЛ КВЕСТІВ ===")

    print("\nПочатковий список квестів:")
    print_quests(quests)

    print("\n--- Додавання нового квесту ---")
    add_quest(quests)

    title = input("\nВведіть назву квесту, який ви щойно завершили: ")

    if complete_quest(quests, title):
        print("Квест позначено як виконаний!")
    else:
        print("Квест з такою назвою не знайдено.")

    print("\n--- Оновлений журнал ---")
    print_quests(quests)

    total = calculate_total_reward(quests)

    print(f"\nЗагальна сума заробленого золота: {total} монет")


main()