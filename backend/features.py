from controller import CalculationContext


def make_complex_calculation(context: CalculationContext) -> float:
    indexes_of_first_operations = [i for i, value in enumerate(context.operators) if value == "*" or value == "/"]
    for i in indexes_of_first_operations:
        cs = context.select_strategy(context.operators[i])
        result = cs.calculate(context.values[i:i + 2])
        context.operators[i] = None
        context.values[i] = None
        context.values[i + 1] = result

    context.operators = [i for i in context.operators if i != None]
    context.values = [i for i in context.values if i != None]

    left_operations = context.operators
    for i in range(len(left_operations)):
        if not left_operations[i]:
            del context.operators[i]
            del context.values[i]
        cs = context.select_strategy(context.operators[i])
        result = cs.calculate(context.values)
        if i < len(left_operations):
            context.values.pop(0)
        context.values[0] = result
    return result


if __name__ == "__main__":
    result = make_complex_calculation(CalculationContext(["-", "*", "-", "/"], [1, 2, 3, 4, 2]))
    print("Result:", result)