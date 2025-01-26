#СТЕК
#пошаговая реализация стека пайтон

#Создание класса Stack
class Stack:
    def __init__(self):
        self.items = []
    
    #Добавить метод is empty для проверки пуст ли стек
    def is_empty(self):
        return len(self.items) == 0
    
    #добавить метод push, который добавляет элемент в стек (в конец списка)
    def push(self, item):
        self.items.append(item)

    #Метод pop, который удаляет и возвращает элемент из вершины стека +проверяем, не пуст ли стек перед попыткой извелчения
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")
        
    #Метод peek - возвращает элекмент из вершины стека без его удаления + проверяем не пуст ли стек
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")
        
    #метод size - возвращает кол-во элементов в стеке
    def size(self):
        return len(self.items)
    

#Тестирование стека
#Создаем экземпляр стека
my_stack = Stack()

#Добавляем элемент в стек
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)

#просматриваем вершину стека
print('Вершина стека:', my_stack.peek())

#Удаляем эдемент из стека
my_stack.pop()

#Проверяем пуст ли стек
print("Стек пуст?", my_stack.is_empty())

#Выводим размер стека
print("Размер стека:", my_stack.size())

"Hello World!"
print(4+3)