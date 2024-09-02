#EXERCISE 5
# We have to manage the number in auditorium for orientation program.
chairs=200
space_per_chair=1.0
students = 90
faculties = 10
chairs_occupied = chairs-students+faculties
chairs_vacant = chairs-chairs_occupied
auditorium_capacity = chairs*space_per_chair


print("there are",chairs,"chairs available")
print("there is only",space_per_chair,"space_each")
print("there will be",chairs_occupied,"chairs filled")
print("no.of the empty chairs will be",chairs_vacant)