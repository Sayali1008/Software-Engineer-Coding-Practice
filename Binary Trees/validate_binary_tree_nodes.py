class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Neetcode
        hasParent = set(leftChild + rightChild)
        hasParent.discard(-1)
        if len(hasParent) == n:
            return False
        
        root = -1
        for i in range(n):
            if i not in hasParent:
                root = i
                break
        
        visited = set()
        def dfs(i):
            if i == -1:
                return True
            if i in visited:
                return False
            visited.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])
        
        return dfs(root) and len(visited) == n
        
        # My solution
        stack = [root]
        visited = {root}
        while len(stack) > 0:
            node = stack.pop()
            print(node)
            if leftChild[node] != -1:
                if leftChild[node] not in visited:
                    stack.append(leftChild[node])
                    visited.add(leftChild[node])
                else:
                    return False
            if rightChild[node] != -1:
                if rightChild[node] not in visited:
                    stack.append(rightChild[node])
                    visited.add(rightChild[node])
                else:
                    return False
    
        return len(visited) == n
