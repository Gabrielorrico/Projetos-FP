programa {
  funcao inicio() {
   inteiro valor, qntN,i=1, m2=0,m3=0


   escreva("Olá, digite a quantidade de números que serão inseriodos: ")
   leia(qntN)

   enquanto(i<=qntN){
    escreva("Digite o ", i, "° ", "dos ", qntN, " valores escolhidos: ")
    leia(valor)
    i++

    se(valor%2 ==0){
      m2++
    }
    se(valor%3 ==0){
      m3++
    }

    
   }

   escreva("\nDentro dos números escolhidos, você teve: ", m2, " números múltiplos de 2 ",
   "e ", m3, " números múltiplos de 3")
   } 
  }
