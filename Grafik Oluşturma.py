import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(dependencies: dict, filename: str):
    G = nx.DiGraph()
    for pkg, deps in dependencies.items():
        G.add_node(pkg)
        for dep in deps:
            G.add_edge(pkg, dep)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="skyblue")
    plt.savefig(filename)
    plt.close()