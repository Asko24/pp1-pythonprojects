class Student():

    university='UEK Kraków'
    field='Informatyka Stosowana'
    album=100000
    
    def __init__(self,name):
        self.name=name
        self.album=Student.album
        Student.album+=1
    
    def __str__(self):
        return f'''
Name: {self.name}
Album {self.album}
Field: {Student.field}
University: {Student.university}'''
    
student1=Student('Adam Niezgódka')
print(student1)
student2=Student('Krzysztof Kanciarz')
print(student2)
student3=Student('Wiesław Wszywka')
print(student3)
    