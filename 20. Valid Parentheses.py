class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(","{","["]:
                stack.append(c)
            else:
                if len(stack) != 0:
                    if c == ")":
                        a = stack.pop()
                        if a =="(":
                            continue
                        else:
                            return False
                    elif c =="}":
                        a = stack.pop()
                        if a =="{":
                            continue
                        else:
                            return False
                    else:
                        a = stack.pop()
                        if a =="[":
                            continue
                        else:
                            return False
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
                    
            