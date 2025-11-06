programa {
  funcao inicio() {
    inteiro i, valorC, valorTotal=0, valorAcima=0
    cadeia nome

    para(i=1;i<=5;i++){
      escreva(" Digite seu nome:")
      leia(nome)

      escreva(" Digite o valor mensal que você gastou: ")
      leia(valorC)

      se(valorC >= 100){
        valorAcima ++
      }

      


      valorTotal += valorC

      
    }

    escreva("O valor total de todas as compras do 5 clientes foi de R$: ", valorTotal)
    escreva("\nO número de todas as compras acima de 100 R$ é de R$: ", valorAcima)
  }
}
