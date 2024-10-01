class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operations = ["+","*","/","-"]
        #result = int(6 / -132)
        #print(result)
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                e1 = stack.pop()
                e2 = stack.pop()
                #print("e1",e1)
                #print("e2",e2)
                if token == "+":
                    toPush = e2 + e1
                    stack.append(toPush)
                    #print(toPush)
                elif token == "*":
                    toPush = e2 * e1
                    stack.append(toPush)
                    #print(toPush)
                elif token == "/" :
                    toPush = int(float(e2)/e1)
                    stack.append(toPush)
                    #print(toPush)
                else :
                    toPush = e2 - e1
                    stack.append(toPush)
                    #print(toPush)
        return int(stack[0])



        