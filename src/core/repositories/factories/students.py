from core.config import Config
from core.helpers.dataframes import build_from_excel
from core.repositories.students import StudentsRepository


class StudentsRepositoryFactory:
    def __init__(self, config: Config):
        self._config = config

    def __call__(self, identifications_fields: list[str]) -> StudentsRepository:
        file_path = self._config.database.path
        sheet_name = self._config.database.sheet_name
        return StudentsRepository(
            df=build_from_excel(path=file_path, sheet_name=sheet_name),
            identifications_fields=identifications_fields,
        )
