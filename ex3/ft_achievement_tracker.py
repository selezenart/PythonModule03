#!/usr/bin/python3
import random

ACHIEVEMENTS: list[str] = [
    "First Steps",
    "Boss Slayer",
    "Speed Runner",
    "Master Explorer",
    "Treasure Hunter",
    "Survivor",
    "Untouchable",
    "Unstoppable",
    "Collector Supreme",
    "Strategist",
    "Sharp Mind",
    "Crafting Genius",
    "World Savior",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    # Pick a big fraction so unions/intersections stay likely non-empty.
    count: int = random.randint(len(ACHIEVEMENTS) // 2, len(ACHIEVEMENTS) - 1)
    return set(random.sample(ACHIEVEMENTS, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, owned in players.items():
        print(f"Player {name}: {owned}")

    all_achievements: set[str] = set()
    for owned in players.values():
        all_achievements |= owned
    print(f"All distinct achievements: {all_achievements}")

    common: set[str] = set(ACHIEVEMENTS)
    for owned in players.values():
        common &= owned
    print(f"Common achievements: {common}")

    for name, owned in players.items():
        others: set[str] = set()
        for other_name, other_owned in players.items():
            if other_name != name:
                others |= other_owned
        print(f"Only {name} has: {owned - others}")

    full: set[str] = set(ACHIEVEMENTS)
    for name, owned in players.items():
        print(f"{name} is missing: {full - owned}")
