import Laboratorio6;
import pytest;
from unittest import mock
# from unittest.mock import patch

modulo = Laboratorio6

def test_convertir_1():  
    opcion = '2'
    numero = '7'
    with mock.patch('builtins.input', side_effect = [opcion, numero]):
        assert modulo.convertirBase() == 111
        
def test_convertir_2():  
    opcion = '3'
    numero = '7'
    with mock.patch('builtins.input', side_effect = [opcion, numero]):
        assert modulo.convertirBase() == 21

def test_convertir_3():  
    opcion = '5'
    numero = '7000'
    with mock.patch('builtins.input', side_effect = [opcion, numero]):
        assert modulo.convertirBase() == '1B58'
        
def test_convertir_4():  
    opcion = '6'
    numero = '1B58'
    with mock.patch('builtins.input', side_effect = [opcion, numero]):
        assert modulo.convertirBase() == 7000
        
def test_convertir_5():  
    opcion = '8'
    numero = '21'
    with mock.patch('builtins.input', side_effect = [opcion, numero]):
        assert modulo.convertirBase() == 7
