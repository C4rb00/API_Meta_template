from fastapi import APIRouter, UploadFile, File, HTTPException
from app.validations.template_validator import TemplateValidator
from io import BytesIO

from app.validations.rules import (
    RequiredFieldsValidator,
    CategoryValidator,
    LanguageValidator,
    BodyPlaceholderValidator
)
from app.services.meta_template_sender import MetaTemplateSender 
import pandas as pd
from app.config import META_TOKEN, BUSINESS_ACCOUNT_ID, GRAPH_API_VERSION

router = APIRouter()

validator = TemplateValidator(validators=[
    RequiredFieldsValidator(),
    CategoryValidator(),
    LanguageValidator(),
    BodyPlaceholderValidator()
])

@router.post("/upload")
async def upload_template_excel(file: UploadFile = File(...)):
    try:
        df = pd.read_excel(BytesIO(file.file.read()))
        file.file.seek(0)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Archivo no válido o formato incorrecto.")

    errores = []
    resultados_meta = []

    sender = MetaTemplateSender(access_token=META_TOKEN, business_account_id=BUSINESS_ACCOUNT_ID, graph_version=GRAPH_API_VERSION)

    for index, row in df.iterrows():
        data = row.to_dict()
        result = validator.validate(data)
        if result is not True:
            errores.append({"fila": index + 2, "error": result})
            continue

        meta_result = sender.send_template(data)
        resultados_meta.append({"fila": index + 2, **meta_result})

    if errores:
        raise HTTPException(status_code=422, detail=errores)

    return {
        "message": "Archivo procesado correctamente.",
        "meta_resultados": resultados_meta
    }
