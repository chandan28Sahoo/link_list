class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class Link_list:

  def __init__(self):
    self.head = None

  def insertFirst(self, data):
    #1. create new node by giving value
    new_node = Node(data)
    #2. point the address pointer to new node
    new_node.next = self.head
    #3. reassign head to new node
    self.head = new_node

  def print_list(self):
    current_node = self.head
    while current_node:
      print(current_node.data)
      current_node = current_node.next

  def insertLast(self, data):
    #1. create new node by giving value
    new_node = Node(data)
    current_node = self.head
    if current_node is None:
      self.head = new_node
      return

    while current_node.next:
      current_node = current_node.next

    current_node.next = new_node

  def insert_middle(self, prev_data, data):
    #1. create new node by giving value
    new_node = Node(data)
    current_node = self.head
    while current_node is not None:
      # print(current_node.data,'current_node.next')
      if current_node.data == prev_data:
        break

      current_node = current_node.next

    if current_node is None:
      print("Previous node not found")
    else:
      new_node.next = current_node.next
      current_node.next = new_node

  def delete_first(self):
    current_node = self.head
    if current_node is None:
      print("List is empty")
      return

    self.head = current_node.next

  def delete_last(self):
    current_node = self.head
    if current_node is None:
      print("List is empty")
      return

    if current_node.next is None:
      self.head = None
      return

    while current_node.next.next is not None:
      current_node = current_node.next

    current_node.next = None

  def delete_middle(self, data):
    current_node = self.head
    if current_node is None:
      print("List is empty")
      return

    if current_node.data == data:
      self.head = current_node.next
      return

    while current_node.next is not None:
      if current_node.next.data == data:
        break
      current_node = current_node.next

    if current_node.next is None:
      print("Node not found")
    else:
      current_node.next = current_node.next.next


ll = Link_list()
ll.insertFirst(1)
ll.insertFirst(2)
ll.insertLast(4)
ll.insert_middle(2, 10)
# ll.delete_first()
# ll.delete_last()
# ll.delete_last()
# ll.delete_last()
# ll.delete_last()
ll.delete_middle(4)
ll.print_list()
