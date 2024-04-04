from pydantic import BaseModel


class Operation(BaseModel):
    operators: list[str] = []
    operands: list[float] = []
