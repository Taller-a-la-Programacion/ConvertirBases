# Convertir Bases Numéricas

## Instrucciones Generales
- El archivo **debe** llamarse **Laboratorio6.py**
- No olvidar los comentarios


- Realice un programa en python similar a convertirdor de temperaturas, pero en este caso a convertir de una base numérica a otra.
- Las opciones a recibir son:
  - 2: Decimal a Base 2
  - 3: Decimal a Base 3
  - 4: Decimal a Base 4
  - 5: Decimal a Hexadecimal
  - 6: Hexadecimal a Decimal
  - 7: Base 2 a Decimal
  - 8: Base 3 a Decimal
  - 9: Base 4 a Decimal

### Restricciones
- El valor para la selección de las opciones será un caracter desde 2 a 9, este puede ser en string o int.
- El valor del numero a convertir deberá ser entero o string en el caso de ser hexadecimal

```python
>>> convertirBase()

===========================
Bienvenido a Convertidor   
===========================
Opciones:
2: Decimal a Base 2
3: Decimal a Base 3
4: Decimal a Base 4
5: Decimal a Hexadecimal
6: Hexadecimal a Decimal
7: Base 2 a Decimal
8: Base 3 a Decimal
9: Base 4 a Decimal
Digite una opción: 2
Digite el valor a convertir: 7
111

>>> convertirBase()
===========================
Bienvenido a Convertidor   
===========================
Opciones:
2: Decimal a Base 2
3: Decimal a Base 3
4: Decimal a Base 4
5: Decimal a Hexadecimal
6: Hexadecimal a Decimal
7: Base 2 a Decimal
8: Base 3 a Decimal
9: Base 4 a Decimal
Digite una opción: 3
Digite el valor a convertir: 7
21

>>> convertirBase()
===========================
Bienvenido a Convertidor   
===========================
Opciones:
2: Decimal a Base 2
3: Decimal a Base 3
4: Decimal a Base 4
5: Decimal a Hexadecimal
6: Hexadecimal a Decimal
7: Base 2 a Decimal
8: Base 3 a Decimal
9: Base 4 a Decimal
Digite una opción: 5
Digite el valor a convertir: 7000
'1B58'

>>> convertirBase()
===========================
Bienvenido a Convertidor   
===========================
Opciones:
2: Decimal a Base 2
3: Decimal a Base 3
4: Decimal a Base 4
5: Decimal a Hexadecimal
6: Hexadecimal a Decimal
7: Base 2 a Decimal
8: Base 3 a Decimal
9: Base 4 a Decimal
Digite una opción: 6
Digite el valor a convertir: 1B58
7000

>>> convertirBase()
===========================
Bienvenido a Convertidor   
===========================
Opciones:
2: Decimal a Base 2
3: Decimal a Base 3
4: Decimal a Base 4
5: Decimal a Hexadecimal
6: Hexadecimal a Decimal
7: Base 2 a Decimal
8: Base 3 a Decimal
9: Base 4 a Decimal
Digite una opción: 8
Digite el valor a convertir: 21
7
```
