import random
import sys

def run():
    print("\n--- Vlink Minesweeper ---")
    size = 5
    mines_count = 3
    # Генерация поля
    field = [["?" for _ in range(size)] for _ in range(size)]
    mines = set()
    while len(mines) < mines_count:
        mines.add((random.randint(0, size-1), random.randint(0, size-1)))

    while True:
        for row in field: print(" ".join(row))
        try:
            move = input("Enter x y (or 'q'): ").split()
            if move[0] == 'q': break
            x, y = int(move[0]), int(move[1])
            if (x, y) in mines:
                print("BOOM! Game Over.")
                break
            field[y][x] = "."
        except: print("Invalid input")

if __name__ == "__main__":
    run()