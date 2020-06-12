class Queue:

    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def push(self, e):
        self.queue.append(e)
        self.len_queue += 1

    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1

    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    def length(self):
        return self.len_queue

    def front(self):
        if not self.empty():
            return self.queue[0]
        return None

l = Queue()

print('Lista de Clientes')
#inserção dos clientes
l.push('Julia')
l.push('Lucas')
l.push('Fernando')
#Mostragem do primeiro cliente a ser atendido
print(l.front())
#inserção de clientes na fila
c = input(str('Qual o nome do próximo cliente ?\n'))
l.push(c)
#Remoção de clientes da fila
l.pop()
l.pop()
l.pop()
#Mostrando novamente o cliente
print('Ultima cliente a ser adicionado é o(a)', l.front())
print('Quantidade de clientes restantes %d' % l.length() )





