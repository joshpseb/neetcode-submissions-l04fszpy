class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+","-","*","/"]
        for t in tokens:      
            if t in ops:
                op = t
                num2 = stack.pop()
                num1 = stack.pop()
                match(op):
                    case "+":
                        stack.append(num1 + num2)
                    case "-":
                        stack.append(num1 - num2)
                    case "*":
                        stack.append(num1 * num2)
                    case "/":
                        stack.append(int(num1 / num2))
            else: # t is a digit
                t = int(t)
                stack.append(t)
                
            print(stack)
        return stack[0]

        '''
        for t in tokens[::-1]:
            if t.isdigit():
                stack.append(int(t))
            else:
                stack.append(t)
        '''
        
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


                