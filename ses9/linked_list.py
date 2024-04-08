class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.__dict__}'


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f'{self.__dict__}'

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
