from core.enums.references import ReferenceType
from docxtpl import DocxTemplate


def load_reference_templates(references: dict[ReferenceType, str]) -> dict[ReferenceType, DocxTemplate]:
    return {
        key: DocxTemplate(value)
        for key, value in references.items()
    }
