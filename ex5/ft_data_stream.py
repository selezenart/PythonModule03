#!/usr/bin/python3
import random
from typing import Iterator

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run", "eat", "sleep", "grab", "move",
    "climb", "swim", "release", "use",
]


def gen_event() -> Iterator[tuple[str, str]]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(events: list[tuple[str, str]]) -> Iterator[tuple[str, str]]:
    while len(events) > 0:
        index: int = random.randrange(len(events))
        yield events.pop(index)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    stream: Iterator[tuple[str, str]] = gen_event()
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    events: list[tuple[str, str]] = [next(stream) for _ in range(10)]
    print(f"Built list of {len(events)} events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
