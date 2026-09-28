class sol:
    def adjacecnyList(self):
        n,m = map(int,input().split())

        adj = [[] for _ in range(n)]

        for _ in range(m):


            src,dest = map(int,input().split())

            adj[src].append(dest)
            adj[dest].append(src)

        print(adj)

obj = sol()
obj.adjacecnyList()