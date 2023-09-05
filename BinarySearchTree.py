# создаем класс единичного узла дерева
class node:

    def __init__(self, node_value, left_value=None, right_value=None, parent=None):
        self.left = left_value # левый ребенок текущего узла
        self.right = right_value # правый ребенок текущего узла
        self.value = node_value # значение текущего узла
        # self.key = key
        self.parent = parent # предок текущего узла

# создаем класс бинарного дерева поиска
class binary_search_tree:

    def __init__(self):
        self.root = None # корень дерева

# метод поиска элемента по его значению. Передаем два параметра: исходный узел и значение искомого
    def search_node(self, node, k):
        if node is None or node.value == k:
            return node
        elif k < node.value:
            return self.search_node(node.left, k)
        else: 
            return self.search_node(node.right, k)

# поиск минимального значения дерева. Оно будет в нижнем левом узле или в корне
    def search_min(self, node):
        if node.left == None:
            return node
        return self.search_min(node.left)

# поиск максимального значения дерева. Оно будет в нижнем правом узле или в корне
    def search_max(self, node):
        if node.right == None:
            return node
        return self.search_max(node.right)

# метод добавления нового узла. Ищем место вставки нового ущла, новые узлы крепятся к существующим листам    
    def insert(self, node):
        y = None # переменная для поиска места для вставки
        x = self.root # находим корень, если он есть. если нет, создаеи его
        while x != None:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node 

# метод замены двух узлов. нужен для метода удаления
    def transplant(self, replace_node, new_node):
        if replace_node.parent == None:
            self.root = new_node # если у заменияемой ноды нет родителя, делаем родителем новую узел
        elif replace_node == replace_node.parent.left:
            replace_node.parent.left = new_node
        else:
            replace_node.parent.right = new_node
        if new_node != None:
            new_node.parent = replace_node.parent

# метод удаления.
    def remove(self, remove_node):
        if remove_node.left == None:
            self.transplant(remove_node, remove_node.right)
        elif remove_node.right == None:
            self.transplant(remove_node, remove_node.left)
        else:
            y = self.search_min(remove_node.right) # хранит в себе минимум поддерева, то есть либо нижний левый лист, либо корень поддерева
            if y.parent != remove_node:
                self.transplant(y, y.right)
                y.right = remove_node.right
                y.right.parent = y
            self.transplant(remove_node, y)
            y.left = remove_node.left
            y.left.parent = y

# симметричный обход.
    def in_order(self, root):
        res = []
        if root:
            res = self.in_order(root.left)
            res.append(root.value)
            res = res + self.in_order(root.right)
        return res

# обход в прямом порядке
    def pre_order(self, root):
        res = []
        if root:
            res.append(root.value)
            res = res + self.pre_order(root.left)
            res = res + self.pre_order(root.right)
        return res

# обход в обратном порядке 
    def post_order(self, root):
        res = []
        if root:
            res = self.post_order(root.left)
            res = res + self.post_order(root.right)
            res.append(root.value)
        return res    


# создание дерева и добавление в нео новых элементовв
tree = binary_search_tree()
node1 = node(8)
node2 = node(3)
node3 = node(1)
node4 = node(6)
node5 = node(4)
node6 = node(7)
node7 = node(5)
node8 = node(2)
node9 = node(10)
node10 = node(14)
node11 = node(13)
tree.insert(node1)
tree.insert(node2)
tree.insert(node3)
tree.insert(node4)
tree.insert(node5)
tree.insert(node6)
tree.insert(node7)
tree.insert(node8)
tree.insert(node9)
tree.insert(node10)
tree.insert(node11)

# demo функций
tree.remove(node6)
print(tree.search_node(node1, 7))
print(tree.in_order(node1))
print(tree.pre_order(node1))
print(tree.post_order(node1))
