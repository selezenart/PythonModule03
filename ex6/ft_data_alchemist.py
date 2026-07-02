#!/usr/bin/python3
import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam",
    ]
    print(f"Initial list of players: {players}")

    all_caps: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_caps}")

    caps_only: list[str] = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {caps_only}")

    scores: dict[str, int] = {
        name: random.randint(1, 1000) for name in all_caps
    }
    print(f"Score dict: {scores}")

    average: float = sum(scores[name] for name in scores) / len(scores)
    print(f"Score average is {round(average, 2)}")

    high: dict[str, int] = {
        n: scores[n] for n in scores if scores[n] > average
    }
    print(f"High scores: {high}")
