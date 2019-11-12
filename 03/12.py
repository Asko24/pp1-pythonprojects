with open ('Shoppinglist.txt','a') as file:
    produkt=input('Wpisz nazwe produktu: ')
    file.write(f'{produkt}\n')