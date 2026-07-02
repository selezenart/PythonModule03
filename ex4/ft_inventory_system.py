#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        parts: list[str] = arg.split(":")
        if len(parts) != 2 or len(parts[0]) == 0 or len(parts[1]) == 0:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name: str = parts[0]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            quantity: int = int(parts[1])
        except ValueError as err:
            print(f"Quantity error for '{name}': {err}")
            continue
        inventory.update({name: quantity})

    print(f"Got inventory: {inventory}")

    items: list[str] = list(inventory.keys())
    print(f"Item list: {items}")

    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    if len(inventory) == 0:
        print("At the beginning of the game, "
              "your inventory is usually empty ;)")
        sys.exit(0)

    for name in inventory.keys():
        percent: float = round(inventory[name] / total * 100, 1)
        print(f"Item {name} represents {percent}%")

    most: str = items[0]
    least: str = items[0]
    for name in inventory.keys():
        if inventory[name] > inventory[most]:
            most = name
        if inventory[name] < inventory[least]:
            least = name
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
