class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.children = []
        self.parent = None 
    
    def add_child(self,child):
        child.parent = self 
        self.children.append(child)

    def get_level(self):
        level = 0 
        p = self.parent 
        while p:
            level+=1
            p = p.parent 
        return level  

    def print_tree(self):
        spaces = ' '*self.get_level()*2
        prefix = spaces + "|-"  if self.parent else ""
        print(prefix + self.data)
        if(self.children):
            for child in self.children:
                child.print_tree()



def build_family():
    root = TreeNode('Big Indian Family')

    father = TreeNode('Grandfather')
    mother = TreeNode('GrandMother')

    son = TreeNode('Elder Son')
    younger_son = TreeNode('Younger Son')

    elder_daughter = TreeNode('Elder daughter')
    younger_daughter = TreeNode('Younger daughter')

    root.add_child(father)
    root.add_child(mother)
    father.add_child(son)
    father.add_child(younger_son)
    mother.add_child(elder_daughter)
    mother.add_child(younger_daughter)

    return root

root = build_family()
root.print_tree()