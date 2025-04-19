# Refactorizado aplicando SOLID
import pandas as pd
from io import BytesIO

class ExcelLoader:
    def __init__(self, file: bytes):
        self.file = file

    def load_data(self) -> pd.DataFrame:
        return pd.read_excel(BytesIO(self.file))
