dict1 = {
    "Name": "Astik",
    "Script": "Python",
    "Genre": "Pop",
    "Python": {1 : 2.6, 2 : 3.6, 3: 3.8},
    "Grade": "This is FUN!"
}
print(dict1)

del dict1["Genre"] #deletes genre key and its value
print(dict1)

del dict1["Python"][1] #deletes 2.6 under Python sub-dictionary
print(dict1)

del dict1["Grade"] #deletes grade key and its content
print(dict1)
