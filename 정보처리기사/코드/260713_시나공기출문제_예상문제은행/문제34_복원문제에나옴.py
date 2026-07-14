class Node:
	def __init__(self, value):
		self.value = value
		self.children = []
def tree(li):
	nodes = [Node(i) for i in li]
	# nodes = [Node(3,[]),Node(5,[]),Node(8,[]),Node(12,[]),Node(15,[]),Node(18,[]),Node(21,[])]
	for i in range(1, len(li)):
		nodes[(i - 1) // 2].children.append(nodes[i])
		# nodes[0].children.append(nodes[1]) = Node(3, [Node(5,[])]) 이런 식으로 추가
		# 즉 Node(3, [Node(5,[Node(12,[]),Node(15,[])]), Node(8,[Node(18,[]),Node(21,[])])])
	return nodes[0]
def calc(node, level=0):
	# level이 홀수인 경우에만 value 값을 더함
	# 즉 5 + 8만 됨
	if node is None:
		return 0
	return (node.value if level % 2 == 1 else 0) + sum(calc(n,
		level + 1) for n in node.children)
li = [3, 5, 8, 12, 15, 18, 21]
root = tree(li) # root = Node(3, )
print(calc(root))

# 답
# 13