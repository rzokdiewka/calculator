from typing import Any

from fastapi import FastAPI

from controller import CalculationContext
from models import Operation

app = FastAPI()


@app.post("/calculate")
async def calculate(operation: Operation) -> dict[str, Any]:
    context = CalculationContext(operators=operation.operators, values=operation.operands)
    return {"result": context.make_calculation()}