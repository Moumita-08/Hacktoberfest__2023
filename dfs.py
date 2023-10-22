print("The given graph is ")
print("\n")
print("      1")
print("     / \ ")
print("    2   3")
print("     \ / \ ")
print("      4   7")
print("     / \ ")
print("    5   6")

n=int (input("Enter the number of elements in the tree: "))
graph={
    '1':['2','3'],
    '2':['4'],
    '3':['4','7'],
    '4':['5','6'],
    '5':[],
    '6':[],
    '7':[]
}
visited=set()
def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        def search(root):
            l=[]
            for i in range(0,n):
                l.append(root)
                print(l)
        visited.add(root)
        for sub_root in graph [root]:
            dfs(visited,graph,sub_root)
dfs(visited,graph,'1')
search(root)
