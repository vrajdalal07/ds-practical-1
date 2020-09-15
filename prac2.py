# Implement Linked List. Include options for insertion, deletion and search of a number, reverse the list and concatenate two linked lists
# 3028 Vraj

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def is_empty(self) -> bool:
        return self.length == 0

    def get_size(self) -> int:
        return self.length

    def display(self):
        if self.is_empty():
            print("Doubly Linked List is empty")
            return
       
    def get_head(self) -> Node:
        return self.start

    def remove_head(self):
        if self.is_empty():
            print("Doubly Linked List is empty")
            return
        elif self.length == 1:
            self.start = None
            self.end = None
        else:
            self.start = self.start.next
        self.length -= 1

    

    def get_tail(self) -> Node:
        return self.end

    def remove_tail(self):
        if self.is_empty():
            print("Doubly Linked List is empty")
            return
        elif self.length == 1:
            self.start = None
            self.end = None
        else:
            self.end = self.end.prev
        self.length -= 1

        else:
            prev_node = self.get_node_at(index - 1)
            current_node = self.get_node_at(index)
            new_value = Node(element)
            prev_node.next = new_value
            new_value.next = current_node
            new_value.prev = prev_node
            current_node.prev = new_value
            self.length += 1

    def get_node_at(self, index, direction="auto") -> Node:
        if index < 0 or index >= self.length:
            print("Index out of bounds")
        else:
            element_node = self.start
            counter = 0
            while counter < index:
                element_node = element_node.next
                counter += 1
            return element_node

    def remove_between_list(self, index):
        if index < 0 or index >= self.length:
            print("Index out of bounds")
        elif index == self.length - 1:
            self.remove_tail()
        elif index == 0:
            self.remove_head()
        else:
            prev_node = self.get_node_at(index - 1)
            next_node = self.get_node_at(index + 1)
            prev_node.next = next_node
            next_node.prev = prev_node
            self.length -= 1

        def reverse(self):
        if self.is_empty():
            print("Doubly Linked List is empty")
            return
        elif self.length == 1:
            return
        elif self.length == 2:
            temp = self.start
            self.start = self.end
            self.end = temp
            self.start.prev = None
            self.start.next = self.end
            self.end.prev = self.start
            self.end.next = None
        elif self.length == 3:
            mid = self.__get_node_from_start(1)
            temp = self.start
            self.start = self.end
            self.end = temp
            self.start.prev = None
            self.start.next = mid
            mid.prev = self.start
            mid.next = self.end
            self.end.prev = mid
            self.end.next = None
        elif self.length > 3:
            temp_lst = []
            first = self.start
            temp_lst.append(first)
            first = first.next
            while first:
                temp_lst.append(first)
                first = first.next
            temp_lst.reverse()
            class Matrix:
    def __init__(self, m_1):
        self.m_1 = m_1

    def addition(self, m_2):
        sum_m = [[None, None, None], [None, None, None], [None, None, None]]
        for i in range(0, 3):
            for j in range(0, 3):
                sum_m[i][j] = self.m_1[i][j] + m_2[i][j]
        return sum_m


if __name__ == '__main__':
    matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = Matrix(matrix_1)
    print(matrix.addition(matrix_2))


arr1=[12,35,42,22,1,6,54]
arr2=['hello','world']
arr1.index(35)
print(arr1)
arr1.sort()
print(arr1)
arr1.extend(arr2)
print(arr1)
arr1.reverse()
print(arr1)


