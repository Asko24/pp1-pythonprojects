import random
cpu_roll=int(random.randint(1,6))
player_guess=int(input('Podaj, ile oczek kostki wyrzucił komputer: '))
print('Komputer wyrzucił: ',cpu_roll)
print('Zgadłeś: ',cpu_roll==player_guess)