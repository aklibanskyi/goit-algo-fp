import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#1296F0"
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show(block=False)
    plt.pause(2)
    plt.close()

def generate_color(step, total_steps):
    """Генерує колір від темного синього до світлого синього (hex)."""
    # Змінюємо Lightness від 0.2 (темний) до 0.8 (світлий)
    l = 0.2 + (0.6 * (step / max(1, total_steps - 1)))
    r, g, b = colorsys.hls_to_rgb(0.55, l, 0.9) # 0.55 - синій відтінок
    return f"#{int(r*255):02X}{int(g*255):02X}{int(b*255):02X}"

def count_nodes(root):
    if not root: return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def dfs_visualize(root):
    """Обхід у глибину (DFS) з використанням стека."""
    if not root: return
    total = count_nodes(root)
    stack = [root]
    step = 0
    
    while stack:
        node = stack.pop()
        node.color = generate_color(step, total)
        step += 1
        
        # Додаємо правого, потім лівого, щоб лівий оброблявся першим
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
        
    draw_tree(root, "DFS (У глибину)")

def bfs_visualize(root):
    """Обхід у ширину (BFS) з використанням черги."""
    if not root: return
    
    # Скидаємо кольори перед новим обходом
    queue = [root]
    while queue:
        n = queue.pop(0)
        n.color = "skyblue"
        if n.left: queue.append(n.left)
        if n.right: queue.append(n.right)
        
    total = count_nodes(root)
    queue = [root]
    step = 0
    
    while queue:
        node = queue.pop(0)
        node.color = generate_color(step, total)
        step += 1
        
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
        
    draw_tree(root, "BFS (У ширину)")

# --- Тестування Завдання 5 ---
if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    
    dfs_visualize(root)
    bfs_visualize(root)
