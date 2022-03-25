class Character():
    def __init__(self, real_name, super_name):
        self.name = real_name
        self.super = super_name

    def set_power(self, hero_power):
        self.power = hero_power

    def get_power(self):
        print(self.power)