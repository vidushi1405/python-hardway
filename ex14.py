#EXERCISE 14
from sys import argv
script,user_name=argv
prompt=">"

print(f"hi{user_name},im the {script}script.")
print("I'd like to ask you a few questions")
print(f"do u like me{user_name}?")
likes=input(prompt)

print(f"where do you live{user_name}?")
lives=input(prompt)

print("what kind of computer do u like?")
computer=input(prompt)

print(f""" we ahve seen "{likes}about liking me.
      you live in {lives}.and you have a {computer} computer.""")