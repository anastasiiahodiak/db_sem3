from typing import List

from t08_flask_mysql.app.my_project.auth.service import account_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class AccountController(GeneralController):
    """
    Realization of Account controller.
    """
    _service = account_service
    def find_all(self) -> List[object]:
        """
        Gets all objects from table using Service layer as DTO objects.
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: x.put_into_dto(), self._service.find_all()))
