from abc import ABC, abstractmethod


class CalculationStrategy(ABC):
    @abstractmethod
    def calculate(self, values: list[float]) -> float:
        raise NotImplementedError


class Addition(CalculationStrategy):
    def calculate(self, values: list[float]) -> float:
        return values[0] + values[1]


class Subtraction(CalculationStrategy):
    def calculate(self, values: list[float]) -> float:
        return values[0] - values[1]


class Multiplication(CalculationStrategy):
    def calculate(self, values: list[float]) -> float:
        return values[0] * values[1]


class Division(CalculationStrategy):
    def calculate(self, values: list[float]) -> float:
        return values[0] / values[1]


class CalculationContext:

    def __init__(self, operators: list[str], values: list[float]):
        self.values: list[float] = values
        self.operators: list[str] = operators
        self.calculation_strategy: CalculationStrategy = self.select_strategy(operators[0])

    def set_calculation_strategy(self, operators: list[str]):
        self.calculation_strategy: CalculationStrategy = self.select_strategy(operators[0])

    def make_calculation(self) -> float:
        return self.calculation_strategy.calculate(self.values)

    @staticmethod
    def select_strategy(operator: str) -> CalculationStrategy:
        if operator == "+":
            return Addition()
        elif operator == "-":
            return Subtraction()
        elif operator == "*":
            return Multiplication()
        elif operator == "/":
            return Division()
