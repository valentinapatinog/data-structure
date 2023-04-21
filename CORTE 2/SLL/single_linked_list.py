class SingleLinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    """ Por fuera de la clase nodo """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def show_list(self):
        # 1. Declarar una array vacío que contendraá los valores de los nodos de SLL
        array_with_nodes_value = list()
        current_node = self.head
        # Mientras el nodo actual que estoy visitando sea diferente de None
        while (current_node != None):
            # Añado al final de la lista el valor extraido del nodo
            array_with_nodes_value.append(current_node.value)
            # Visito el próximo nodo antes de salir del while
            current_node = current_node.next
        # Imprimimos la lista
        print(array_with_nodes_value)

    def create_node_sll_ends(self, value):
        # Creamos una variable que va a tener la estructura de un nodo
        new_node = self.Node(value)
        # Validar si la SLL tiene nodos o no
        if self.head == None:
            # Al nuevo nodo se convierte en la cabeza y cola de la lista
            self.head = new_node
            self.tail = new_node
        else:
            # Si ingresa en esta condición, es porque ya existe al menos un nodo
            # 1. Debemos relacionar al nuevo nodo con la cola de la lista
            # 2. Convertir al nuevo nodo en la cola de la lista
            self.tail.next = new_node
            self.tail = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length += 1

 #Crear nuevos nodos
    def create_node_sll_unshift(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            print(self.head.value)
        else:
            new_node.next = self.head
            self.head = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length += 1

#Eliminar nodo especifico
    def delete_node_sll_pop(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            current_node = self.head
            new_tail = current_node
            while current_node.next != None:
                new_tail = current_node
                current_node = current_node.next
            print(f'Valor del nodo a eliminar es: {self.tail.value}')
            self.tail = new_tail
            self.tail.next = None
            self.length -= 1

    '''Eliminar nodo al inicio de la lista'''
#Eliminar el primer nodo/ cabeza 
    def shift_node_sll(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:

            self.head = None
            self.tail = None
            self.length -= 1
        else:
            remove_node = self.head
            print(f'Valor del nodo a eliminar es: {remove_node.value}')
            self.head = remove_node.next
            self.length -= 1

    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while (index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node

 #Consultar el valor del nodo
    def get_node_value(self, index):
        if index < 1 or index > self.length:
            print('No se encontro')
        elif index == 1:
            print(self.head.value)
        elif index == self.length:
            print(self.tail.value)
        else:
            current_node = self.head
            node_counter = 1
            while (index != node_counter):
                current_node = current_node.next
                node_counter += 1
            print(current_node.value)

#Cambiar un nodo por otro
    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            # Encontro el nodo y se puede actualizar
            print(
                f'Actualizando el valor del nodo ...\n           >> {search_node.value} << a\n           >>{new_value}<<')
            search_node.value = new_value
        else:
            # No encuentra el nodo
            print("     >> No se encontro el nodo <<")

#Remover nodo especifico
    def remove_node(self, index):
        if index == 1:
            self.shift_node_sll()
        elif index == self.length:
            self.delete_node_sll_pop()
        else:
            remove_node_sll = self.get_node(index)
            if remove_node_sll != None:
                previous_node = self.get_node(index - 1)
                print(self.get_node(index).value)
                previous_node.next = remove_node_sll.next
                remove_node_sll.next = None
            else:
                print('     >> No se encontro el nodo <<')

    # Obtener el tamaño de la lista y devuelve en String y los valores que tiene la lista
    def list_size(self):
        print(self.length)

    # Buscar un elemento en la lista simplemente enlazada y devolver su posición
    def position_of_an_element(self, valor):
        if valor == self.head.value:
            return print('1')
        elif valor == self.tail.value:
            return print(self.length)
        else:
            current_node = self.head
            node_counter = 1
            while (valor != current_node.value):
                print(current_node.value)
                current_node = current_node.next
            return print(node_counter)

    #Invertir la lista
    def invest_list (self,list):
        if len(list) == 0:
            return []
        names = list.pop(0) 
        list2 = self.invest_list (list) 
        print(list2)
        list2.append (names)
        return list2

    # Eliminar todos los elementos de la lista.
    def remove_all_nodes_list(self):
        while self.head != None:
            remove_node = self.head
            self.head = remove_node.next
            self.length -= 1
            
    # Insertar un elemento en una posición determinada de la lista
    def insert_on_index(self, index, value):
        new_node = self.Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            previous_node = self.head
            for i in range(index-1):
                previous_node = previous_node.next
                if previous_node is None:
                    raise IndexError("Index out of range")
                new_node.next = previous_node.next
                previous_node.next = new_node

    # Comprobar si la lista esta vacia
    def check_empty(self):
        if self.length < 1:
            print("La lista esta vacia")
        else:
            print("La lista no esta vacia")
            
    