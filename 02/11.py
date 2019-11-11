login='marek'
password='m-123'

login_attempt=input('Wprowadz login: ')
password_attempt=input('Wprowadz haslo: ')

if login_attempt==login and password_attempt==password:
    print('Zalogowano pomyślnie')
else:
    print('Podane dane są nieprawidłowe')