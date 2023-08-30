from dataclasses import dataclass

@dataclass
class Student: #define attributes and set their data types
    name: str 
    school_id: str
    gpa: float

def main(): # define main function, test class by creating objects
    peter = Student('Peter', 'mc6987tc', 3.85)
    print(peter.name)
    print(peter.school_id)
    print(peter.gpa)
    print(peter)

    tammy = Student('Tammy', 'mc1234tc', 2.42)
    print(tammy)

main() # call main funtion