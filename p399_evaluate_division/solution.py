class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        lookup = collections.defaultdict(dict)
        for (x, y), value in zip(equations, values):
            lookup[x][y] = value
            lookup[y][x] = 1.0/value

        def dfs(x, y, visited):
            if x not in lookup and y not in lookup: return -1
            if y in lookup[x]: return lookup[x][y]
                
            for n in lookup[x]:
                if n in visited: continue
                visited.add(n)
                tmp = dfs(n, y, visited)
                if tmp == -1: continue
                return lookup[x][n] * tmp
                
            return -1

        result = []
        for x, y in queries:
            result.append(dfs(x, y, set()))

        return result