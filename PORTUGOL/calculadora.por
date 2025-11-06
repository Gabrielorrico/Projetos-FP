programa {
  funcao inicio() {
    inteiro num1, tabu, finaltabu, i


    escreva("vamos lá, digite o número que você quer a tabuada: ")
    leia(num1)

    escreva("agora digite o número que você quer que inicie a tabuada: ")
    leia(tabu)

    escreva("agora digite o número que você quer que termine a tabuada: ")
    leia(finaltabu)

    para(i=tabu; i<=finaltabu;i++){
      escreva(num1, " X ", i," = ", num1 * i, "\n" )
    }
  }
}
