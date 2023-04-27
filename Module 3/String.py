msg="hello world"
msg2='Hellow World'
msg3="Sad's World"
msg4='sad\'s world'
# print(msg3)
# print(msg4)
# print(msg,msg2)


print(len(msg))
print(msg[0],msg[10])

#generate error string out of range
#print(msg[12]) 

print(msg[:8])
print(msg[0:5]) #between 0 to 5 but not 5

#various method of string objects
print(msg.upper())
print(msg.count('l'))
print(msg.find('world'))
print(msg.find('laxman')) #shall return -1 as laxman isn't present in msg
# msg=msg.replace('world','cotiviti');print(msg)

#concatenate

greeting='Namaste'
name='Ram'
# msg =greeting + name
#msg=greeting +', '+name + '. Welcome!' #keeping track will be difficult

msg='{}, {}. Welcome!'.format(greeting,name)
print(msg)

# for python3 we can use f string
msg=f'{greeting}, {name.upper()}. Welcome!'
print(msg)

#see more information about str methods
#print(help(str))

string = "Hello World"
substring = "World"
if substring in string:
    print("Substring found")
else:
    print("Substring not found")