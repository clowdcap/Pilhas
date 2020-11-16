class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# inserir
# remover
# observar o topo da pilha

class Pilha:
    def __init__(self):
        self.topo = None
        self._size = 0

    # Enquadra nos casos especiais, 4 op elementares, complexidade de O[1]
    def push(self, elemento):  # Insere um elemento na pilha
        node = Node(elemento)
        node.next = self.topo
        self.topo = node
        self._size = self._size + 1

    # Operações constantes, complexidade de O[1]
    def pop(self):  # remove o elemento do topo da pilha
        if self._size > 0:
            node = self.topo
            self.topo = self.topo.next
            self._size = self._size - 1
            return node.data
        raise IndexError("A pilha está vazia")

    # Operações constantes, complexidade de O[1]
    def peek(self):  # retorna o topo sem remover
        if self._size > 0:
            return self.topo.data
        raise IndexError("A pilha está vazia")

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        r = ""
        ponteiro = self.topo
        while ponteiro:
            r = r + str(ponteiro.data) + "\n"
            ponteiro = ponteiro.next
        return r

    def __str__(self):
        return self.__repr__()


'''
    COMANDOS PARA EXECUTAR EM TESTES

pilha = Pilha()  # Cria uma pilha

pilha.push(23)
pilha.push('python')
pilha.push(5)
pilha.push('Sucesso')
pilha.push(10)
pilha.push(24.5)    # Adiciona elementos na pilha ( Do topo pra baixo )

pilha  
print(pilha)   # Comandos para ver a pilha listada


pilha.peek()   # Ver o topo da pilha

pilha.pop()   # Retira elementos da pilha ( Do topo pra baixo )

len(pilha)   # Ve a quantidade de elementos que há na pilha
'''