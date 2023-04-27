#looping through entire list
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
 print(f"{magician.title()}, that was a great trick!")
 print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("------------------------------------")
 #making numerical list
for value in range(1,5):
 print(value)

#using range() to make a list of numbers
#even number
numbers=list(range(2,11,2))
print(numbers)
sqr=[]
for i in range(1,11):
 square=i**2
 sqr.append(square)

print(sqr)

#enumerate
courses=['History','Math','Physics','CompSci']

for index,course in enumerate(courses,start=1):
 print(index,course)

 #using join function to convert list into str

 course_str='-'.join(courses)
 print(course_str)
 