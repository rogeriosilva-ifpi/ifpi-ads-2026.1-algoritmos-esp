import { question } from "readline-sync"

function main(){
  const n = Number(question('N: '))
  const superior = Number(question('Superior: '))
  const inferior = Number(question('Inferior: '))

  for (let i = inferior; i <= superior; i++){
    if (i % n === 0){
      console.log(i)
    }
  }

}


main()