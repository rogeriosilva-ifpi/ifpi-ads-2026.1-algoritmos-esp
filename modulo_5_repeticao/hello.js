import { question } from 'readline-sync'


function main(){
  const clube = question('Qual seu clube? ')
  const qtd = Number(question('Quantas vezes foi campeão? '))

  for(let i = 0; i < qtd; i += 1){
    console.log(`Volta: ${i} - ${clube}`)
  }

}

main()