from datetime import date

class Person(object):
    def __init__(self, name: str, DOB: str):
        self.name = name
        self.DOB = DOB
    
    def speak(self):
        print('hello')
        
    def walk(self):
        print("walking away")
    
    def get_name(self):
        return self.name
    
    def get_year(self,DOB: str):
        return int(DOB.split('/')[2])
    
    def get_age(self):
        current_year = date.today().year
        return 23 - self.get_year(self.DOB)
    
    
class Student(Person):
    def __init__(self, name:str, DOB:str, courses:list[str]):
        super().__init__(name, DOB)
        self.courses = courses
        
    def get_courses(self):
        return self.courses
    
    def speak(self):
        print("I am so tired")
        
        
        
if __name__ == "__main__":
    kofi = Person("kofi", "07/02/05")
    ama = Student("Justina", "05/03/14",["DCIT202","DCIT111", "SOWK123"])

    kofi.speak()
    kofi.walk()
    print(kofi.get_age())
    print(kofi.get_name())
        
    ama.speak()
    ama.walk()
    print(ama.get_age())
    print(ama.get_name())
    print(ama.get_courses())
        
        
