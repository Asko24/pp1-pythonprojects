numer_rachunku=input('Wpisz numer rachunku: ')
numer_rachunku=numer_rachunku[:2]+' '+numer_rachunku[2:6]+' '+numer_rachunku[6:10]+' '+numer_rachunku[10:14]+' '+numer_rachunku[14:18]+' '+numer_rachunku[18:22]+' '+numer_rachunku[22:26]
print('Numer rachunku po formatowaniu: ',numer_rachunku)


''' RACZEJ DŁUŻSZY SPOSÓB
numer_rachunku=numer_rachunku[:2]+' '+numer_rachunku[2:]
numer_rachunku=numer_rachunku[:7]+' '+numer_rachunku[7:]
numer_rachunku=numer_rachunku[:12]+' '+numer_rachunku[12:]
numer_rachunku=numer_rachunku[:17]+' '+numer_rachunku[17:]
numer_rachunku=numer_rachunku[:22]+' '+numer_rachunku[22:]
numer_rachunku=numer_rachunku[:27]+' '+numer_rachunku[27:]
print('Numer rachunku po formatowaniu: ',numer_rachunku)
'''