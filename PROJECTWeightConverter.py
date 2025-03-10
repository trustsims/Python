weight = int(input('Weight: '))
unit = input('(L)bs  or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos.")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds.")


#Further_Thought
currency = int(input('Currency: '))
unit = input('(ZMW)K or (USD)$: ')
if unit.upper() == "K100":
    forex = currency * 0.0387
    print(f"You are receiving {forex} dollars.")
else:
    forex = currency / 0.0387
    print(f"You are receiving {forex} kwacha")