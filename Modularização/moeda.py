# desafio 107. Crie um módulo chamado moeda.py que tenha as funções 
# incorporadas aumentar(), diminuir (), dobro (), metade ()
# Faça também um progrma que import esse modulo e utilize algumas funções


def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço, taxa):
     res = preço - (preço * taxa/100)
     return res


def dobro(preço):
      res = preço *2
      return res


def metade(preço):
      res = preço /2
      return res


