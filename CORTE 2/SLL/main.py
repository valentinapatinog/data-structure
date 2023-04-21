from single_linked_list import SingleLinkedList
inst_sll = SingleLinkedList()

# Ingresamos como parametro el valor del nodo

""" Métodos para añadir nodo"""
inst_sll.create_node_sll_ends("Batman")
inst_sll.create_node_sll_ends('Robin')
inst_sll.create_node_sll_ends("Gatubela")
inst_sll.create_node_sll_ends("Deadpool")
inst_sll.create_node_sll_ends("Wolverine")
inst_sll.create_node_sll_unshift("Hulk")
#"""" | Hulk | Batman | Robin | Wolverine"""
inst_sll.show_list()

"""Métodos de eliminar
print('---------------------------------------------------')
print('     >> Eliminar último nodo <<')
inst_sll.delete_node_sll_pop()
inst_sll.show_list()

# | Hulk | Batman | Robin |

print('---------------------------------------------------')
print('\n     >> Eliminar primer nodo <<')
inst_sll.shift_node_sll()
inst_sll.show_list()
# | Batman | Robin |

print('---------------------------------------------------')
print('\n     >> Consultar el valor del nodo <<')
inst_sll.get_node_value (1)
inst_sll.get_node_value (2)

print('---------------------------------------------------')
print('\n     >> Actualizar valor del nodo <<')
inst_sll.update_node_value(1, "Linterna verde")
inst_sll.show_list()

print('---------------------------------------------------')
print('\n     >> Eliminar nodo especifico <<')
inst_sll.remove_node(2)
inst_sll.show_list()


print('---------------------------------------------------')
print('\n     >> Obtener el tamaño de la lista <<')
inst_sll.list_size()
inst_sll.show_list()

print('---------------------------------------------------')
print('\n     >> Devolver elemento de determiada posicion <<')
inst_sll.position_of_an_element("Gatubela")
inst_sll.show_list()


print('---------------------------------------------------')
print('\n     >> Invertir la lista <<')
nombres = ['Hulk' , 'Batman','Robin','Wolverine']
l = inst_sll.invest_list(nombres)
print(l)


print('---------------------------------------------------')
print('\n     >>    Insertar un elemento en una posición determinada de la lista    <<')
inst_sll.insert_on_index(2, 'Gatubela')
inst_sll.show_list()


print('---------------------------------------------------')
print('\n     >> La lista está vacia/ La lista no está vacia <<')
inst_sll.check_empty()
inst_sll.show_list()

print('---------------------------------------------------')
print('\n     >> Eliminar todos los elementos de la lista <<')
inst_sll.remove_all_nodes_list()
inst_sll.show_list()"""


