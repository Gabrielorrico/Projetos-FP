programa {
  funcao inicio() {
    cadeia curvas
    inteiro i, curvaEsq=0, curvaDir=0, incorretas=0
    
    para (i= 1; i<=10;i++){
      escreva("A ",i,"° curva foi para a: ")
      leia(curvas)

      se(curvas == 'E' ou curvas == "Esq" ou curvas =="Esquerda"){
        curvaEsq++

      }senao se(curvas == 'D' ou curvas == "Dir" ou curvas == "Direita"){
        curvaDir++
      }senao{
        incorretas++
      }


    }
    escreva("\nO número de curvas a direita é: ",curvaDir, "\nO número de curvas a esquerda é: ", curvaEsq, "\nO número de indicações incorretas é: ", incorretas)



  }
}
