Entertainement=[{"Going out":"2000", "Movies":"200", "Games":"1000"}]
travel=[{"Metro":"1600", "E-Rickshaw":"1200", "Random Ubers":"500"}]
food=[{"Lunch":"2000","Snacks":"1300"}]
wants=[{"Clothes":"2000","Shoes":"3000"}]

category=[Entertainement, travel, food,wants]
import time
import rich
rich.print("------  [red]Welcome to [green3]Expense Tracker  ------")
print()

isrunning=True
while isrunning:
    options=input(("Press 1 to see your total expenses: \nPress 2 to add expenses: \nPress 3 to see per category breakdown: \nPress 4 to exit \nEnter your option: "))

    total_expenses=0
    if options=="1":
        for i in Entertainement:
            for j in i:
                total_expenses+=int(i[j])
        for i in travel:
            for j in i:
                total_expenses+=int(i[j])
        for i in food:
            for j in i:
                total_expenses+=int(i[j])
        for i in wants:
            for j in i:
                total_expenses+=int(i[j])
        print(f"Your total expenses are: {total_expenses}")
        time.sleep(3)
        print("--------------------------------------------------------------")
        print()

    elif options=="2":
        add_expense=input("Do you want to add any expenses? (yes/no): ").lower()

        if add_expense=="no":
            print("No expenses added")
        elif add_expense=="yes":
            category_input=input("Enter the category (Entertainement/Travel/Food/Wants): ").title()
            item=input("Enter the item: ").title()
            amount=input("Enter the amount: ")

            if category_input=="Entertainement":
                Entertainement.append({item:amount})

            elif category_input=="Travel":
                travel.append({item:amount})

            elif category_input=="Food":
                food.append({item:amount})

            elif category_input=="Wants":
                wants.append({item:amount})

            else:
                print("Invalid category")
            print("Expense added successfully")
        time.sleep(3)
        print()
        print("--------------------------------------------------------------")

    elif options=="3":
        print("Your expenses per category are: ")
        entertainement_expenses=0
        travel_expenses=0
        food_expenses=0
        wants_expenses=0
        for i in Entertainement:
            for j in i:
                entertainement_expenses+=int(i[j])
        print(f"Entertainement: {entertainement_expenses}")
        for i in travel:
            for j in i:
                travel_expenses+=int(i[j])
        print(f"Travel: {travel_expenses}")
        for i in food:
            for j in i:
                food_expenses+=int(i[j])
        print(f"Food: {food_expenses}")
        for i in wants:
            for j in i:
                wants_expenses+=int(i[j])
        print(f"Wants: {wants_expenses}")
        time.sleep(3)
        print()
        print("--------------------------------------------------------------")

    elif options=="4":
        isrunning=False
        rich.print("------  [red]Thank you for [green3]]using Expense Tracker  ------")
    else:
        print("Invalid option. Please try again.")
        print()
        print("--------------------------------------------------------------")
        time.sleep(3)
