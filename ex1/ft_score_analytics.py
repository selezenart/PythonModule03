#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("=== Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided!")
        sys.exit(1)

    scores: list[int | float] = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            try:
                scores.append(float(arg))
            except ValueError:
                print(f"Invalid score discarded: {arg}")

    if len(scores) == 0:
        print("No valid scores to analyze!")
        sys.exit(1)

    number: int | float = len(scores)
    total: int | float = sum(scores)
    average: float = total / number
    highest: int | float = max(scores)
    lowest: int | float = min(scores)
    score_range: int | float = highest - lowest

    print("=== Player Score Analytics ===")
    print(f"Scores processed: {scores}")
    print(f"Total players: {number}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {highest}")
    print(f"Low score: {lowest}")
    print(f"Score range: {score_range}")
