wzrost=float(input('Podaj wzrost w cm: '))
waga=float(input('Podaj wage w kg: '))
bmi=waga/(wzrost/100)**2
print('Twoje BMI wynosi: ',round(bmi,2))


if bmi<16:
    print('wygłodzenie')
elif bmi>16 and bmi<17:
    print('wychudzenie')
elif bmi>17 and bmi<18.5:
    print('niedowaga')
elif bmi>18.5 and bmi<25:
    print('wartość prawidłowa')
elif bmi>25 and bmi<30:
    print('nadwaga')
elif bmi>30 and bmi<35:
    print('I stopień otyłości')
elif bmi>35 and bmi<40:
    print('II stopień otyłości')
else:
    print('otyłość skrajna')