import pytest
from calculadora import soma, subtracao, multiplicacao, divisao

def test_soma():
    assert soma(5, 5) == 10
    assert soma(-1, 1) == 0

def test_subtracao():
    assert subtracao(10, 5) == 5
    assert subtracao(0, 5) == -5

def test_multiplicacao():
    assert multiplicacao(3, 5) == 15
    assert multiplicacao(4, 0) == 0

def test_divisao():
    assert divisao(10, 2) == 5
    assert divisao(5, 2) == 2.5

def test_divisao_por_zero():
    with pytest.raises(ValueError, match="Divisão por zero não é permitida."):
        divisao(10, 0)
