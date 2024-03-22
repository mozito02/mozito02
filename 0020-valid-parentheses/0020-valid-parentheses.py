class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open_b={'(','{','['}
        closed_b={')','}',']'}
        b_dict={'(':')','{':'}','[':']'}
        for char in s:
            if char in open_b:
                stack.append(char)
            elif char in closed_b:
                if not stack:
                    return False
                else:
                    top_stack=stack.pop()
                    if(b_dict[top_stack]!=char):
                        return False
        if stack:
            return False
        else:
            return True