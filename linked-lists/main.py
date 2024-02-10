from linkedList import Node, LinkedList

if __name__ == "__main__":
    node_1 = Node(5)
    node_2 = Node(6)
    node_3 = Node(10)

    my_list = LinkedList(node_1)
    my_list.append(node_2)
    my_list.append(node_3)
    my_list.append(Node(17))

    my_list.insert(Node(21), 0)

    my_list.print_values()
    print("############")
    my_list.delete(0)
    my_list.print_values()
    print("############")
    my_list.reverse()
    my_list.print_values()
    print("############")

