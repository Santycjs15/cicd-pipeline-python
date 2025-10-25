# app/calculadora.py
"""Módulo calculadora: contiene operaciones aritméticas básicas."""


def sumar(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b


def restar(a: float, b: float) -> float:
    """Resta el segundo número al primero."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Multiplica dos números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Divide el primer número por el segundo.

    Lanza:
        ZeroDivisionError: Si el divisor es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


def potencia(a: float, b: float) -> float:
    """Eleva a a la potencia b."""
    return a**b


def modulo(a: float, b: float) -> float:
    """Resto de la división de a entre b.

    Lanza:
        ZeroDivisionError: Si el divisor es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede calcular el módulo por cero")
    return a % b
