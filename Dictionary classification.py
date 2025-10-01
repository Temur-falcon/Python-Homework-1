
#Question 1 : Write a python program to convert a list to a list of dictionaries.

color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

for name , code in zip(color_names, color_codes):
    print({"color_name" : name, "color_code": code })

#I used zip because without zip I was getting an error that there are too much values to unpack