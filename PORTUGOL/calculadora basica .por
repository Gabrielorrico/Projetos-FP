programa {
  funcao inicio() {
    inteiro n1, n2, op
    caracter a

    escreva("digite o primeiro número: ")
    leia(n1)

    escreva("digite o segundo número: ")
    leia(n2)

    escreva("digite qual da 3 operações você vai escolher \n[S] Soma \n[M] Multiplicação \n[B] Subtração \n escolha : ")
    leia(a)

    


    se( a == 'S' ou a == 's' ){
      escreva(" o resultado da soma é: ", (n1+n2)  )
    } senao se (a == 'M'ou a =='m' ) {
      escreva("o resultado da multiplicação é: ", (n1 * n2))
    } senao se( a == 'B' ou a =='b'){
      escreva("o resultado da subtração é: ", (n1- n2))
    } senao {
      escreva("O que você digitou não corresponde a nenhuma das 3 operações, tente novamente")
    }


  }
}
