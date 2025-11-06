programa {
  funcao inicio() {
    cadeia nome
    real n1, n2, n3, media

    escreva("digite seu nome:")
    leia(nome)

    escreva(" \ndigite a primeira nota: ")
    leia(n1)

    escreva(" \ndigite a segunda nota: ")
    leia(n2)

    escreva(" \ndigite a terceira nota: ")
    leia(n3)

    media = (n1 * 2 + n2 * 3 + n3 * 5) / 10

    escreva("\n SITUAÇÃO ATUAL: ")

    se (media < 5 ) {
      escreva(" \nvocê está reprovado")
    } senao se (media == 5 e media <7){
      escreva(" \nvocê está de recuperação ")
    } senao {
      escreva(" \nvocê está aprovado")
    }
  }
}
