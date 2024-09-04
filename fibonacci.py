# Questão 2
from typing import List


def fibonacci_sequence(limit: int) -> List[int]:
    sequence = [0, 1]
    while sequence[-1] < limit:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence


def is_in_fibonacci(number: int) -> bool:
    sequence = fibonacci_sequence(number)
    if number in sequence:
        print(f"{number} pertence à sequência de Fibonacci.")
        return True
    print(f"{number} não pertence à sequência de Fibonacci.")
    return False


number = int(input(f"Enter a number: "))
is_in_fibonacci(number)
