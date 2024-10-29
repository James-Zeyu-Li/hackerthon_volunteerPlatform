from service.areaService import AreaService
from service.areaDataHelper import AreaDatabaseHelper
from controller.areaController import AreaController


def main():
    helper = AreaDatabaseHelper()
    area_service = AreaService(helper)
    area_controller = AreaController(area_service)

    area_service.create_mock_area()

    area = area_controller.select_area(1)
    if area:
        area_controller.display_area_details(area)
    else:
        print("Area not found")


if __name__ == "__main__":
    main()
