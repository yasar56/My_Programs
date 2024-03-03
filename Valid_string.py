class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for i in s:
            if len(lst) == 0:
                lst.append(i)
            elif (lst[-1] == '(' and i == ')') or (lst[-1] == '[' and i == ']') or (lst[-1] == "{" and i == '}'):
                lst.pop()
            else:
                lst.append(i)

        if len(lst) == 0:
            return True
        else:
            return False
