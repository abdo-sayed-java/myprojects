# # 1
# def validate_input(func):
#     def wrapper(num):
#         if num < 0:
#             raise ValueError("Number must be non-negative")
#         return func(num)
#     return wrapper

# @validate_input
# def square(num):
#     return num * num

# square1 = square(5)
# square1 = square(-5)
# print(square1)

# # 2
# class Counter:
#     count = 0
#     def __init__(self):
#         Counter.count += 1

#     @classmethod
#     def get_count_number(cls):
#         return cls.count
    
# x = Counter()
# y = Counter()
# z = Counter()

# print(Counter.get_count_number())
    
# # 3
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     @property
#     def area(self):
#         return self.width * self.height

#     @property
#     def perimeter(self):
#         return (self.width + self.height) * 2

# Rectangle1 = Rectangle(10,5)
# print(Rectangle1.area)
# print(Rectangle1.perimeter)




class Combined:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Combined.count += 1

    def validate_input(func):
        def wrapper(self, num ,*args, **kwargs):
            if (num < 0):
                raise ValueError("The number must be positive!") 
            return func(self, num ,*args, **kwargs)
        return wrapper

    @classmethod
    def get_count(cls):
        return cls.count
    
    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return (self.width + self.height) * 2
    
    @validate_input
    def square(self,num):
        return num * num

object1 = Combined(10,5)
print(object1.square(5))
print(object1.square(-5))

x = Combined(10,5)
y = Combined(6,3)
z = Combined(3,1)
print(Combined.get_count())

print(object1.area)
print(object1.perimeter)
