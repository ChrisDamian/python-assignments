class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # Encapsulated attribute

    def get_storage(self):
        return self.__storage

    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def __str__(self):
        return f"{self.brand} {self.model} with {self.__storage}GB storage"
    

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")    
    
# Create instances of Smartphone
my_phone = Smartphone("Apple", "iPhone 14", 128)
print(my_phone)  # Output: Apple iPhone 14 with 128GB storage
print(my_phone.call("123-456-7890"))  # Output: Calling 123-456-7890 from Apple iPhone 14...

# Create instances of Car and Plane
my_car = Car()
my_plane = Plane()

# Demonstrate polymorphism
vehicles = [my_car, my_plane]
for vehicle in vehicles:
    print(vehicle.move())  # Output: Driving 🚗 and Flying ✈️
