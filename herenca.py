import random

class pessoa(object):

    def __init__(self, nome, apelido, mensagem):
        self.nome       = nome
        self.apelido    = apelido
        self.mensagem   = mensagem

    def __str__(self):
        
        return "\nPessoa: %s,%s,%s \nFala: %s" %(self.nome, self.apelido, str(self.pegarIdade()),self.mensagem)

    def pegarIdade(self):

        idade = random.randint(1,100)
        return idade

if __name__ == "__main__":

    pessoa1 = pessoa("Leonardo", "Leo", "Olá a todos!")
    pessoa2 = pessoa("Roberson", "Rob", "Eae, blz!")

    print(pessoa1)
    print(pessoa2)    