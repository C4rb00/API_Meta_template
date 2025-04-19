import re

class RequiredFieldsValidator:
    """
    Verifica que todos los campos requeridos estén presentes y no vacíos.
    """
    def __init__(self):
        self.required_fields = ["template_name", "language", "category", "body", "phone_number_id"]

    def validate(self, data):
        missing = [field for field in self.required_fields if not data.get(field)]
        if missing:
            return f"Los siguientes campos son requeridos y están vacíos o ausentes: {', '.join(missing)}"
        return True

    """
    Valida que la categoría esté dentro de las opciones permitidas por Meta.
    """
from typing import Dict, Any

class CategoryValidator:
    ALLOWED_CATEGORIES = ["MARKETING", "TRANSACTIONAL", "OTP", "UTILITY"]

    def validate(self, data: Dict[str, Any]) -> bool:
        category = data.get("category")
        if category not in self.ALLOWED_CATEGORIES:
            return f"Categoría inválida: {category}. Debe ser una de: {', '.join(self.ALLOWED_CATEGORIES)}"
        return True


class LanguageValidator:
    """
    Valida que el código de idioma esté en un formato válido según Meta (ej: es, en, pt_BR).
    """
    def __init__(self):
        self.allowed_languages = [
            "en", "es", "fr", "pt_BR", "de", "it", "ar", "tr", "id", "hi", "zh_CN", "ja", "ko"
        ]

    def validate(self, data):
        language = data.get("language")
        if language and language not in self.allowed_languages:
            return f"Idioma no permitido: {language}. Debe ser uno de: {', '.join(self.allowed_languages)}"
        return True


class BodyPlaceholderValidator:
    """
    Valida que los placeholders en el cuerpo estén en formato correcto ({{1}}, {{2}}, ...).
    """
    def validate(self, data):
        body = data.get("body", "")
        placeholders = re.findall(r"{{\s*\d+\s*}}", body)

        if "{{" in body and not placeholders:
            return "El cuerpo contiene placeholders mal formateados. Usa el formato correcto: {{1}}, {{2}}, etc."

        return True