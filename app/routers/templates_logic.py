from fastapi import APIRouter, UploadFile, File, HTTPException

class TemplatesRouter:
    def __init__(self):
        self.router = APIRouter()

        @self.router.post("/upload")
        async def upload_excel(file: UploadFile = File(...)):
            if not file.filename.endswith(".xlsx"):
                raise HTTPException(status_code=422, detail="Invalid file format")
            return {"filename": file.filename}
