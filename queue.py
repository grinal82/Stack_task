from collections import deque


class Stack:
    def __init__(self):
        my_stack = deque()
        self.my_stack = my_stack

    def __str__(self):
        """
        Перегружает метод __str__ для более удобного отображения 'принта'
        """
        values = [str(x) for x in self.my_stack]
        return ' '.join(values)

    def isEmpty(self):
        """
        проверка стека на пустоту.
        Метод возвращает True или False.
        """
        if len(self.my_stack) == 0:
            return True
        else:
            return False

    def push(self, element):
        """
        добавляет новый элемент на вершину стека.
        Метод ничего не возвращает.
        """
        self.element = element
        self.my_stack.append(element)

    def pop(self):
        """
        Метод удаляющий верхний элимент. Стек изменяется.
        Метод возвращает верхний элимент стека
        """
        if len(self.my_stack) == 0:
            return None
        element = self.my_stack[-1]
        self.my_stack.pop()
        return element

    def peek(self):
        """
        возвращает верхний элемент стека, но не удаляет его.
        Стек не меняется.
        """
        if len(self.my_stack) == 0:
            return None
        else:
            return self.my_stack[-1]

    def size(self):
        """
        возвращает количество элементов в стеке.
        """
        result = len(self.my_stack)
        return result


def balanced_str(str: str):
    stack = Stack()
    balance = True
    index = 0
    while index < len(str) and balance:
        symbol = str[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balance = False
            else:
                top = stack.pop()
                if not match(top, symbol):
                    balance = False
        index += 1
    if balance and stack.isEmpty():
        return "Сбалансировано"
    else:
        return "Несбалансировано"


def match(open_bracket, close_bracket):
    openers = '([{'
    closers = ')]}'
    return openers.index(open_bracket) == closers.index(close_bracket)


# Пример сбалансированных последовательностей скобок:
string1 = '(((([{}]))))'
string2 = '[([])((([[[]]])))]{()}'
string3 = '{{[()]}}'

# Несбалансированные последовательности:
string4 = '}{}'
string5 = '{{[(])]}}'
string6 = '[[{())}]'

print(balanced_str(string3))
