import re

napis='To be, or not to be, that is the question'
samogloski=re.findall('[eaoyiu]',napis)
print(len(samogloski))