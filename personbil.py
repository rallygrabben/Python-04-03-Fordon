# klass som ärver fordon

class personbil: 
    # constructor
    def __init__(self, fabrikat, color, bagagevolym):
        self.fabrikat = fabrikat
        self.color = color
        self.bagagevolym = bagagevolym

    # Metoder
    def set_bagagevolym(self, bagagevolym):
        self.bagagevolym = bagagevolym

    def get_bagagevolym(self):
        return self.bagagevolym

    def print_fordon(self):
        print(f"\n\t{self.fabrikat} \t\nFärg: {self.color} \t\nBagagevolym: {self.bagagevolym}")