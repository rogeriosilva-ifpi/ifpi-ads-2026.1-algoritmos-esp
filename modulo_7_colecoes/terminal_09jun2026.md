➜  python                    
Python 3.13.1 (main, Jan  8 2025, 12:52:48) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 












>>> 
>>> 
>>> c = {'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2019, 'ano_fab': 2019, 'valor\
': 102.900}
>>> 
>>> 
>>> c
{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2019, 'ano_fab': 2019, 'valor': 102.9}
>>> 
>>> c[]
  File "<python-input-7>", line 1
    c[]
      ^
SyntaxError: invalid syntax
>>> 




>>> c
{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2019, 'ano_fab': 2019, 'valor': 102.9}
>>> 
>>> c['nome']
'CIVIC'
>>> 
>>> c['ano_modelo'] = 2020
>>> 
>>> c
{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9}
>>> 
>>> 







>>> c['automatico'] = False
>>> 
>>> c
{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False}
>>> 
>>> carros = []
>>> 
>>> carros.append(c)
>>> 
>>> carros
[{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False}]
>>> len(carros)
1
>>> 



>>> c
{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False}
>>> 















>>> carros
[{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False}]
>>> 
>>> m = {'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'}
>>> 
>>> m
{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'}
>>> 
>>> m['pais']
'JAPÃO'
>>> 







>>> 
>>> 
>>> montadoras = []
>>> montadoras.append(m)
>>> 
>>> montadoras
[{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'}]
>>> montadoras.append({'id': 1, 'nome': 'FIAT', 'pais': 'ITÁLIA'})
>>> 
>>> montadoras
[{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'}, {'id': 1, 'nome': 'FIAT', 'pais': 'ITÁLIA'}]
>>> 






>>> 
>>> carros
[{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False}]
>>> 
>>> carros.append({'id': 9, 'nome': 'Fastback', 'ano_modelo': 2026, 'ano_fab': \
2025, 'valor': 135000, 'automatico': True})
>>> 
>>> carros
[{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False}, {'id': 9, 'nome': 'Fastback', 'ano_modelo': 2026, 'ano_fab': 2025, 'valor': 135000, 'automatico': True}]
>>> 






>>> carros
[{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False}, {'id': 9, 'nome': 'Fastback', 'ano_modelo': 2026, 'ano_fab': 2025, 'valor': 135000, 'automatico': True}]
>>> montadoras
[{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'}, {'id': 1, 'nome': 'FIAT', 'pais': 'ITÁLIA'}]
>>> 











>>> 
>>> 
>>> len(carros)
2
>>> carros[0]
{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False}
>>> carros[1]
{'id': 9, 'nome': 'Fastback', 'ano_modelo': 2026, 'ano_fab': 2025, 'valor': 135000, 'automatico': True}
>>> 
>>> montadoras
[{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'}, {'id': 1, 'nome': 'FIAT', 'pais': 'ITÁLIA'}]
>>> 




>>> carros[0]
{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False}
>>> carros[0]['montadora_id'] = 2
>>> 
>>> montadoras
[{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'}, {'id': 1, 'nome': 'FIAT', 'pais': 'ITÁLIA'}]
>>> 
>>> carros[1]['montadora_id'] = 1
>>> 
>>> carros
[{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False, 'montadora_id': 2}, {'id': 9, 'nome': 'Fastback', 'ano_modelo': 2026, 'ano_fab': 2025, 'valor': 135000, 'automatico': True, 'montadora_id': 1}]
>>> 


>>> carros
[{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False, 'montadora_id': 2}, {'id': 9, 'nome': 'Fastback', 'ano_modelo': 2026, 'ano_fab': 2025, 'valor': 135000, 'automatico': True, 'montadora_id': 1}]
>>> 
>>> carros.append({'id': 11, 'nome': 'City', 'ano_modelo': 2015, 'ano_fab': 201\
6, 'valor': 75000, 'automatico': True, 'montadora_id': 2})
>>> 
>>> carros
[{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False, 'montadora_id': 2}, {'id': 9, 'nome': 'Fastback', 'ano_modelo': 2026, 'ano_fab': 2025, 'valor': 135000, 'automatico': True, 'montadora_id': 1}, {'id': 11, 'nome': 'City', 'ano_modelo': 2015, 'ano_fab': 2016, 'valor': 75000, 'automatico': True, 'montadora_id': 2}]
>>> 



>>> carros
[{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False, 'montadora_id': 2}, {'id': 9, 'nome': 'Fastback', 'ano_modelo': 2026, 'ano_fab': 2025, 'valor': 135000, 'automatico': True, 'montadora_id': 1}, {'id': 11, 'nome': 'City', 'ano_modelo': 2015, 'ano_fab': 2016, 'valor': 75000, 'automatico': True, 'montadora_id': 2}]
>>> montadoras
[{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'}, {'id': 1, 'nome': 'FIAT', 'pais': 'ITÁLIA'}]
>>> 
>>> def contar_carro_por_montadora(lista_carros, id_montadora):
...     contador = 0
...     for carro in lista_carros:
...         if carro['montadora_id'] == id_montadora:
...             contador = contador + 1
...     return contador
...     
>>> 

>>> contar_carro_por_montadora(carros, 200)
0
>>> contar_carro_por_montadora(carros, 2)
2
>>> contar_carro_por_montadora(carros, 1)
1
>>> carros.append({'id': 15, 'nome': 'HRV', 'ano_modelo': 2025, 'ano_fab': 2026\
, 'valor': 175000, 'automatico': True, 'montadora_id': 2})
>>> 
>>> contar_carro_por_montadora(carros, 2)
3
>>> for m in montadoras:
...     print(m['id'], m['nome'], m['pais'], contar_carro_por_montadora(carros,\
 m['id']))
...     
2 HONDA JAPÃO 3
1 FIAT ITÁLIA 1
>>> 

>>> for m in montadoras:
...     print(m['id'], m['nome'], m['pais'], contar_carro_por_montadora(carros, m['id']\
))
...     
2 HONDA JAPÃO 3
1 FIAT ITÁLIA 1
>>> 












>>> for m in montadoras:
...     print(m['id'], m['nome'], m['pais'], contar_carro_por_montadora(carros, m['id']))
...     
2 HONDA JAPÃO 3
1 FIAT ITÁLIA 1
>>> 
>>> def contar_carro_por_montadora(lista_carros, montadora):
...     contador = 0
...     for carro in lista_carros:
...         if carro['montadora_id'] == montadora['id']:
...             contador = contador + 1
...     return contador
...     
>>> for m in montadoras:
...     print(m['id'], m['nome'], m['pais'], contar_carro_por_montadora(carros, m))
...     
2 HONDA JAPÃO 3
1 FIAT ITÁLIA 1
>>> 
>>> for c in carros:
...     print(c['id'], c['montadora_id'], c['valor'])
...     
10 2 102.9
9 1 135000
11 2 75000
15 2 175000
>>> for c in carros:
...     print(c['nome'], c['montadora_id'], c['valor'])
...     
CIVIC 2 102.9
Fastback 1 135000
City 2 75000
HRV 2 175000
>>> 




>>> for c in carros:
...     print(c['montadora_id'], c['nome'], c['valor'])
...     
2 CIVIC 102.9
1 Fastback 135000
2 City 75000
2 HRV 175000
>>> 
>>> obter_nome_montadora(montadoras, id):
  File "<python-input-91>", line 1
    obter_nome_montadora(montadoras, id):
                                        ^
SyntaxError: invalid syntax
>>> 





>>> def obter_nome_montadora(montadoras, id):
...     for m in montadoras:
...         if m['id'] == id:
...             return m['nome']
...     return 'DESCONHECIDA'
...     
>>> obter_nome_montadora(montadoras, 3)
'DESCONHECIDA'
>>> obter_nome_montadora(montadoras, 1)
'FIAT'
>>> obter_nome_montadora(montadoras, 2)
'HONDA'
>>> obter_nome_montadora(montadoras,
KeyboardInterrupt
>>> 




>>> for c in carros:
...     print(obter_nome_montadora(montadoras, c['montadora_id']), c['nome'], c['valor'])
...     
HONDA CIVIC 102.9
FIAT Fastback 135000
HONDA City 75000
HONDA HRV 175000
>>> def obter_montadora(montadoras, id):
...     for m in montadoras:
...         if m['id'] == id:
...             return m
...     return None
...     
>>> obter_montadora(montadoras, 1)
{'id': 1, 'nome': 'FIAT', 'pais': 'ITÁLIA'}
>>> obter_montadora(montadoras, 2)
{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'}
>>> 

>>> obter_montadora(montadoras, 1)
{'id': 1, 'nome': 'FIAT', 'pais': 'ITÁLIA'}
>>> 
>>> for c in carros:
...     print(obter_montadora(montadoras, c['montadora_id']), c['nome'], c['valor'])
...     
{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'} CIVIC 102.9
{'id': 1, 'nome': 'FIAT', 'pais': 'ITÁLIA'} Fastback 135000
{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'} City 75000
{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'} HRV 175000
>>> for c in carros:
...     print(obter_montadora(montadoras, c['montadora_id']), c['nome'], c['valor'])
KeyboardInterrupt
>>> l





>>> for c in carros:
...     print(obter_montadora(montadoras, c['montadora_id']), c['nome'], c['valor'])
...     
{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'} CIVIC 102.9
{'id': 1, 'nome': 'FIAT', 'pais': 'ITÁLIA'} Fastback 135000
{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'} City 75000
{'id': 2, 'nome': 'HONDA', 'pais': 'JAPÃO'} HRV 175000
>>> 
>>> for c in carros:
...     print(obter_montadora(montadoras, c['montadora_id'])['nome'], c['nome'], c['valor'])
...     
HONDA CIVIC 102.9
FIAT Fastback 135000
HONDA City 75000
HONDA HRV 175000
>>> 



>>> for c in carros:
...     montadora = obter_montadora(montadoras, c['montadora_id'])
...     print(montadora['nome'], c['nome'], c['valor'])
...     
HONDA CIVIC 102.9
FIAT Fastback 135000
HONDA City 75000
HONDA HRV 175000
>>> carros[0]
{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102.9, 'automatico': False, 'montadora_id': 2}
>>> carros[0]['valor'] = 102900
>>> 
>>> for c in carros:
...     montadora = obter_montadora(montadoras, c['montadora_id'])
...     print(montadora['nome'], c['nome'], c['valor'])
...     
HONDA CIVIC 102900
FIAT Fastback 135000
HONDA City 75000
HONDA HRV 175000
>>> 
>>> def obter_carro_por_id(lista_carros, id_carro):
...     for c in lista_carros:
...         if c['id'] == id_carro:
...             return c
...     return None
...     
>>> obter_carro_por_id(carros, 1)
>>> obter_carro_por_id(carros, 10)
{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102900, 'automatico': False, 'montadora_id': 2}
>>> obter_carro_por_id(carros, 11)
{'id': 11, 'nome': 'City', 'ano_modelo': 2015, 'ano_fab': 2016, 'valor': 75000, 'automatico': True, 'montadora_id': 2}
>>> obter_carro_por_id(carros, 15)
{'id': 15, 'nome': 'HRV', 'ano_modelo': 2025, 'ano_fab': 2026, 'valor': 175000, 'automatico': True, 'montadora_id': 2}
>>> obter_carro_por_id(carros, 1)
>>> carros
[{'id': 10, 'nome': 'CIVIC', 'ano_modelo': 2020, 'ano_fab': 2019, 'valor': 102900, 'automatico': False, 'montadora_id': 2}, {'id': 9, 'nome': 'Fastback', 'ano_modelo': 2026, 'ano_fab': 2025, 'valor': 135000, 'automatico': True, 'montadora_id': 1}, {'id': 11, 'nome': 'City', 'ano_modelo': 2015, 'ano_fab': 2016, 'valor': 75000, 'automatico': True, 'montadora_id': 2}, {'id': 15, 'nome': 'HRV', 'ano_modelo': 2025, 'ano_fab': 2026, 'valor': 175000, 'automatico': True, 'montadora_id': 2}]
>>> obter_carro_por_id(carros, 9)
{'id': 9, 'nome': 'Fastback', 'ano_modelo': 2026, 'ano_fab': 2025, 'valor': 135000, 'automatico': True, 'montadora_id': 1}
>>> 
>>> def obter_carro_por_id(lista_carros, id_carro):
...     for c in lista_carros:
...         if c['id'] == id_carro:
...             return c
...     return None