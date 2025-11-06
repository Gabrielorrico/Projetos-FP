programa {
  funcao inicio() {
    cadeia user, senha
    


    escreva("digite o usuario: ")
    leia(user)

    se (user == "1234") {
      escreva("usuário correto, digite sua senha: ")
      leia(senha)
      se (senha != "9999") {
        escreva(" Senha incorreta ")
      } senao {
        escreva("Acesso permitido")
      }
    } senao {
      escreva("usuario incorreto")
    }
    

  }
}
