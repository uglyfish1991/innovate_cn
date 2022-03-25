from person import Person

liam = Person("Liam", "30","6'7")

#liam is the object, (Liam) is the name we passed through

print(liam)

jordan = Person("Jordan", "27", "4'7")

print(jordan.height)

print(f"Jordan is {jordan.height} tall")

liam.set_hair("brown and curly")

jordan.set_hair("blonde and straight")

print(f"Liam's hair is {liam.hair}, but Jordan's hair is {jordan.hair}")

liam.get_hair()
jordan.get_hair()