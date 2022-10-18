class Stack(list):

    def isEmpty(self):
        '''Проверка стека на пустоту. Метод возвращает True или False.'''
        return False if len(self) > 0 else True 
    
    def push(self, new_element):
        '''Добавляет новый элемент на вершину стека. Метод ничего не возвращает.'''
        self.append(new_element)
    
    def pop(self):
        '''Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека.'''
        last_el = self[-1]
        self.__delitem__(-1)
        return last_el
    
    def peek(self):
        '''Возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''
        return self[-1]
    
    def size(self):
        '''Возвращает количество элементов в стеке.'''
        return len(self)
    

if __name__ == '__main__':
   
    my_stack = Stack('123456789')
    empty_stack = Stack('')
    print(my_stack.isEmpty(), empty_stack.isEmpty())
    my_stack.push('0')
    print(my_stack)
    my_stack.pop()
    print(my_stack)
    print(my_stack.peek())
    print(my_stack.size())