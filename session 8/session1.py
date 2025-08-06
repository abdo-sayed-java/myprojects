# 1
name = "Abdo"
age = 21

skills_levels = {
    "HTML": "sinor",
    "Python": "intermediate",
    "Django": "sinor",
    "JavaScript": "intermediate",
    "CSS": "sinor"
}
# 2
print(type(name))
print(type(age))
print(type(skills_levels))

# 3
skills_levels["java"] = "intermediate"

# 4
class Employee:
    # 9
    title = "PythonTech"

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    # 6
    def get_info(self):
        return f"Name: {self.name}, Department: {self.department}, Salary: {self.salary}"

    # 7
    def year_salry(self):
        return self.salary * 12
    
    # 10
    @classmethod
    def get_company(cls):
        return cls.title
    
    # 11
    @staticmethod
    def valid_salary(salary):
        if salary >= 6000:
            return True
        else:
            return False

# 5
employee1 = Employee("Abdo", "FullStack python", 8000)
employee2 = Employee("Ahmed", "IT", 10000)
print("\nname:" , employee1.name , "\ndepartment: " ,employee1.department, "\nsalary: ", employee1.salary)

# 8
print(employee1.get_info())
print(employee1.year_salry())
