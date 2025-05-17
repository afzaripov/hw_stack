from typing import Any
from node import Node


class Stack:
    '''Абстрактный тип данных, представляющий список элементов, организованных по принципу LIFO'''
    def __init__(self):
        self.head = None
        self._size = 0

    def is_empty(self) -> bool:
        '''Проверка стека на пустоту'''
        return self.head is None
    
    def push(self, item: Node):
        '''Добавляет новый элемент на вершину стека'''
        item.next = self.head
        self.head = item
        self._size += 1
    
    def pop(self) -> Any:
        '''Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'''
        if self.is_empty():
            raise ValueError("Стек пуст")
        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value
    
    def peek(self) -> Any:
        '''Возвращает верхний элемент стека, но не удаляет его. Стек не меняется'''
        if self.is_empty():
            raise ValueError("Стек пуст")
        value = self.head.value
        return value
    
    def size(self) -> int:
        '''Возвращает количество элементов в стеке'''
        return self._size