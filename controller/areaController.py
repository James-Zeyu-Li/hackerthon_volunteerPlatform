from view.areaView import AreaView


class AreaController:
    def __init__(self, area_service):
        self.area_service = area_service
        self.view = AreaView()

    def get_sorted_areas(self):
        areas = self.area_service.get_all_areas()
        return sorted(
            areas,
            key=lambda area: (-area.help_needs.danger_rate, -
                              area.population.homeless)
        )

    def select_area(self, area_id):
        return self.area_service.get_area_by_id(area_id)

    def display_area_details(self, area):
        if not area:
            print("Area not found.")
            return None

        #   Get area details
        population = area.get_population_details()
        infrastructure = area.get_infrastructure_needs()
        weather_impact = area.get_weather_impact()
        resources = area.get_resources_status()
        volunteers = area.get_volunteer_info()
        help_needs = area.help_needs.get_help_needed_info()

        area_details = {
            "area_id": area.area_id,
            "name": area.name,
            "population": population,
            "infrastructure": infrastructure,
            "current_event": weather_impact,
            "resources": resources,
            "volunteers": volunteers,
            "help_needs": help_needs
        }

        self.view.display_area_information(area_details)

        while True:
            print("\nOptions:")
            print("1: Become a Volunteer")
            print("2: Go back to the area list")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.become_volunteer(area)  # become a volunteer
                break  # return to the area list
            elif choice == "2":
                break  # return to the area list
            else:
                print("Invalid choice. Please try again.")

    def become_volunteer(self, area):
        print(
            f"You have chosen to become a volunteer for the area: {area.name}")
