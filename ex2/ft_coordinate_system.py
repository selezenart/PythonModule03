#!/usr/bin/python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw: str = input("Enter player coordinates (x,y,z): ")
        parts: list[str] = raw.split(",")
        try:
            x_str, y_str, z_str = parts
        except ValueError:
            print("Invalid input! Please use the format x,y,z")
            continue
        try:
            x: float = float(x_str)
            y: float = float(y_str)
            z: float = float(z_str)
        except ValueError:
            print("Invalid input! Coordinates must be numbers")
            continue
        return (x, y, z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    first: tuple[float, float, float] = get_player_pos()
    print(f"Player position: {first}")
    print(f"X: {first[0]}")
    print(f"Y: {first[1]}")
    print(f"Z: {first[2]}")

    center_dist: float = math.sqrt(first[0] ** 2 + first[1] ** 2
                                   + first[2] ** 2)
    print(f"Distance to center (0, 0, 0): {round(center_dist, 2)}")

    second: tuple[float, float, float] = get_player_pos()
    print(f"New player position: {second}")

    move_dist: float = math.sqrt(
        (second[0] - first[0]) ** 2
        + (second[1] - first[1]) ** 2
        + (second[2] - first[2]) ** 2
    )
    print(f"Distance traveled: {round(move_dist, 2)}")
