import pytest
from fastapi import HTTPException
from app.validations.template_validator import TemplateValidator
from app.validations.rules import (
    RequiredFieldsValidator,
    CategoryValidator,
    LanguageValidator,
    BodyPlaceholderValidator
)

# Instancia global del validador
validator = TemplateValidator(validators=[
    RequiredFieldsValidator(),
    CategoryValidator(),
    LanguageValidator(),
    BodyPlaceholderValidator()
])

@pytest.mark.parametrize("template_data,expected", [
    ({
        "template_name": "bienvenida",
        "language": "es",
        "category": "MARKETING",
        "body": "Hola {{1}}, bienvenido a nuestra óptica!",
        "phone_number_id": "123456789"
    }, True),
    ({
        "template_name": "",
        "language": "es",
        "category": "MARKETING",
        "body": "Hola {{1}}, bienvenido a nuestra óptica!",
        "phone_number_id": "123456789"
    }, False),
    ({
        "template_name": "bienvenida",
        "language": "",
        "category": "MARKETING",
        "body": "Hola {{1}}, bienvenido a nuestra óptica!",
        "phone_number_id": "123456789"
    }, False),
    ({
        "template_name": "bienvenida",
        "language": "es",
        "category": "DESCONOCIDO",
        "body": "Hola {{1}}, bienvenido a nuestra óptica!",
        "phone_number_id": "123456789"
    }, False)
])
def test_validate_template(template_data, expected):
    if expected:
        assert validator.validate(template_data) is True
    else:
        with pytest.raises(HTTPException):
            validator.validate(template_data)


