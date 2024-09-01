class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)  # Initialize the parent class explicitly
        self.__counter = 0  # Initialize the counter

    def get_counter(self):
        return self.__counter  # Return the current counter value

    def push(self, val):
        Stack.push(self, val)  # Call the parent class's push method explicitly
        self.__counter += 1  # Increment the counter

    def pop(self):
        Stack.pop(self)  # Call the parent class's pop method explicitly
        self.__counter += 1  # Increment the counter



stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
