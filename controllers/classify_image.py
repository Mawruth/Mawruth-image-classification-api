from initializers import app
from model import classifyImage,imagePreprocessing
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import io

@app.post('/api/v1/classify-image')
async def classifyImageHandler(image: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await image.read()))

        image = imagePreprocessing(image)

        result = classifyImage(image)

        return JSONResponse(content={"result": result})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
