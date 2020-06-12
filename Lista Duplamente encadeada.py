class No:

    def __init__(self,dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class Lista:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.__tamanho = 0

    def vazia(self):
       if self.inicio is None:
         return True
       return False

    def add_inicio(self, valor):
       no = No(valor)
       if self.vazia():
          self.inicio = self.fim = no
       else:
         no. proximo = self. inicio
         self.inicio.anterior = no
         no.anterior = None
         self.inicio = no
         self.__tamanho += 1

    def add_fim(self, valor):
       no = No(valor)
       if self.vazia():
          self.inicio = self.fim = no
       else:
           self.fim.proximo = no
           no.anterior = self.fim
           no. proximo = None
           self.fim = no
           self.__tamanho += 1

    def inserir(self, i, valor):
       metade = int(self.__tamanho / 2)
       if i > self.__tamanho:
          raise IndexError ("Posiçao de memoria invalida")
       elif i == self.__tamanho:
              self.add_fim(valor)
       elif i == 0:
              self.add_inicio(valor)
       else:
             if i <= metade:
                no = No(valor)
                perc = self.inicio
                cont = 0
                while cont < i - 1:
                  perc = perc.proximo
                  cont += 1
                No.proximo = perc.proximo
                perc.proximo.anterior = no
                perc.proximo = no
                no.anterior = perc
             else:
                no = No(valor)
                perc = self.fim
                cont = self.__tamanho
                while cont > i:
                  perc = perc.anterior
                  cont -= 1
                No.proximo = perc.proximo
                perc.proximo.anterior = no
                perc.proximo = no
                no.anterior = perc
             self.__tamanho += 1

    def remover_inicio(self):
            if self.vazia():
               raise TypeError("Lista esta vazia!")
            elif self.__tamanho == 1:
               self.inicio = None
               self.fim = None
            else:
               self.inicio = self.inicio.proximo
               self.inicio.anterior = None
            self.__tamanho -= 1

    def remover_fim(self):
           if self.vazia():
               raise TypeError("Lista esta vazia!")
           elif self.__tamanho == 1:
               self.inicio = None
               self.fim = None
           else:
               self.fim = self.fim.anterior
               self.fim.proximo = None
               self.__tamanho -= 1

    def remover_index (self, i):
        if self.vazia():
           raise TypeError("Lista esta vazia!")
        elif i == 0:
           self.remover_inicio()
        elif i == self.__tamanho - 1:
           self.remover_fim()
        else:
           perc = self.inicio
           cont = 0
           while cont < i - 1:
              perc = perc.proximo
              cont += 1
           aux = perc.proximo
           perc.proximo = aux.proximo
           aux.proximo.anterior = perc
           aux = None
           self.__tamanho -= 1

    def remover_valor(self, elemento):
      if self.__tamanho == 0:
         return None
      perc = self.inicio
      cont = 0
      while perc.elemento != elemento:
        perc = perc.proximo
        cont += 1
      self.remover_index(cont)

    def buscarindex(self, idc):
        perc = self.inicio
        cont = 0
        while cont < self.tamanho:
          if cont == ide:
            return f'No indice {idc} tem valor {perc.dado}.'
          perc = perc.proximo
          cont += 1

        raise IndexError('list out of range')

    def buscarValor(self, elem):
        perc = self.inicio
        cont = 1
        while perc:
           if perc.dado == elem:
              return f'{elem} esta na posiçao {cont}.'
           perc = perc.proximo
           cont += 1

        raise ValueError(f'O {elem} não esta na lista.')

    def sobrescrever(self, index, elemento):
        perc = self.inicio
        cont = 0
        while cont != index:
          perc = perc.proximo
          cont += 1
        perc.elemento = elemento

    def get_tamanho(self):
       return self.__tamanho

    def get_index(self, i):
      perc = self.inicio
      cont = 0
      while cont < self.__tamanho:
        if cont == i:
          return perc.dado
        perc = perc.proximo
        cont += 1

    def countPorValor(self, var):
        cont = 0
        perc = self.inicio
        while perc:
         if perc.dado == var:
            cont += 1
         perc = perc.proximo
         print(f' {var} aparece {cont} vezes na lista.')

    def __str__(self):
       valor = ''
       if self.inicio is not None:
          perc = self.inicio
          valor += str(perc.dado)
          while perc.proximo is not None:
            perc = perc.proximo
            valor += ','
            valor += str(perc.dado)
          valor += ''
       return valor

    def __len__(self):
       return self.get_tamanho()+1

    def __getitem__(self, item):  # aqui é pra exibi desse jeito: lista[5] exibindo o valor em seguida
        if item >= self.__tamanho:
           raise Stoplteration
        return self.get_index(item)

    def __setitem__(self, key, value):
        return self.sobrescrever(key, value)

lista = Lista()
lista.add_inicio(2) #Inserção no inicio
lista.add_fim(1) #iNSERÇÃO NO FIM
lista.add_fim(3)
lista.add_inicio(7)
lista.add_inicio(5)
print(lista)
print(lista.buscarValor(2)) #Busca do valor
print(lista.buscarValor(1))
lista.remover_index(2) #Remoção de valor
print('A lista está vazia ?', lista.vazia()) #Lista vazia ou não
print(lista)
print('O tamanho da lista é %d' % lista.__len__()) #Tamanho da lista