import random


def main():

    print("Welcome to Sarah's dice simulator!")
    rolls = 0
    while True:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        rolls += 1
        print(f"Roll {rolls}: Die 1 = {die1}, Die 2 = {die2}")
        if die1 == die2:
            print(f"Doubles achieved in {rolls} rolls!")
            break

    total_rolls_to_doubles = rolls
    doubles_count = 0
    num_simulations = 10

    print(
        f"\n--- Calculating Percentage Chance of Rolling Doubles over {num_simulations} simulations ---"
    )
    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 == die2:
            doubles_count += 1

    percentage_doubles = (doubles_count / num_simulations) * 100
    print(
        f"Out of {num_simulations} individual rolls, doubles occurred {doubles_count} times."
    )
    print(f"Percentage chance of rolling doubles: {percentage_doubles:.2f}%")

    return total_rolls_to_doubles


if __name__ == "__main__":
    main()
