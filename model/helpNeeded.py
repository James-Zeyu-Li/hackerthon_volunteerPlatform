class HelpNeeds:
    def __init__(self, old_house_rate, population_in_old_houses_rate,
                 homeless_rate,
                 shelter_coverage_rate, resource_availability_rate,
                 weather_event, danger_rate):
        self.old_house_rate = old_house_rate
        self.population_in_old_houses_rate = population_in_old_houses_rate
        self.homeless_rate = homeless_rate
        self.shelter_coverage_rate = shelter_coverage_rate
        self.resource_availability_rate = resource_availability_rate
        self.weather_event = weather_event
        self.danger_rate = danger_rate

    def calculate_danger_rate(self, current_event):
        """
        identify the event type and severity and calculate the danger rate
        """
        base_danger_rate = self.danger_rate
        event_description = self.weather_event

        if current_event.event_type == "Flood Warning" and current_event.severity == "High":
            base_danger_rate += 20.0
            event_description = "Flood warning, Level High, Danger Rate + 20%"
        elif current_event.event_type == "Earthquake" and current_event.severity == "High":
            base_danger_rate += 30.0
            event_description = "Earthquake warning, Level High, Danger Rate + 30%"
        elif current_event.event_type == "Fire Warning" and current_event.severity == "Low":
            base_danger_rate += 5.0
            event_description = "Fire warning, Level Low, Danger Rate + 5%"

        self.danger_rate = base_danger_rate
        self.weather_event = event_description

    def get_help_needed_info(self):
        return {
            "old_house_rate": self.old_house_rate,
            "population_in_old_houses_rate": self.population_in_old_houses_rate,
            "homeless_rate": self.homeless_rate,
            "shelter_coverage_rate": self.shelter_coverage_rate,
            "resource_availability_rate": self.resource_availability_rate,
            "weather_event": self.weather_event,
            "danger_rate": self.danger_rate
        }
