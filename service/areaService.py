# area_service.py

from model.area import Area
from model.population import Population
from model.Infrastructure import InfrastructureStatus
from model.event import CurrentEvent
from model.resource import ResourceStatus
from model.volunteer import VolunteerTeam
from model.helpNeeded import HelpNeeds
# from service import AreaDatabaseHelper


class AreaService:
    def __init__(self, database_helper):
        self.database_helper = database_helper

    def create_mock_areas(self):
        areas = [
            Area(
                area_id=1,
                name="Downtown",
                population=Population(
                    total=100000, old_homes=1500, homeless=300, apartments=20000, houses=5000),
                infrastructure=InfrastructureStatus(
                    "Old", 10, "Needs Renewal", "Stable"),
                current_event=CurrentEvent(
                    "Flood Warning", "High", 70.0, "Main St closed"),
                resources=[
                    ResourceStatus("Water", 100, "Available"),
                    ResourceStatus("Electricity", 50, "Limited")
                ],
                volunteer_teams=[
                    VolunteerTeam(1, "Active", 10),
                    VolunteerTeam(2, "Recruiting", 5)
                ],
                help_needs=HelpNeeds(30.0, 10.0, 3.0, 15.0, 80.0, "", 50)
            ),
            Area(
                area_id=2,
                name="Uptown",
                population=Population(
                    total=50000, old_homes=1000, homeless=150, apartments=5000, houses=2000),
                infrastructure=InfrastructureStatus(
                    "Moderate", 5, "Stable", "Needs Update"),
                current_event=CurrentEvent(
                    "Earthquake", "High", 85.0, "Uptown Rd closed"),
                resources=[
                    ResourceStatus("Water", 80, "Limited"),
                    ResourceStatus("Electricity", 30, "Critical")
                ],
                volunteer_teams=[
                    VolunteerTeam(3, "Active", 7),
                    VolunteerTeam(4, "Standby", 5)
                ],
                help_needs=HelpNeeds(25.0, 8.0, 4.0, 10.0, 70.0, "", 30)
            ),
            Area(
                area_id=3,
                name="Suburb",
                population=Population(
                    total=20000, old_homes=500, homeless=50, apartments=1000, houses=500),
                infrastructure=InfrastructureStatus(
                    "New", 3, "Good", "Stable"),
                current_event=CurrentEvent(
                    "Fire Warning", "Low", 10.0, "None"),
                resources=[
                    ResourceStatus("Water", 200, "Plenty"),
                    ResourceStatus("Electricity", 100, "Stable")
                ],
                volunteer_teams=[
                    VolunteerTeam(5, "Active", 8)
                ],
                help_needs=HelpNeeds(15.0, 5.0, 2.0, 20.0, 90.0, "", 10)
            )
        ]
        for area in areas:
            area.help_needs.calculate_danger_rate(
                area.current_event)  # weather
            self.database_helper.insert_area(area)

    def get_area_by_id(self, area_id):
        return self.database_helper.get_area(area_id)

    def get_all_areas(self):
        return self.database_helper.get_all_areas()
