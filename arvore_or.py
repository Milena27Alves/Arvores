class No:
     
     def __init__(self, key, di, esq):
          self.item = key
          self.dir = di
          self.esq = esq

     def __str__(self):
        return str(self.item)

class Arvore:

     def __init__(self):
          self.root = None

#Verifica se a árvore está vazia
     def vazia(self):
        if self.root == None:
            return "Vazia"
        else:
            return "Contém elemento"

#Inserir elemento na árvore
     def inserir(self, v):
          novo = No(v,None,None)
          if self.root == None:
               self.root = novo
          else:
               atual = self.root
               while True:
                    anterior = atual
                    if v == atual.item:
                         return
                    elif v < atual.item:
                         atual = atual.esq
                         if atual == None:
                                anterior.esq = novo
                                return
                    else:
                         atual = atual.dir
                         if atual == None:
                                 anterior.dir = novo
                                 return


#Remover elemento
     def remover(self, v):
         if self.root == None:
               return False
         atual = self.root
         pai = self.root
         filho_esq = True

         while atual.item != v: 
               pai = atual
               if v < atual.item:
                    atual = atual.esq
                    filho_esq = True 
               else: 
                    atual = atual.dir 
                    filho_esq = False
               if atual == None:
                    return False
          
         if atual.esq == None and atual.dir == None:
               if atual == self.root:
                    self.root = None
               else:
                    if filho_esq:
                         pai.esq =  None 
                    else:
                         pai.dir = None 
         elif atual.dir == None:
               if atual == self.root:
                    self.root = atual.esq 
               else:
                    if filho_esq:
                         pai.esq = atual.esq 
                    else:
                         pai.dir = atual.esq
         elif atual.esq == None:
               if atual == self.root:
                    self.root = atual.dir
               else:
                    if filho_esq:
                         pai.esq = atual.dir
                    else:
                         pai.dir = atual.dir
         else:
               sucessor = self.nosucessor(atual)
               if atual == self.root:
                    self.root = sucessor
               else:
                    if filho_esq:
                         pai.esq = sucessor
                    else:
                         pai.dir = sucessor
               sucessor.esq = atual.esq
         return True


     def nosucessor(self, apaga):
          paidosucessor = apaga
          sucessor = apaga
          atual = apaga.dir 

          while atual != None:
               paidosucessor = sucessor
               sucessor = atual
               atual = atual.esq 

          if sucessor != apaga.dir:
               paidosucessor.esq = sucessor.dir 
               sucessor.dir = apaga.dir 
          return sucessor


# Altura da árvore
     def alt(self):
         return self.altura(self.root)

     def altura(self,no):

         if no == None:
             return -1
         esquerdo = self.altura(no.esq)
         direito = self.altura(no.dir)
         if esquerdo>direito:
             return esquerdo+1
         else:
             return direito+1

# Buscar elemento na árvore
     def busca(self, valor):
         self.buscar(self.root, valor)

     def buscar(self, no, v):
         if no == None:
             return 
         if no.item == v:
             print("valor encontrado: ", v)
         self.buscar(no.esq, v)
         self.buscar(no.dir, v)

#Buscar elemento na árvore ordenada
     def busca_arvore_ordenada(self, chave):
         if self.root == None:
              return None
         atual = self.root 
         while atual.item != chave:
               if chave < atual.item:
                    atual = atual.esq 
               else:
                    atual = atual.dir
               if atual == None:
                    return None 
         return atual 

#Percurso ERD
     def erd(self):
         self.inOrder(self.root)

     def inOrder(self, atual):
         if atual != None:
              self.inOrder(atual.esq)
              print(atual.item,end=" ")
              self.inOrder(atual.dir)

#Percurso RED
     def red(self):
         self.preOrder(self.root)

     def preOrder(self, atual):
         if atual != None:
              print(atual.item,end=" ")
              print("(", end=" ")
              self.preOrder(atual.esq)
              self.preOrder(atual.dir)
              print(")", end=" ")
              


t = Arvore()
t.inserir(4)
t.inserir(2)
t.inserir(6)
t.inserir(3)
t.inserir(1)
print(t.vazia())
print("A altura é: ",t.alt())
t.busca(2)
print("Busca na árvore ordenada: ",t.busca_arvore_ordenada(3))
t.red()
print()
t.erd()
print()
t.remover(2)
print("Depois da remorção")
t.red()

