from utils_io import obter_texto, obter_numero_real, escrever


def main():
  nome = obter_texto('Qual seu nome? ')
  altura = obter_numero_real('Qual sua altura (m)? ')
  peso = obter_numero_real('Qual seu peso (kg)? ')

  imc = calcular_imc(altura, peso)
  classificao = classificar_imc(imc)

  escrever(f'{nome} seu IMC é {imc:.1f} ({classificao})')


def calcular_imc(altura, peso):
  imc = peso / (altura*altura)
  return imc


def classificar_imc(imc):
  if imc <= 18.5:
    return 'Abaixo do Peso'
  elif imc < 25:
    return 'Peso Normal'
  elif imc < 30:
    return 'Sobrepeso'
  elif imc < 35:
    return 'Obesidade Grau I'
  elif imc < 40:
    return 'Obesidade Grau II'
  else:
    return 'Obesidade Grau III'



main()