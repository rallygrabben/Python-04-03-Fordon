# klass som ärver fordon

class lastbil: 
    # constructor
    def __init__(self, fabrikat, color, flakvolym):
        self.fabrikat = fabrikat
        self.color = color
        self.flakvolym = flakvolym

    # Metoder
    def set_flakvolym(self, flakvolym):
        self.flakvolym = flakvolym

    def get_flakvolym(self):
        return self.flakvolym

    