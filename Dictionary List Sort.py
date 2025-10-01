
#Question 2 : Write a Python program to remove duplicate dictionary entries from a given list.

dctlist = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]

uniq_list = []

for dct in dctlist:
    if dct not in uniq_list:
        uniq_list.append(dct)

print(uniq_list)