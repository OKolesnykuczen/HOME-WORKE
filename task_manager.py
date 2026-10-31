
import random
import json

TASKS_FILE = "tasks.json"


def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def check_password_strength(password):
    has_digit = False
    has_upper = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    if len(password) >= 8 and has_digit and has_upper:
        return "надійний"
    else:
        return "слабкий"


def set_master_password():
    password = input("Придумай головний пароль: ")

    strength = check_password_strength(password)
    print("Надійність пароля:", strength)

    if strength == "слабкий":
        choice = input("Згенерувати надійний пароль? (так/ні): ")

        if choice.lower() == "так":
            password = generate_password(12)
            print("Твій новий пароль:", password)
        else:
            print("Використовуємо введений пароль.")

    return password


def login_gate(master_password):
    print("\nВхід до Менеджера задач.")

    for attempt in range(1, 4):
        entered = input("Введи пароль: ")

        if entered == master_password:
            print("Пароль правильний. Ласкаво просимо!")
            return True
        else:
            remaining = 3 - attempt
            print(f"Невірний пароль! Залишилося спроб: {remaining}")

    print("Доступ заблоковано через підозрілу активність!")
    return False


def save_tasks(tasks, filename=TASKS_FILE):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def load_tasks(filename=TASKS_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def show_menu():
    print("\n===== МЕНЕДЖЕР ЗАДАЧ =====")
    print("1. Додати завдання")
    print("2. Переглянути завдання")
    print("3. Видалити завдання")
    print("4. Позначити завдання виконаним")
    print("5. Змінити головний пароль")
    print("6. Вийти")


def add_task(tasks):
    text = input("Введи нове завдання: ")

    if text.strip() == "":
        print("Завдання не може бути порожнім.")
        return

    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print("Завдання додано!")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("Список завдань поки порожній.")
        return

    print("\nТвій список завдань:")

    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{index}. {status} {task['text']}")


def delete_task(tasks):
    if len(tasks) == 0:
        print("Немає завдань для видалення.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Введи номер завдання для видалення: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            save_tasks(tasks)
            print("Видалено завдання:", removed_task["text"])
        else:
            print("Неправильний номер завдання.")

    except ValueError:
        print("Потрібно ввести число.")


def mark_task_done(tasks):
    if len(tasks) == 0:
        print("Список завдань порожній.")
        return

    view_tasks(tasks)

    number = input("Введи номер виконаного завдання: ")

    if not number.isdigit():
        print("Потрібно ввести число.")
        return

    number = int(number)

    if number < 1 or number > len(tasks):
        print("Немає завдання з таким номером.")
        return

    tasks[number - 1]["done"] = True
    save_tasks(tasks)

    print("Завдання позначено виконаним:", tasks[number - 1]["text"])


def change_master_password():
    print("\nЗміна головного пароля.")

    return set_master_password()


if __name__ == "__main__":
    tasks = load_tasks()

    master_password = set_master_password()

    access_granted = login_gate(master_password)

    if access_granted:
        while True:
            show_menu()
            choice = input("Обери дію (1-6): ")

            if choice == "1":
                add_task(tasks)

            elif choice == "2":
                view_tasks(tasks)

            elif choice == "3":
                delete_task(tasks)

            elif choice == "4":
                mark_task_done(tasks)

            elif choice == "5":
                master_password = change_master_password()

            elif choice == "6":
                print("До побачення!")
                break

            else:
                print("Неправильний вибір. Спробуй ще раз.")
