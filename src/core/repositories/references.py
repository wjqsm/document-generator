from docxtpl import DocxTemplate

from core.enums.references import ReferenceType


class ReferencesRepository:
    def __init__(self, templates: dict[ReferenceType, DocxTemplate]):
        self._templates = templates

    def get_undeclared_vars(self, ref_type: ReferenceType) -> set[str]:
        template = self._templates.get(ref_type)
        return template.get_undeclared_template_variables()

    def generate(
        self,
        data: dict[str, dict[str, str]],
        ref_type: ReferenceType,
    ) -> None:
        for key, value in data.items():
            doc = self._templates.get(ref_type)
            doc.render(value)
            doc.save(key)
