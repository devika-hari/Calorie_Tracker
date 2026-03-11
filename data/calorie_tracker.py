import csv

def read_input(file_path):
    entries = [] #list of dictionaries

    with open(file_path) as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not row["date"]:
                continue # skip if no date
            # convert numeric values
            row["calories"] = int(row["calories"])
            row["protein_g"] = int(row["protein_g"])
            row["carbs_g"] = int(row["carbs_g"])
            row["fat_g"] = int(row["fat_g"])
            entries.append(row)
    return entries

#Calories per day
def calories_per_day(entries):
    calories_by_day = {}
    for entry in entries:
        date = entry["date"]
        calories = entry["calories"]
        calories_by_day[date]= calories_by_day.get(date,0) + calories
    return calories_by_day

def day_with_most_calories(calories_by_day):
    max_day = max(calories_by_day, key=calories_by_day.get)
    return max_day, calories_by_day[max_day] #return tuple

#highest calorie food
def highest_calorie_food(entries):
    max_food = None
    max_calories = 0
    for entry in entries:
        if entry["calories"]>max_calories:
            max_food=entry["food"]
            max_calories=entry["calories"]
    return max_food, max_calories #return tuple

#food with the highest protein
def highest_protein_food(entries):
    max_food = None
    max_protein = 0

    for entry in entries:
        if entry["protein_g"]>max_protein:
            max_food=entry["food"]
            max_protein=entry["protein_g"]
    return max_food, max_protein



def main():
    entries = read_input("input.csv")

    daily_calories = calories_per_day(entries)
    day, calories = day_with_most_calories(daily_calories)

    food, cal = highest_calorie_food(entries)
    protein_food, protein = highest_protein_food(entries)

    print("Day with most calories:", day, calories)
    print("Highest calorie food:", food, cal)
    print("Highest protein food:", protein_food, protein)

if __name__ == "__main__":
    main()

