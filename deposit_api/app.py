import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from deposit_api.calc import deposit
from deposit_api.request_data import Data

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": exc.errors()[0]["msg"]},
    )


@app.post("/deposit/")
async def calc_dep(request: Data):
    return deposit(request)


if __name__ == "__main__":
    uvicorn.run("deposit_api.app:app", host="0.0.0.0", port=8000)
