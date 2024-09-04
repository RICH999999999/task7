my_dict = {"Vasya": 1975, "Egor":1999, "Masha":2002}
print("Dict:",my_dict)
# существующее значение по ключу и отсутвующий
print("Existing value:",my_dict.get("Masha"))
print("Not existing value:",my_dict.get("Rich"))
# добавил две производные в словарь
my_dict["Adam"] = 1994
my_dict["Ramil"] = 1999
# удаляю одну из пар
deleted_value = my_dict.pop("Egor", None)
print("Deleted value:", deleted_value)
print("Modified dictionary:",my_dict)

my_set = {1,'Яблоко', 42.314}
print("Set:", my_set)
my_set.add(5)
my_set.add(6)
my_set.discard(1)
print("Modified set:",my_set)