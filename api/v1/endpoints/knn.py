from fastapi import APIRouter, UploadFile
from libraries import helper
from fastapi.responses import FileResponse

router = APIRouter()

@router.post("/train")
@router.post("/train/", include_in_schema=False)
async def training_and_return_mc(keyword: str, neighbors: int, file: UploadFile):
    contents = file.file.read()
    df = helper.file_to_df(contents)
    file.file.close()

    train, test = helper.train_test_split(df, keyword)

    real, predicts = helper.predict(train, test, neighbors)

    helper.create_confusion_matrix(real, predicts)

    return FileResponse("confusion_matrix.png")