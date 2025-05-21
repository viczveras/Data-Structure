
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        novo_no = Node(valor)
        novo_no.proximo = self.topo
        self.topo = novo_no

    def pop(self):
        if self.topo is None:
            print("Pilha vazia!")
            return None
        valor = self.topo.valor
        self.topo = self.topo.proximo
        return valor

    def is_empty(self):
        return self.topo is None

    def exibir(self):
        atual = self.topo
        elementos = []
        while atual:
            elementos.append(atual.valor)
            atual = atual.proximo
        print("Pilha (topo -> base):", elementos)


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enqueue(self, valor):
        novo_no = Node(valor)
        if self.fim:
            self.fim.proximo = novo_no
        self.fim = novo_no
        if self.inicio is None:
            self.inicio = novo_no

    def dequeue(self):
        if self.inicio is None:
            print("Fila vazia!")
            return None
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return valor

    def is_empty(self):
        return self.inicio is None

    def exibir(self):
        atual = self.inicio
        elementos = []
        while atual:
            elementos.append(atual.valor)
            atual = atual.proximo
        print("Fila (início -> fim):", elementos)


if __name__ == "__main__":
    print("Exemplo de Pilha Encadeada:")
    pilha = Pilha()
    pilha.push(10)
    pilha.push(20)
    pilha.push(30)
    pilha.exibir()
    print("Removendo da pilha:", pilha.pop())
    pilha.exibir()
    print("Removendo da pilha:", pilha.pop())
    pilha.exibir()
    print("Removendo da pilha:", pilha.pop())
    pilha.exibir()
    print("Removendo da pilha:", pilha.pop())

    print("\nExemplo de Fila Encadeada:")
    fila = Fila()
    fila.enqueue("A")
    fila.enqueue("B")
    fila.enqueue("C")
    fila.exibir()
    print("Removendo da fila:", fila.dequeue())
    fila.exibir()
    print("Removendo da fila:", fila.dequeue())
    fila.exibir()
    print("Removendo da fila:", fila.dequeue())
    fila.exibir()
    print("Removendo da fila:", fila.dequeue())