# name="bob"
# eman='sosi'
# b= 'hallo, {}.   {}'
# wb=b.format(name, eman)
# print(wb)
#
# name= input('enter uour name:')
# print (name)
#
# size_input = input("How big is your house (in square feet): ")
# square_feet = float(size_input)
# square_metres = square_feet / 10.8  # Make sure this is correct
# print(f"{square_feet} square feet is {square_metres:.2} square metres.")
#
# l = ["Bob", "Rolf", "Anne"]
# t = ("Bob", "Rolf", "Anne")
# s = {"Bob", "Rolf", "Anne"}
#
# # Access individual items in lists and tuples using the index.
#
# print(l[0])
# print(t[0])
# # print(s[0])  # This gives an error because sets are unordered, so accessing element 0 of something without order doesn't make sense.
#
# # Modify individual items in lists using the index.
#
# l[0] = "Smith"
# # t[0] = "Smith"  # This gives an error because tuples are "immutable".
#
# print(l)
# print(t)
#
# # Add to a list by using `.append`
#
# l.append("Jen")
# print(l)
# # Tuples cannot be appended to because they are immutable.
#
# # Add to sets by using `.add`
#
# s.add("Jen")
# print(s)
#
# # Sets can't have the same element twice.
#
# s.add("Bob")
# print(s)
# # -- Difference between two sets --
#
# friends = {"Bob", "Rolf", "Anne"}
# abroad = {"Bob", "Anne"}
#
# # local_friends = ...
# # If there are 3 friends, and 2 are abroad, that means that 1 friend is local.
# # We can easily calculate which names are in `friends` but not in `abroad` by using `.difference`
#
# local = friends.difference(abroad)
# print(local)
#
#
# print(abroad.difference(friends))  # This returns an empty set
#
# # -- Union of two sets --
#
# local = {"Rolf"}
# abroad = {"Bob", "Anne"}
#
# # friends = ...
# # If we have 1 local friend and 2 abroad friends, we could calculate the total friends by using `.union`
#
# friends = local.union(abroad)
# print(friends)
#
# # -- Intersection of two sets --
#
# art = {"Bob", "Jen", "Rolf", "Charlie"}
# science = {"Bob", "Jen", "Adam", "Anne"}
#
# # Given these two sets of students, we can calculate those who do both art and science by using `.intersection`
#
# both = art.intersection(science)
# print(both)
#
# friends = ["Rolf", "Bob", "Jen"]
# print("Jen" in friends)
#
# # --
#
# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter something you've watched recently: ")
#
# print(user_movie in movies_watched)
#
# The `in` keyword works in most sequences like lists, tuples, and sets.
#
# movies_watched = {"The Matrix", "Green Book", "Her"}
# me = input('i am wathc:')
# if me in movies_watched:
#     print('zbs')
#
#
#
# day_of_week = input("What day of the week is it today? ")
#
# if day_of_week == "Monday":
#     print("Have a great start to your week!")
# elif day_of_week == "Friday":
#     print("It's ok to finish a bit early!")
# else:
#     print("Full speed ahead!")
#
# # -- Problem: user not entering what we expect --
#
# day_of_week = input("What day of the week is it today? ").lower()
#
# if day_of_week == "monday":
#     print("Have a great start to your week!")
# elif day_of_week == "friday":
#     print("It's ok to finish a bit early!")
# else:
#     print("Full speed ahead!")
#
# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter something you've watched recently: ")
#
# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too!")
# else:
#     print("I haven't watched that yet.")
#
# # --
#
# number = 7
# user_input = input("Enter 'y' if you would like to play: ")
#
# if user_input in ("y", "Y"):
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#     elif number - user_number in (1, -1):
#         print("You were off by 1.")
#     else:
#         print("Sorry, it's wrong!")
#
# # --
#
# # We could also do a transformation instead of checking multiple options.
#
# number = 7
# user_input = input("Enter 'y' if you would like to play: ")
#
# if user_input.lower() == "y":
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1:
#         print("You were off by 1.")
#     else:
#         print("Sorry, it's wrong!")
#
#
# numbers = [1, 3, 5]
# squares = [x * 2 for x in numbers]
# print (squares)
#
# # -- Dealing with strings --
#
# friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# starts_s = []
#
# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)
#
# print(starts_s)
#
#
# # -- Can make a new list of friends whose name starts with S --
#
# friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# starts_s = [friend*2 for friend in friends if friend.startswith("S")]
#
# print(starts_s)
#
# # -- List comprehension creates a _new_ list --
#
# friends = ["Sam", "Samantha", "Saurabh"]
# starts_s = [friend for friend in friends if friend.startswith("S")]  # same as above
#
# print(friends)
# print(starts_s)
# print(friends is starts_s)
# print("friends: ", id(friends), " starts_s: ", id(starts_s))
#
# friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
#
# friend_ages["Bob"] = 20
#
# print(friend_ages)  # {'Rolf': 24, 'Adam': 30, 'Anne': 27, 'Bob': 20}
# print(friend_ages["Bob"])
#
# # -- List of dictionaries --
#
# friends = [
#     {"name": "Rolf Smith", "age": 24},
#     {"name": "Adam Wool", "age": 30},
#     {"name": "Anne Pun", "age": 27},
# ]
#
# print(friends)
#
# # -- Iteration --
#
# student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
#
# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")

# # Better
#
# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")
#
# # -- Using the `in` keyword --
#
#json = {"bomonque": [{"iu": [{"iu-1": []}, {"iu10": [{"cozers": ["Zversky", "GoldGem", "Cnya176"]}]}]},
#                      {"fn": [{"fn-12": [{"obercozers": [], "cozers": ["Ivanov", "Petrov"]}]}]}]}
# 
# for bomonqu  in json:
#     for grup in json[bomonqu]:
#         for iu in grup:
#             for kaf in grup[iu]:
#                 for kaf2 in kaf:
#                     # print(f'{kaf[kaf2]}')
#                     for cors in kaf[kaf2]:
#                         # print(f'{cors}')
#                         for cozerogis in cors:
#                             # print(f'{cors[cozerogis]}')
#                             # for peple in cozerogis:
#                             for peple in cors[cozerogis]:
#                                 print(peple)



# if "Bob" in student_attendance:
#     print(f"Bob: {student_attendance[student]}")
# else:
#     print("Bob isn't a student in this class!")
#
# # -- Calculate an average with `.values()` --
#
# attendace_values = student_attendance.values()
# print(sum(attendace_values) / len(attendace_values))
# x, y = 5, 11
#
# # x, y = (5, 11)
#
# # -- Destructuring in for loops --
#
# student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
#
# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")
#
#
# -- Another example --
#
# people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
#
# for name, age, profession in people:
#     print(f"Name: {name}, Age: {age}, Profession: {profession}")
#
#
# # -- Much better than this! --
#
# for person in people:
#     print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")
#
#
# # -- Ignoring values with underscore --
#
# person = ("Bob", 42, "Mechanic")
# name, _, profession = person
#
# print(name, profession)  # Bob Mechanic
#
#
# # -- Collecting values --
#
# head, *tail = [1, 2, 3, 4, 5]
#
# print(head)  # 1
# print(tail)  # [2, 3, 4, 5]
#
#
# *head, tail = [1, 2, 3, 4, 5]
#
# print(head)  # [1, 2, 3, 4]
# print(tail)  # 5
#
#
# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total = total * arg
#
#     return total
#
#
# print(multiply(3, 5))
# print(multiply(-1))
#
# # The asterisk takes all the arguments and packs them into a tuple.
# # The asterisk can be used to unpack sequences into arguments too!
#
#
# def add(x, y):
#     return x + y
#
#
# nums = [3, 5]
# print(add(*nums))  # instead of add(nums[0], nums[1])
#
# # -- Uses with keyword arguments --
# # Double asterisk packs or unpacks keyword arguments
#
#
# def add(x, y):
#     return x + y
#
#
# nums = {"x": 15, "y": 25}
#
# print(add(**nums))
#
# # -- Forced named parameter --
#
#
# def multiply(*args):
#     total = 1
#     for arg in args:
#         total = total * arg
#
#     return total
#
#
# def apply(*args, operator):
#     if operator == "*":
#         return multiply(args)
#     elif operator == "+":
#         return sum(args)
#     else:
#         return "No valid operator provided to apply()."
#
#
# print(apply(1, 3, 6, 7, operator="+"))
# print(apply(1, 3, 5, "+"))  # Error
# # -- Unpacking kwargs --
# def named(**kwargs):
#     print(kwargs)
#
#
# named(name="Bob", age=25)
# # named({"name": "Bob", "age": 25})  # Error, the dictionary is actually a positional argument.
#
# # Unpack dict into arguments. This is OK, but slightly more confusing. Good when working with variables though.
# named(**{"name": "Bob", "age": 25})
#
#
# # -- Unpacking and repacking --
# def named(**kwargs):
#     print(kwargs)
#
#
# def print_nicely(**kwargs):
#     named(**kwargs)  # Unpack the dictionary into keyword arguments.
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")
#
#
# print_nicely(name="Bob", age=25)
#
#
# # -- Both args and kwargs --
#
#
# def both(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# both(1, 3, 5, name="Bob", age=25)
#
# # This is normally used to accept an unlimited number of arguments and keyword arguments, such that some of them can be passed onto other functions.
# # You'll frequently see things like these in Python code:
#
# """
# def post(url, data=None, json=None, **kwargs):
#     return request('post', url, data=data, json=json, **kwargs)
# """
#
# # While the implementation is irrelevant at this stage, what it allows is for the caller of `post()` to pass arguments to `request()`.
#
# # -- Error when unpacking --
#
#
# def myfunction(**kwargs):
#     print(kwargs)
#
#
# myfunction(**"Bob")  # Error, must be mapping
# myfunction(**None)  # Error
#
#
# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}
#
#
# def average(sequence):
#     return sum(sequence) / len(sequence)
#
#
# print(average(student["grades"]))
#
#
# # But wouldn't it be nice if we could...
# # print(student.average()) ?
#
#
# class Student:
#     def __init__(self):
#         self.name = "Rolf"
#         self.grades = (89, 90, 93, 78, 90)
#
#     def average(self):
#         return sum(self.grades) / len(self.grades)
#
#
# student = Student()
# print(student.average())
#
#
# # Identical to Student.average(student)
#
#
# # -- Parameters in __init__ --
#
#
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#     def average(self):
#         return sum(self.grades) / len(self.grades)
#
#
# student = Student("Bob", (36, 67, 90, 100, 100))
# print(student.average())
#
#
# # -- Remember *args ? --
#
#
# class Student:
#     def __init__(self, name, *grades):
#         self.name = name
#         self.grades = grades
#
#     def average(self):
#         return sum(self.grades) / len(self.grades)
#
#
# student = Student("Bob", 36, 67, 90, 100, 100)
# print(student.average())
#
#
