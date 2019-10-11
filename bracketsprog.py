class A:
    def __init_(self):
        self.open_list = ["[","{","("] 
        self.close_list = ["]","}",")"] 
      
    # Function to check parentheses 
    def check(self,myStr): 
        stack = [] 
        for i in myStr: 
            if i in self.open_list: 
                stack.append(i) 
            elif i in self.close_list: 
                pos = self.close_list.index(i) 
                if ((len(stack) > 0) and
                    (self.open_list[pos] == stack[len(stack)-1])): 
                    stack.pop() 
                else: 
                    return "Unbalanced"
        if len(stack) == 0: 
            return "Balanced"
a = A()
str1 = input("\n enter string")
a.check(str1)
