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

    def create_mock_area(self):
        population = Population(
            total=100000,
            old_homes=1500,
            homeless=300,
            apartments=20000,
            houses=5000
        )

        infrastructure = InfrastructureStatus(
            house_condition="Old",
            shelter_availability=10,
            water_pipe_status="Renewal required",
            electric_infrastructure="Stable",
        )

        current_event = CurrentEvent(
            event_type="Flood Warning",
            severity="High",
            affection_rate=70.0,
            road_closure_status="Deep Cove Road closed"
        )

        resources = [
            ResourceStatus("Water", 100, "Useable"),
            ResourceStatus("Electricity", 50, "Limited")
        ]

        volunteers = [
            VolunteerTeam(1, "Active", 10),
            VolunteerTeam(2, "Recruiting", 5)
        ]

        help_needs = HelpNeeds(
            old_house_rate=30.0,
            population_in_old_houses_rate=10.0,
            homeless_rate=3.0,
            shelter_coverage_rate=15.0,
            resource_availability_rate=80.0,
            weather_event="",  # 初始设为空
            danger_rate=65.0  # 初始危险率
        )

        help_needs.calculate_danger_rate(current_event)

        # Create an Area object
        area = Area(
            area_id=1,
            name="Deep Cove, North Vancouver",
            population=population,
            infrastructure=infrastructure,
            current_event=current_event,
            resources=resources,
            volunteer_teams=volunteers,
            help_needs=help_needs
        )

        self.database_helper.insert_area(area)

    def get_area_by_id(self, area_id):
        return self.database_helper.get_area(area_id)

    def get_all_areas(self):
        return self.database_helper.get_all_areas()
