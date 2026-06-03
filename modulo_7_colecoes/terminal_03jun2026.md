>>> numeros
[0, 6, -1, 10, 99, 17]
>>> dir(numeros)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(numeros.sort)

>>> 


>>> numeros.sort()
>>> numeros
[-1, 0, 6, 10, 17, 99]
>>> numeros = [0, 6, -1, 10, 99, 17]
>>> numeros
[0, 6, -1, 10, 99, 17]
>>> sorted(numeros)
[-1, 0, 6, 10, 17, 99]
>>> numeros
[0, 6, -1, 10, 99, 17]
>>> help(numeros.sort)

>>> numeros.sort()
KeyboardInterrupt
>>> 

>>> numeros
[0, 6, -1, 10, 99, 17]
>>> numeros.sort(reverse=True)
>>> numeros
[99, 17, 10, 6, 0, -1]
>>> numeros.sort()
>>> numeros
[-1, 0, 6, 10, 17, 99]
>>> help(sorted)

>>> 





>>> numeros = [0, 6, -1, 10, 99, 17]
>>> numeros
[0, 6, -1, 10, 99, 17]
>>> sorted(numeros, reverse=True)
[99, 17, 10, 6, 0, -1]
>>> 










>>> nomes = ['Lucas', 'Sara', 'Fco Neto', 'Samuel', 'Maurício', 'Antonio']
>>> nomes
['Lucas', 'Sara', 'Fco Neto', 'Samuel', 'Maurício', 'Antonio']
>>> sorted(nomes)
['Antonio', 'Fco Neto', 'Lucas', 'Maurício', 'Samuel', 'Sara']
>>> sorted(nomes, key=len)
['Sara', 'Lucas', 'Samuel', 'Antonio', 'Fco Neto', 'Maurício']
>>> sorted(nomes, key=len, reverse=True)
['Fco Neto', 'Maurício', 'Antonio', 'Samuel', 'Lucas', 'Sara']
>>> 






>>> sorted(nomes, key=len)
['Sara', 'Lucas', 'Samuel', 'Antonio', 'Fco Neto', 'Maurício']
>>> def ultima_letra(nome):
...     return nome[len(nome) - 1]
...     
>>> ultima_letra('sara')
'a'
>>> sorted(nomes, key=ultima_letra)
['Sara', 'Samuel', 'Fco Neto', 'Maurício', 'Antonio', 'Lucas']
>>> 






>>> carro = {'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 1\
20000}
>>> carro
{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000}
>>> carros = []
>>> carros
[]
>>> carros.append(carro)
>>> carros
[{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000}]
>>> 





>>> carro
{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000}
>>> carro['id'] = 100
>>> carro
{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}
>>> 









>>> carros
[{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}]
>>> carros[0]
{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}
>>> carros[0]['id']
100
>>> carros[0]['ano']
2027
>>> 





>>> byd = ['id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000]
  File "<python-input-42>", line 1
    byd = ['id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000]
               ^
SyntaxError: invalid syntax
>>> byd = {'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000}
>>> byd
{'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000}
>>> carros
[{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}]
>>> 




>>> carros.append(byd)
>>> 














>>> len(carros)
2
>>> carros
[{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}, {'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000}]
>>> carros[0]
{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}
>>> carros[1]
{'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000}
>>> carros[1]['nome']
'Seal'
>>> carros[0]['nome']
'Novo Corsa'
>>> 

>>> samuel_car = {'id': 99, 'nome': 'Bentley Continental', 'cor': 'azul', ''
valor': 2000000}
>>> samuel_car = {'id': 99, 'nome': 'Bentley Continental', 'cor': 'azul', '\
valor': 2000000*5}
>>> carros.append(samuel_car)
>>> 










>>> carros
[{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}, {'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000}, {'id': 99, 'nome': 'Bentley Continental', 'cor': 'azul', 'valor': 10000000}]
>>> len(carros)
3
>>> for carro in carros:
...     print(carro['nome'], carro['valor'])
...     
Novo Corsa 120000
Seal 280000
Bentley Continental 10000000
>>> 



>>> for i in range(len(carros)):
...     print(i, carros[i]['nome'], carros[i]['cor'])
...     
0 Novo Corsa branco
Traceback (most recent call last):
  File "<python-input-59>", line 2, in <module>
    print(i, carros[i]['nome'], carros[i]['cor'])
                                ~~~~~~~~~^^^^^^^
KeyError: 'cor'
>>> carros[1]
{'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000}
>>> carros[1]['cor'] = 'azul'
>>> 



>>> for i in range(len(carros)):
...     print(i, carros[i]['nome'], carros[i]['cor'])
...     
0 Novo Corsa branco
1 Seal azul
2 Bentley Continental azul
>>> carros
[{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}, {'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000, 'cor': 'azul'}, {'id': 99, 'nome': 'Bentley Continental', 'cor': 'azul', 'valor': 10000000}]
>>> 




>>> for carro in carros:
...     print(carro)
...     
{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}
{'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000, 'cor': 'azul'}
{'id': 99, 'nome': 'Bentley Continental', 'cor': 'azul', 'valor': 10000000}
>>> carros_ordenados = sorted(carros)
Traceback (most recent call last):
  File "<python-input-65>", line 1, in <module>
    carros_ordenados = sorted(carros)
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> 



>>> def obter_nome_carro(carro):
...     return carro['nome']
...     
>>> carros_ordenados = sorted(carros, key=obter_nome_carro)
>>> carros_ordenados
[{'id': 99, 'nome': 'Bentley Continental', 'cor': 'azul', 'valor': 10000000}, {'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}, {'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000, 'cor': 'azul'}]
>>> 
>>> def get_valor(carro):
...     return carro['valor']
...     
>>> carros_ordenados = sorted(carros, key=get_valor)
>>> carros_ordenados
[{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}, {'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000, 'cor': 'azul'}, {'id': 99, 'nome': 'Bentley Continental', 'cor': 'azul', 'valor': 10000000}]
>>> carros_ordenados = sorted(carros, key=get_valor, reverse=True)
>>> carros_ordenados
[{'id': 99, 'nome': 'Bentley Continental', 'cor': 'azul', 'valor': 10000000}, {'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000, 'cor': 'azul'}, {'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}]
>>> 
>>> 
>>> carros_ordenados = sorted(carros, key=lambda c:c[], reverse=True)
  File "<python-input-76>", line 1
    carros_ordenados = sorted(carros, key=lambda c:c[], reverse=True)
                                                     ^
SyntaxError: invalid syntax
>>> carros_ordenados = sorted(carros, key=lambda c:c['cor'], reverse=True)
>>> carros_ordenados
[{'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}, {'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000, 'cor': 'azul'}, {'id': 99, 'nome': 'Bentley Continental', 'cor': 'azul', 'valor': 10000000}]
>>> 




>>> def get_tam_nome(carro):
...     return len(carro['carro'])
...     
>>> def get_tam_nome(carro):
...     return len(carro['nome'])
...     
>>> carros_ordenados = sorted(carros, key=get_tam_nome)
>>> carros_ordenados
[{'id': 101, 'nome': 'Seal', 'ano': 2026, 'valor': 280000, 'cor': 'azul'}, {'nome': 'Novo Corsa', 'ano': 2027, 'cor': 'branco', 'valor': 120000, 'id': 100}, {'id': 99, 'nome': 'Bentley Continental', 'cor': 'azul', 'valor': 10000000}]
>>> 