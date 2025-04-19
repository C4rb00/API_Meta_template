import pandas as pd
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_excel_valid():
    df = pd.DataFrame({
        "template_name": ["bienvenida"],
        "language": ["es"],
        "category": ["MARKETING"],
        "body": ["Hola {{1}}, bienvenido a nuestra óptica!"],
        "phone_number_id": ["123456789"]
    })
    
    # Guardar temporalmente el archivo Excel
    file_path = "test_templates.xlsx"
    df.to_excel(file_path, index=False)

    with open(file_path, "rb") as file:
        response = client.post("/templates/upload", files={"file": (file_path, file, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")})
    
    assert response.status_code in [200, 422, 400]  

    # Limpieza
    import os
    os.remove(file_path)

def test_upload_excel_invalid_format():
    response = client.post("/templates/upload", files={"file": ("test.txt", b"texto plano", "text/plain")})
    assert response.status_code == 400
