# main.py
from service.areaService import AreaService
from service.areaDataHelper import AreaDatabaseHelper
from controller.areaController import AreaController
from view.pageMenu import MultiLayerMenu


def main():
    helper = AreaDatabaseHelper()
    area_service = AreaService(helper)
    area_controller = AreaController(area_service)

    area_service.create_mock_areas()

    menu = MultiLayerMenu(area_controller)
    menu.main_menu()


if __name__ == "__main__":
    main()
