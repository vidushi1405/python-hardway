# EXERCISE 42
# animal is-a object.
class animal():
  pass
#dog is-a animal
class dog(animal):
  def __init__(self,name): 
    #self.name has-a name
    self.name=name


  def count_letters(self):
      return len(self.name)
my_dog=dog("tuffy")  
print(my_dog.count_letters())  


#cat is-a animal
class cat(animal):
  def __init__(self,name): 
    #self.name has-a name
    self.name=name

  def count_letters(self):
        return len(self.name)

my_cat = cat("Garfunkel")

print(my_cat.count_letters())


# person is-a object
class person():
  def __init__(self,name): 
    #self.name has-a name
    self.name=name
    self.pet=None
    

  def count_words(self):
    return len(self.name)
  
my_person=person("ramu prasad baba")
print(my_person.count_words())  


    

# employee is-a person    
class employee(person):
  def __init__(self,name,salary): 
    #employee has-a name
    super().__init__(name)
    #self.salary has-a salary
    self.salary=salary
# fish is-a object
class fish():
  pass
#sailfish is-a fish
class sailfish(fish):
  pass
#shark is-a fish
class shark(fish):
  pass

#rover is-a dog
rover = dog("Rover") 
     
   
#shasha is-a cat
sasha=cat("Sasha") 
#mary is-a person
mary=person("Mary") 
#mary has-a pet sasha
mary.pet=sasha
#fred is-a employee
fred=employee("fred",120000)
#fred has-a pet rover
fred.pet=rover 
#flipper is-a fish
flipper=fish()
#crouse is-a sailfish
crouse=sailfish()
#casey is-a shark
casey=shark() 