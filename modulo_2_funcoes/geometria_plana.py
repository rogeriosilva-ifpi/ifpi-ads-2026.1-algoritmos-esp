# def isTriangle():
#   ...


def eh_triangulo(a: int, b: int, c: int):
  if a <= (b + c) and b <= (a + c) and c <= (a + b):
    return True
  else:
    return False
  

def obter_tipo_triangulo(a: int, b: int, c: int) -> str:
  if a == b and b == c:
    return 'Equilátero'
  elif a == b or b == c or a == c:
    return 'Isósceles'
  else:
    return 'Escaleno'  
