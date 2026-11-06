backpack = [
    {"item": "зілля лікування", "type": "спорядження", "quantity": 3},
    {"item": "залізний меч", "type": "зброя", "quantity": 1},
    {"item": "смолоскип", "type": "спорядження", "quantity": 2},
]

print("Вміст рюкзака:")

for item in backpack:
    print(f"• {item['item']} ({item['type']}) — {item['quantity']} шт.")

new_item = input("Введіть назву предмета: ").strip()
new_type = input("Введіть тип предмета: ").strip()
new_quantity = int(input("Введіть кількість: ").strip())

found = False

for item in backpack:
    if item["item"].lower().strip() == new_item.lower().strip():
        item["quantity"] += new_quantity
        found = True
        break

if not found:
    backpack.append({
        "item": new_item,
        "type": new_type,
        "quantity": new_quantity
    })

total_quantity = 0

for item in backpack:
    total_quantity += item["quantity"]

print(f"Загальна кількість одиниць у рюкзаку: {total_quantity} шт.")

search_item = input("Введіть назву предмета для пошуку: ").lower().strip()

found_item = False

for item in backpack:
    if item["item"].lower().strip() == search_item:
        print(
            f"Знайдено: {item['item']} "
            f"({item['type']}) — {item['quantity']} шт."
        )
        found_item = True
        break

if not found_item:
    print(f"Предмету «{search_item}» немає в рюкзаку.")

equipment_quantity = 0

for item in backpack:
    if item["type"].lower().strip() == "спорядження":
        equipment_quantity += item["quantity"]

print(f"Усього спорядження: {equipment_quantity} шт.")