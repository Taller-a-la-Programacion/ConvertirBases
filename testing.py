import Laboratorio6;
import pytest;
from unittest import mock
# from unittest.mock import patch

modulo = Laboratorio6

def test_convertir_1():  
    opcion = '2'
    numero = '7'
    with mock.patch('builtins.input', side_effect = [opcion, valor]):
        assert modulo.convertir() == 111
