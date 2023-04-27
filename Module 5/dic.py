alien_o={'color':'green','points':5}

print(alien_o['color'])
print(alien_o['points'])
#adding new key-value pair
alien_o['x_pos']=0
alien_o['y_pos']=25
print(alien_o)

#starting with an empty Dic
alien_o={}
alien_o['color'] = 'green'
alien_o['points'] = 5
print(alien_o)

#modifying value in Dic

print(f"the alien is {alien_o['color']}")
alien_o['color']='red'
print(f"the alien is  now  {alien_o['color']}")

#removing key-value pair

del alien_o['points']
print(alien_o)