class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Solution key: Use python default's stack implementation
        with append and post. Be aware that order might matter.
        '''
        stack = []
        for i in range(len(tokens)):
            print(stack)
            if tokens[i] == '+':
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif tokens[i] == '-':
                # order matters
                a, b = stack.pop(), stack.pop()
                result = b - a
                stack.append(result)
            elif tokens[i] == '*':
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif tokens[i] == '/':
                # order matters
                a, b = stack.pop(), stack.pop()
                result = b / a
                stack.append(int(result))
            else:
                stack.append(int(tokens[i]))

        return int(stack.pop())