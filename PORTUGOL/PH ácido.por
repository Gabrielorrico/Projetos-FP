programa {
  funcao inicio() {
    inteiro ph=0

    enquanto(ph != -1){
      escreva("\nDigite o PH: ")
      leia(ph)
      se(ph < 7){
        escreva("Ácida\n")
      }senao se(ph > 7){
        escreva("Básica\n")
      }senao se(ph == 7){
        escreva("Neutra\n")
      }
    }
  }
}
