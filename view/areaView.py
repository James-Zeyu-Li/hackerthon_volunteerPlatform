class AreaView:
    def display_area_information(self, area_details):
        if not area_details:
            print("Area not supported.")
            return

        print(
            f"--- Area: {area_details['name']} (ID: {area_details['area_id']}) ---")

        print("\nPopulation Details:")
        for category, count in area_details["population"].items():
            print(f"  {category}: {count}")

        print("\nInfrastructure Needs:")
        for key, value in area_details["infrastructure"].items():
            print(f"  {key}: {value}")

        print("\nCurrent Weather Event:")
        print(f"  Event: {area_details['current_event']['event_type']}")
        print(f"  Severity: {area_details['current_event']['severity']}")
        print(
            f"  Affection rate: {area_details['current_event']['affection_rate']}%")
        print(
            f"  Road Closure Status: {area_details['current_event']['road_closure_status']}")

        print("\nResource Status:")
        for resource in area_details["resources"]:
            print(
                f"  {resource['type']}: {resource['amount']} ({resource['status']})")

        print("\nVolunteer Teams:")
        for volunteer in area_details["volunteers"]:
            print(
                f"  Team {volunteer['team_id']} - Status: {volunteer['status']}, Members: {volunteer['members']}")

        # Display help needs information
        print("\nHelp Needed Information:")
        help_needs = area_details["help_needs"]
        for key, value in help_needs.items():
            print(f"  {key.replace('_', ' ').capitalize()}: {value}")

        print("\n" + "-"*50 + "\n")
