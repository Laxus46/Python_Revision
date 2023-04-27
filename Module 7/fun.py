def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


#returning value

print('Returning a Simple Value')
def get_formatted_name(first_name,last_name):
 full_name=f"{first_name} {last_name}"
 return full_name.title()
musician=get_formatted_name('laxman','Uchiha')
print(musician)


#making an arugment optional

def format_name(first,last,mid=''):

 if mid:
  full=f"{first} {mid} {last}"

 else:
  full=f"{first} {last}"
  
 return full
get_name=format_name('bidha','hero')
print(get_name)
get_name=format_name('a','b','c')
print(get_name)