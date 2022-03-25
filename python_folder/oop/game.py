from character import Character

spidey = Character("Peter Parker", "Spiderman")
spidey.set_power("web-slinging")

spidey.get_power()

print(f"{spidey.name} is secretly the superhero {spidey.super}, and his superpower is {spidey.power}" )

hulk = Character("Bruce Banner", "The Incredible Hulk")
hulk.set_power("smashing")

hulk.get_power()


print(f"{hulk.name} is secretly the superhero {hulk.super}, and his superpower is {hulk.power}" )