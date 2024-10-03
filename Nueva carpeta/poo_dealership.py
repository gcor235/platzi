class Car:
        def __init__(self, brand, model, price):
            self.brand = brand
            self.model = model
            self.price = price
            self.is_available = True
   
        def sell(self):
            if self.is_available:
               self.is_available = False
               print(f"El coche {self.brand} {self.model} ha sido vendido.")
            else:
               print(f"El coche {self.brand} {self.model} no está disponible.")

        def cheack_availability(self):
            return self.is_available
#para devolver el valor de la variable
        def get_price(self):
            return self.price
    

class Customer:
        def _init_(self, name):
            self.name = name
            self.cars_purchased = []
            
        def buy_car(self, car):
            if car.cheack_availability():
                car.sell()
                self.cars_purchased.append(car)
            else:
                print(f"lo siento, {car.brand} {car.model} no esta disponible.")
            
        def inquire_car(self, car):
            availability = "disponible" if car.cheack_availability() else "no esta disponible"
            print(f"El coche {car.brand} {car.model} esta {availability} y cuesta {car.price}")
            
class Dealership:
        def _init_(self):
            self.inventory = []
            self.customers = []
            
        def add_car(self, car):
            self.inventory.append(car)
            print(f"El coche {car.brand} {car.model} ha sido añadido al inventario.")

        def register_customer(self, customer):
           self.customer.append(customer)
           print(f"El cliente {customer.name} ha sido registrado en la concesionaria")
        
        def show_available_car(self):
           print("coches disponibles en la concesionaria: ")
           for car in self.inventory:
                if car.cheack_availability():
                   print(f"- {car.brand} {car.model} está disponible por {car.get_price()}")
            
# Crear autos
car1 = Car("Toyota", "Corolla", 20000)
car2 = Car("Honda", "Civic", 22000)
car3 = Car("Ford", "Mustang", 35000)

# Crear cliente
customer1 = Customer("Alexis")

# Crear concesionaria 
dealership = Dealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)
dealership.register_customer(customer1)
                   
# Mostrar autos disponibles
dealership.show_available_car()

#consulta del coche
customer1.inquire_car(car1)

# Comprar auto
customer1.buy_car(car1)

#autos disponibles
dealership.show_available_car()

#compra de auto ya vendido
customer1.buy_car(car1)

# Mostrar autos disponibles después de la compra
