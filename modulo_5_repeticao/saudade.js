import { question } from "readline-sync"

function main(){
  const nome = question('Seu nome: ')

  const lista = [5, 7, 0, 0, 1]

  for (let i of lista){
    console.log(`${i} - ${nome}`)
  }
  
  console.log('-----')

  for (let i in lista){
    console.log(`${i} - ${nome}`)
  }
}


main()