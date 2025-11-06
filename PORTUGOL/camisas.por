programa {
  funcao inicio() {
    inteiro p, m, g, somaTotal, vp, vm, vg

    escreva("quantidade de camisas pequenas: ")
    leia(p)

    escreva("quantidade de camisas medias : ")
    leia(m)

    escreva("quantidade de camisas grandes: ")
    leia(g)

    vp = (p * 10)
    vm = (m * 12)
    vg = (g * 15)
    
    somaTotal = (vp + vm + vg)

    escreva("total de camisas p: ", p,"\ntotal de camisas m: ",m,"\n total de camisas g: ",g,"\nO valor total a pagar é: ", somaTotal, " reais")


  }
}
