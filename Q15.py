'''
Create a class Appliance with attributes name, brand, power_usage, is_on.
Implement methods:

__str__ to return appliance details.
turn_on() to set is_on = True.
turn_off() to set is_on = False.
show_details() to display all information.
From Appliance, inherit:

SmartLight with an extra attribute brightness_level.
SmartAC with an extra attribute temperature_setting.
'''

class Appliance:
    def __init__(self, name, brand, power_usage, is_on=False):
        self.name = name
        self.brand = brand
        self.power_usage = power_usage
        self.is_on = is_on
    
    def __str__(self):
        return f"Appliance: {self.name}, Brand: {self.brand}, Power Usage: {self.power_usage}W, Status: {'On' if self.is_on else 'Off'}"
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is now ON.")
    
    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is now OFF.")
    
    def show_details(self):
        print(self)

class SmartLight(Appliance):
    def __init__(self, name, brand, power_usage, brightness_level, is_on=False):
        super().__init__(name, brand, power_usage, is_on)
        self.brightness_level = brightness_level
    
    def __str__(self):
        return super().__str__() + f", Brightness Level: {self.brightness_level}"
    
    def show_details(self):
        print(self)

class SmartAC(Appliance):
    def __init__(self, name, brand, power_usage, temperature_setting, is_on=False):
        super().__init__(name, brand, power_usage, is_on)
        self.temperature_setting = temperature_setting
    
    def __str__(self):
        return super().__str__() + f", Temperature Setting: {self.temperature_setting}°C"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    smart_light = SmartLight("Living Room Light", "Philips", 10, 75)
    smart_ac = SmartAC("Bedroom AC", "Samsung", 2000, 22)
    
    smart_light.show_details()
    smart_ac.show_details()
    
    smart_light.turn_on()
    smart_light.show_details()
    
    smart_ac.turn_off()
    smart_ac.show_details()

