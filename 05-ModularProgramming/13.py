def wspak(string):
    return string[::-1]
    
def rozstrzel(string):
    newstring=''
    for i in range (0,len(string)):
        newstring+=string[i]
        newstring+=' '
    return newstring

def slowazduzej(string):
    
    tab_capitalized=[]
    string=string.lower()
    tab_capitalized=string.split()
    
    for i in range (0,len(tab_capitalized)):
        tab_capitalized[i]=tab_capitalized[i].capitalize()
    for i in range (0,len(tab_capitalized)):
        print (tab_capitalized[i],end=' ')

x='uniwersytet ekonoMICZNY W kraKOWIE'
slowazduzej(x)