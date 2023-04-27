#lambda that accepts one agrument
greeting=lambda name : print('Hey there ,',name)

#lambda call
greeting('Abish')


num=[1,5,4,6,8,11,3,12]

new_list=list(filter(lambda x: (x%2==0), num))
print(new_list)