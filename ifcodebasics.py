#AnotherExample(CodeBasics)
Swahili = ["Mayai", "Wari", "Ugari"]
Namwanga = ["Amenza","Umupunga", "Insima"]
English = ["Eggs", "Rice","Nshima"]
dish = input("Enter a dish name:")
if dish in Swahili:
    print("Swahili")
elif dish in Namwanga:
    print("Namwanga")
elif dish in English:
    print("English")
else:
    print("Unknown Language")
    