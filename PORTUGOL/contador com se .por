programa {
  funcao inicio() {
    inteiro valor, i, valorf
    cadeia nome

    para(i=1;i<=4;i++){
      escreva("\ndigite o seu nome: ")
      leia(nome)
      escreva("digite o valor que você comprou: ")
      leia(valor)

      se(valor < 5000) {
        escreva("Prezado ", nome, ", você pagará o valor final de: ", 0.90 * valor)
      } senao { 
        escreva("Prezado", nome, ", você pagará o valor final de: ", 0.85 * valor )

      }

    }



    
  }
}
