class Area:
    def __init__(self, area_id, name, population, infrastructure,
                 current_event, resources, volunteer_teams, help_needs):
        self.area_id = area_id
        self.name = name
        self.population = population  # Population object
        self.infrastructure = infrastructure  # InfrastructureStatus object
        self.current_event = current_event  # CurrentEvent object
        self.resources = resources  # List of ResourceStatus objects
        self.volunteer_teams = volunteer_teams  # List of VolunteerTeam objects
        self.help_needs = help_needs

    def get_population_details(self):
        """
        return population details
        """
        return {
            "old_homes": self.population.old_homes,
            "homeless": self.population.homeless,
            "apartments": self.population.apartments,
            "houses": self.population.houses,
        }

    def get_infrastructure_needs(self):
        """
        return infrastructure needs
        """
        return {
            "house_condition": self.infrastructure.house_condition,
            "shelter_availability": self.infrastructure.shelter_availability,
            "water_pipe_status": self.infrastructure.water_pipe_status,
            "electric_infrastructure":
                self.infrastructure.electric_infrastructure,
        }

    def get_weather_impact(self):
        """
        return the affection rate of the current weather event
        """
        return {
            "event_type": self.current_event.event_type,
            "severity": self.current_event.severity,
            "affection_rate": self.current_event.affection_rate,
            "road_closure_status": self.current_event.road_closure_status,
        }

    def get_resources_status(self):
        """
        return resources status
        """
        return [{"type": res.type, "amount": res.amount, "status": res.status}
                for res in self.resources]

    def get_volunteer_info(self):
        """
        return volunteer teams information
        """
        return [{"team_id": team.team_id, "status": team.status,
                 "members": team.members}
                for team in self.volunteer_teams]

    def get_help_needed_info(self):
        """
        The percentage of old houses, homeless people, shelter coverage,
          resource availability, and danger rate
        """
        return self.help_needs.get_help_needed_info()
