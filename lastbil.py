# klass som ärver fordon

class lastbil: 
    # constructor
    def __init__(self, fabrikat, color, flakvolym):
        self.fabrikat = fabrikat
        self.color = color
        self.flakvolym = flakvolym

    # metoder
    def set_flakvolym(self, flakvolym):
        self.flakvolym = flakvolym

    def get_flakvolym(self):
        return self.flakvolym

    def print_fordon(self):
        print(f"\n\t{self.fabrikat} \t\nFärg: {self.color} \t\n Flakvolym: {str(self.flakvolym)}")

