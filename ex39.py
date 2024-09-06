#EXERCISE 39
states={
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

#create a basic set of states and some cities in them
cities={
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

#add some more cities
cities['NY']='New York'
cities['OR']='Portland'
#print out some cities 
print("NY state has:cities['NY']")
print("OR state has:cities['OR']")

#print some states
print('-'*10)
print("Michigan's abbreviation is:",states['Michigan'])
print("Florida's abbreviation is:",states['Florida'])

#do it by using the state then cities dict
print('-'*10)
print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])

#print every state abbreviation
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-'* 10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev}has the city{city}")

#now do both at same time
print('-'* 10)
for state,abbrev in list(states.items()):
    print(f"{state}state is abbreviated{abbrev}")
    print(f"and has {cities[abbrev]}")

print('-'* 10)
state=states.get('texas')
if not state:
   print("sorry,no taxes.") 

city=cities.get('TX','doesnt exist')
print(f"the city for state 'TX'is:{city}")        
                            
