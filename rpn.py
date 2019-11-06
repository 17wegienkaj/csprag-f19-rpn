#!/usr/bin/env python3

def calculate(s):
    stack = list()
    for token in s.split():
        if token == '+':
            s2 = stack.pop()
            s1 = stack.pop()
            result = s1 + s2
            stack.append(result)
        elif token == '-':
            s2 = stack.pop()
            s1 = stack.pop()
            result = s1 - s2
            stack.append(result)
        else:
            stack.append((int(token)))
    if (len(stack)) != 1:                                                                                           
        raise TypeError('malformed input')  
    return stack.pop();

def main():
    while True:
        calculate(input("prn calc> "))
                                
if __name__== '__main__':         
    main()

