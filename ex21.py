#EXERCISE 21
def add(a,b):
  print(f"adding {a} and {b}")
  return a+b

def substract(a,b):
   print(f"SUBSTRACTING {a} - {b}")
   return a-b

def multiply(a,b):
  print(f"MULTIPLYING {a} * {b}")
  return a*b

def divide(a,b):
  print(f"DIVIDING {a} / {b}")
  return a/b

print("lets do some math with just functions!")

age=add(30,5)
height=substract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print(f"age:{age},height:{height},weight:{weight},iq:{iq}")

print("here is a puzzle")

what=add(age,substract(height,multiply(weight,divide(iq,2))))   
print("that becomes:",what,"can you do it by hand?")