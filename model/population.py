class Population:
    def __init__(self, total, old_homes, homeless, apartments, houses):
        self.total = total
        self.old_homes = old_homes
        self.homeless = homeless
        self.apartments = apartments
        self.houses = houses

    def get_old_homes_percentage(self):
        """% of prople in old homes"""
        return (self.old_homes / self.total) * 100 if self.total > 0 else 0
