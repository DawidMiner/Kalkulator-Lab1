from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Konfiguracja CORS (aby frontend mógł gadać z backendem)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Model danych wejściowych
class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operator: str


@app.post("/api/calculate")
def calculate(request: CalculationRequest):
    a = request.num1
    b = request.num2
    op = request.operator

    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        if b == 0:
            raise HTTPException(status_code=400, detail="Nie można dzielić przez zero")
        res = a / b
    else:
        raise HTTPException(status_code=400, detail="Nieznany operator")

    return {"result": res}


# Serwowanie plików statycznych (frontendu) - w produkcji często robi to nginx,
# ale tutaj uprości to deployment na Azure Web App
app.mount("/", StaticFiles(directory="../frontend", html=True), name="static")