# view/multiLayerMenu.py
class MultiLayerMenu:
    def __init__(self, area_controller):
        self.area_controller = area_controller

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1: Select an area")
            print("2: I want to Help!")
            print("0: Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.select_area_menu()
            elif choice == "2":
                print("Redirecting to Help page... Still under construction.")
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def select_area_menu(self):
        sorted_areas = self.area_controller.get_sorted_areas()

        while True:
            print("\nSelect an Area (sorted by Danger Rate):")
            for idx, area in enumerate(sorted_areas, 1):
                print(
                    f"{idx}: {area.name}, Danger Rate: {area.help_needs.danger_rate}")

            print("0: Go back to Main Menu")

            try:
                choice = int(input("Enter your choice: "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(sorted_areas):
                    selected_area = sorted_areas[choice - 1]
                    self.area_controller.display_area_details(
                        selected_area)
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric choice.")
