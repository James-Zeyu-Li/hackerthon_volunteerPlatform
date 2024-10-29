# database_helper.py

# from model import Area

class AreaDatabaseHelper:
    def __init__(self):
        self.database = {}

    def insert_area(self, area):
        self.database[area.area_id] = area

    def get_area(self, area_id):
        return self.database.get(area_id)

    def get_all_areas(self):
        return list(self.database.values())
