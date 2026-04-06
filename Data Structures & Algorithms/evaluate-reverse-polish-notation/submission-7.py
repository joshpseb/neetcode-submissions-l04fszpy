class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens: 
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 - num2)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(t)) 
        return stack[0]

        '''
        for t in tokens[::-1]:
            if t.isdigit():
                stack.append(int(t))
            else:
                stack.append(t)
    
        
        while len(stack) > 1:
            
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            op = stack.pop()

            match(op):
                case "+":
                    stack.append(num1 + num2)
                case "-":
                    stack.append(num1 - num2)
                case "*":
                    stack.append(num1 * num2)
                case "/":
                    stack.append(num1 / num2)
        return stack[0]
        '''


                