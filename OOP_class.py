# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"


# Derived class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Use constructor of Device (inheritance)
        super().__init__(brand, model)
        self.storage = storage
        self.__battery = battery   # 🔒 Encapsulation (private attribute)

    # Encapsulation: Getter & Setter
    def get_battery(self):
        return f"{self.__battery}% remaining"
    
    def charge_battery(self, amount):
        self.__battery = min(100, self.__battery + amount)
        return f"🔋 Charged! Battery now at {self.__battery}%"

    # Custom method
    def install_app(self, app_name):
        return f"📱 Installing {app_name} on {self.brand} {self.model}"


# --- Using the class ---
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB", 70)
print(phone1.info())                     # From base class
print(phone1.get_battery())              # Encapsulation
print(phone1.charge_battery(20))         # Charging
print(phone1.install_app("WhatsApp"))    # Custom method
