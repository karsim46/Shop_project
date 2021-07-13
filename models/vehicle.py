class Vehicle:

    def __init__(self, description, engine, gearbox, colour, price, year, quantity, for_sale, manufacturer, make, id = None, ):
        
        self.description = description
        self.engine = engine
        self.gearbox = gearbox
        self.colour = colour
        self.price = price
        self.year = year
        self.quantity = quantity
        self.for_sale = for_sale
        self.manufacturer = manufacturer
        self.make = make
        self.id = id

    def display_name(self):
        return f"{self.make} {self.description}"
    #do i need to pull in Manufacturer class?