courses=['History','Math','Physics','CompSci']

print(courses[0])
print(courses[-1])
print(courses[2:])

#append insert item in last of list
courses.append('Art')
print(courses)
#use insert to insert item in any index of list
course2=['Art','Education']
#courses.insert(2,'TOC')
#courses.insert(0,course2)

courses.append(course2)
print(courses)
#removing an item Using del

motorcycles=['honda','yamaha','suzuki']
del motorcycles[0]
print(motorcycles)

print('----------------------------------')

#removing an item using pop()
motorcycles=['honda','yamaha','suzuki']
popped_motorcycles=motorcycles.pop()
print(popped_motorcycles)
print(motorcycles)
print('----------------------------------------------')
motorcycles=['honda','yamaha','suzuki']
popped_motorcycles=motorcycles.pop(1)
print(popped_motorcycles)
print(motorcycles)

print('------------------------------')

#removing an item by value
motorcycles=['honda','yamaha','suzuki','ducati']
x=motorcycles.remove('ducati')
print(x)
print(motorcycles)

print('------------------------------------------')
#sorting a list with sort() method

cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
#in reverse order
cars.sort(reverse=True)
print(cars)
print('-------------------------------------------')
#sort a list with sorted()function
cars=['bmw','audi','toyota','subaru','BMW']
print(sorted(cars))
print(cars)