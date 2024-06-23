class Solution {
    public boolean isOpen(char c){
            return (c=='('||c=='{'||c=='[');
        }
    public boolean isMatching(char a,char b){
            return (a == '(' && b == ')') || (a == '{' && b == '}') || (a == '[' && b == ']');
    }
    public boolean isValid(String s) {
        Stack<Character> stack =new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (isOpen(c)) {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                // char top = stack.pop();
                if (!isMatching(stack.peek(), c)) {
                    return false;
                }
                else{
                    stack.pop();
                }
            }
        }
        
        return stack.isEmpty();
    }
}
