from pydantic import BaseModel
from pydantic_yaml import parse_yaml_raw_as

from core.enums.references import ReferenceType


class DatabaseConfig(BaseModel):
    path: str
    sheet_name: str


class TemplatesConfig(BaseModel):
    references: dict[ReferenceType, str]


class Config(BaseModel):
    database: DatabaseConfig
    templates: TemplatesConfig

    @staticmethod
    def load(path: str) -> 'Config':
        with open(path, 'r') as file:
            return parse_yaml_raw_as(Config, file.read())
