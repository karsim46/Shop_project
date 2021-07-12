class Manufacturer:
    def __init__(self, make, model, id = None):
        self.make = make
        self.model = model
        self.id = id

    def full_name(self):
        return f"{self.make} {self.model}"