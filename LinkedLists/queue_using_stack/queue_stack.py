# Approach 1
# push: if front is empty: push to front else push to rear
# pop: if font is !empty: pop from front else push everything from rear to front, then pop
# Better solution: Enqueue in s1. When popping, pop from stack1 and push to stack2.
# Keep popping from s2 till s2 not empty. Push will always be in s1. O(n). Enqueue is fast.
