programa {
  funcao inicio() {
    real imc, peso, altura 

    escreva("digite o seu peso: ")
    leia(peso)

    escreva("digite a sua altura: ")
    leia(altura)

    imc = peso / (altura * altura )

    se(imc < 18.5){
      escreva("você está abaixo do peso")
    }senao se ( imc >= 18.5 e imc <= 24.9){
      escreva("você está no peso ideal")
    }senao se (imc >= 25 e imc <= 29.9){
      escreva("você está com sobrepeso")
    }senao se (imc >= 30 e imc <= 40 ){
      escreva("você está com obesidade")
    }senao {
      escreva("vocé está com obesidade morbida")
    }
  }
}
