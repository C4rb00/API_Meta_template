from pathlib import Path
from typing import List, Dict
import pandas as pd
from fastapi import HTTPException

class Validator:
    def validate(self, df: pd.DataFrame) -> List[Dict]:
        raise NotImplementedError("Each validator must implement the validate method.")


class EmptyFieldValidator(Validator):
    def __init__(self, required_fields: List[str]):
        self.required_fields = required_fields

    def validate(self, df: pd.DataFrame) -> List[Dict]:
        errors = []
        for field in self.required_fields:
            missing = df[df[field].isnull()]
            for idx in missing.index:
                errors.append({
                    "row": int(idx + 2),  # +2 to match Excel row number
                    "column": field,
                    "message": f"{field} is required."
                })
        return errors


from typing import List, Dict, Any

class TemplateValidator:
    def __init__(self, validators: List):
        self.validators = validators

    def validate(self, data: Dict[str, Any]) -> bool:
        errors = []

        for validator in self.validators:
            result = validator.validate(data)
            if result is not True:
                errors.append(result)

        if errors:
            raise HTTPException(status_code=422, detail=errors)

        return True

# Archivo validado según principios SOLID. ¿Deseas que continúe con meta_templates.py?
import os
if os.path.exists('/mnt/data'):
    os.listdir('/mnt/data')
