from json import dumps
class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []
    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}
    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)
    def __lt__(self, other):
        return self.label < other.label
    def __eq__(self, other):
        return self.__dict__() == other.__dict__()
    def from_pov(self, from_node):
        if self.node_exists(from_node) == False:
            raise ValueError('Tree could not be reoriented')
        
        relazione = self.get_relations()
        return self.tree_builder(from_node, relazione, [from_node])
    def tree_builder(self, parent, relazione, nodoUsato):
        tree = Tree(parent)
        for relation in relazione:
            if relation[0] == parent and relation[1] not in nodoUsato:
                nodoUsato.append(relation[1])
                tree.children.append(self.tree_builder(relation[1], relazione, nodoUsato))
            if relation[1] == parent and relation[0] not in nodoUsato:
                nodoUsato.append(relation[0])
                tree.children.append(self.tree_builder(relation[0], relazione, nodoUsato))
        return tree
    def path_to(self, from_node, to_node):
        if self.node_exists(to_node) == False:
            raise ValueError('No path found')
        if self.node_exists(from_node) == False:
            raise ValueError('Tree could not be reoriented')
        tree = self.from_pov(from_node)
        return tree.traverse(to_node, [tree.label])
        
    def traverse(self, target, path):
        if target == self.label:
            return path
        for child in self.children:
            new_path = child.traverse(target, path+[child.label])
            if new_path != None:
                return new_path
        return None
        
    def get_relations(self):
        relations = []
        for child in self.children:
            relations.append((self.label, child.label))
            relations += child.get_relations()
        return relations
    def node_exists(self, node):
        exists = node == self.label
        for child in self.children:
            exists = exists or child.node_exists(node)
            if exists:
                return True
        return exists