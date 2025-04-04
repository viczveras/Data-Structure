class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elemento):
        node = Node(elemento)
        node.next = self.top
        self.top = node 
        self._size += 1


    def pop(self):
        if self.empty():
            return 'Pilha vazia'
        node = self.top
        self.top = self.top.next
        self._size -= 1
        return node.data
    

    def peek(self):
        if self.empty():
            return 'Pilha vazia'
        return self.top.data

    

    def __len__(self):
        return self._size


    def empty(self):
        return len(self) == 0




    def __repr__(self):
        if len(self) == 0:
            return 'Pilha vazia'
        
        string = ''
        pointer = self.top
        
        while pointer:
            string += str(pointer.data) + '\n'
            pointer = pointer.next  

        return string

stack = Stack()
print(stack)  # Deve mostrar "Pilha vazia"
stack.push(1)
stack.push(2)
stack.push(3)
print(len(stack)) # Deve mostrar 3 
print(stack)  # Deve mostrar: 3\n2\n1\n