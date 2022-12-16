from pydantic import BaseModel
from fastapi import Form, File, UploadFile

class UploadForm(BaseModel):
    file: UploadFile
    keyword: str
    neighbors: int

    @classmethod
    def as_form(
        cls,
        keyword: str = Form(),
        neighbors: int = Form(),
        file: UploadFile = File()
    ):
        return cls(
            keyword=keyword,
            neighbors=neighbors,
            file=file
        )