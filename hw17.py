# .1 עבודה עם- dict
# צור מילון עבור מדינת ישראל ושים בו את הפרטים הבאים:


# name: Israel
# birth: 1948
# population_millions: 9.3
# capital: Jerusalem
# language: Hebrew
# cities: Jerusalem, Tel Aviv, Haifa, Rishon LeZion, Petah Tikva, Ashdod
# currency: ILS
# area_Kilometer: 22,145
# gdp_billion: 450

israel: dict = {'name': 'Israel', 'birth': 1948, 'population_millions': 9.3, 'capital': 'Jerusalem',
                'cities': ['Jerusalem', 'Tel Aviv', 'Haifa', 'Rishon LeZion', 'Petah Tikva', 'Ashdod'], 'currency': 'ILS', "area_Kilometer": 22145, 'gdp_billion': 450 }
print(israel)

# a. מצא והדפס את עיר הבירה. רמז: get
print('capital is:', israel.get('capital'))

# b. הדפס את כל המפתחות. רמז: keys
keys: list[str] = israel.keys()
print("israel keys:",keys)

# c. הדפס את כל הערכים. רמז: values
values: list[any] = israel.values()
print("israel values:", israel.values())

# d. הדפס את כל זוגות הערכים בלולאה תוך שימוש ב - unpack. רמז: items
for key, value in israel.items():
    print(f'key = {key}, value = {value}')

# e. העתק את המילון שעשית למילון חדש, רמז: copy
copy_israel = israel.copy()
print(copy_israel)

# f. משוך ומחק מהמילון החדש את ה- billion_gpd. רמז: pop
copy_israel.pop("gdp_billion")
print(copy_israel)

# g. צור מילון חדש מאותם המפתחות )וערכים ריקים(, רמז fromkeys. לאחר מכן, קלוט
# מהמשתמש ערך לכל שדה. הכנס את הערכים שנקלטו מהמשתמש למילון החדש .
# כלומר- קלוט את שם המדינה , לאחר מכן את שנת ה לידה של המדינה וכו'
# )עבור שדה הערים: קלוט 3 מחרוזות לשמות ערים ואח סן אותם ברשימה(
# לאחר סיום הקלט, הדפס את המילון שנוצר עם כל ה ערכים בתוכו

new_dict: dict = israel.fromkeys(keys)
print(new_dict)
for key in new_dict:
    if key == "cities":
        new_dict[key] = [input(f"enter city {i+1}: ") for i in range(3)]
    else:
        new_dict[key] = input(f"enter {key}: ")

print(new_dict)


# .2 שאלת מחרוזות - leetcode
# יש לקבל מחרוזת ולהדפיס את אורך המילה האחרונה במחרוזת


# Example 1:
a = "Hello World"
words_a: list[str] = a.split()
print(len(words_a[-1]))


# Example 2:
b = "   fly me   to   the moon  "
words_b: list[str] = b.split()
print(len((words_b[-1])))

# Example 3:
c = "luffy is still joyboy"
words_c: list[str] = c.split()
print(len((words_c[-1])))