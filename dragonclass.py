class Dragon:
    def __init__(self, name, mass, plwt):
        self.name = name
        self.mass = mass
        self.plwt = plwt

    def __str__(self):
        return f"Name: {self.name}  Dry mass: {self.mass} Payload weight: {self.plwt}"

