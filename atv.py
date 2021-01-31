class No:
    valor = None
    f_esq = None
    f_dir = None

    def __init__(self,v,esq=None,di=None):
        self.valor = v
        self.f_esq = esq
        self.f_dir = di

    def __str__(self):
        return str(self.valor)

class arvore:
     raiz = None
     def __init__(self,r=None):
         self.raiz = r

     def vazia(self):
        if self.raiz == None:
            return "Vazia"
        else:
            return "Contém elemento"

     def valor_folhas(self,no):
         if no == None:
             return 
         if(no.f_esq == None and no.f_dir == None):
             print(no.valor)
         self.valor_folhas(no.f_esq)
         self.valor_folhas(no.f_dir)

     def altura(self,no):

         if no == None:
             return -1
         esquerdo = self.altura(no.f_esq)
         direito = self.altura(no.f_dir)
         if esquerdo>direito:
             return esquerdo+1
         else:
             return direito+1

     def buscar(self, no, v):
         if no == None:
             return 
         if no.valor == v:
             print("valor encontrado: ", v)
         self.buscar(no.f_esq, v)
         self.buscar(no.f_dir, v)

     def quantidade(self, no):
         if no == None:
             return 0
         else:
             return self.quantidade(no.f_esq) + self.quantidade(no.f_dir) +1
         


raiz = No(5)
raiz.f_esq = No(3)
raiz.f_esq.f_dir = No(4)
raiz.f_dir = No(8)


tree = arvore(raiz)
print("A arvore está vazia? ",tree.vazia())
print("Qual a altura da arvore? ",tree.altura(raiz))
print("Quantidade? ", tree.quantidade(raiz))
print( tree.valor_folhas(raiz))
print(tree.buscar(raiz, 3))
print(tree.buscar(raiz, 20))

