class quickfind:
    def __init__(self,n):
        self.li = list(range(n+1))
        self.we = [0] * (n+1)

    def _root(self,e):
        while self.li[e] != e:
            e = self.li[e]
        return e

    #def _weight

    def isConnected(self,n,m):
        return self._root(n) == self._root(m)

    def union(self,n,m):
        i = self._root(n)
        j = self._root(m)
        self.li[i] = j



q = quickfind(5)
print(q.isConnected(0,3))
q.union(0,3)
print(q.isConnected(0,3))
q.union(3,5)
print(q.isConnected(0,5))
for i,j in enumerate(q.li):
    print(i,j)