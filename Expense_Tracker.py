import time

import rich


CATEGORIES = {
    "Entertainment": {"Going out": 2000, "Movies": 200, "Games": 1000},
    "Travel": {"Metro": 1600, "E-Rickshaw": 1200, "Random Ubers": 500},
    "Food": {"Lunch": 2000, "Snacks": 1300},
    "Wants": {"Clothes": 2000, "Shoes": 3000},
}


def category_total(expenses):
    return sum(expenses.values())


def read_amount():
    raw_amount = input("Enter the amount (whole, non-negative rupees): ").strip()
    try:
        amount = int(raw_amount)
    except ValueError:
        return None
    return amount if amount >= 0 else None


def main():
    rich.print("------  [red]Welcome to [green3]Expense Tracker  ------")
    while True:
        options = input(
            "Press 1 to see your total expenses:\n"
            "Press 2 to add expenses:\n"
            "Press 3 to see per category breakdown:\n"
            "Press 4 to exit\nEnter your option: "
        ).strip()

        if options == "1":
            total = sum(category_total(expenses) for expenses in CATEGORIES.values())
            print(f"Your total expenses are: {total}")
            time.sleep(1)
        elif options == "2":
            if input("Do you want to add any expenses? (yes/no): ").strip().lower() != "yes":
                print("No expenses added")
                continue

            category_name = input(
                f"Enter the category ({'/'.join(CATEGORIES)}): "
            ).strip().title()
            if category_name not in CATEGORIES:
                print("Invalid category; no expense was added.")
                continue

            item = input("Enter the item: ").strip().title()
            if not item:
                print("Item cannot be empty; no expense was added.")
                continue

            amount = read_amount()
            if amount is None:
                print("Enter a valid non-negative whole-number amount; no expense was added.")
                continue

            CATEGORIES[category_name][item] = CATEGORIES[category_name].get(item, 0) + amount
            print("Expense added successfully")
            time.sleep(1)
        elif options == "3":
            print("Your expenses per category are:")
            for name, expenses in CATEGORIES.items():
                print(f"{name}: {category_total(expenses)}")
            time.sleep(1)
        elif options == "4":
            rich.print("------  [red]Thank you for using Expense Tracker  ------")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
