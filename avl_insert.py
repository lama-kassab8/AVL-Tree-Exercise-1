class Node:
    def __init__(self, data):
        self.data = data
        self.left= None
        self.right= None
        self.height= 1 # every new node starts at height 1


class AVLTree:
    def __init__(self):
        self.root= None

    def get_height(self, node):
        if not node: # if the node is None, return height 0 as there's no height to measure
            return 0
        return node.height
    
    def balance_factor(self,node):
        if not node: # if there are no nodes in the tree, it means the tree is perfectly balanced
            return 0
        return self.get_height(node.left)- self.get_height(node.right) # if there are nodes in the tree, calculate the tree's height difference between the left and the right subtrees by subtracting the height of the right subtree from the height of the left subtree
    
    # the right_rotation method is used in case the tree is unbalanced due to the fact that left subtree being too tall
    def right_rotation(self, y):
        x = y.left # make x the left child of the node y
        T2 = x.right # store the right child of x in T2

        x.right= y # by making y the right child of x, the rotation is performed
        y.left = T2 # now T2 is the left child of y
        # update the height of both x and y nodes
        y.height=  1 + max(self.get_height(y.left), self.get_height(y.right) )
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x # return the new root(x)

    # the left_rotation method is used in case the tree is unbalanced due to the fact that the right subtree is too tall
    def left_rotation(self, y):
        x= y.right # make x the right child of the node y
        T2= x.left # store the left child of x in T2

        x.left= y # by making y the left child of x, the left rotation is performed
        y.right= T2 # now T2 is the right child of y
        # update the heights os both x and y
        y.height=  1 + max(self.get_height(y.left), self.get_height(y.right) )
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x # return the new root (x)
    
    # the rebalance method is used in case the tree is unbalanced and rotations need to be performed to restore the balance
    def rebalance(self, node):
        balance = self.balance_factor(node) # calculate the balance factor of the node

        if balance > 1 and self.balance_factor(node.left) >= 0: # if the left subtree is too heavy and the left child of the node is balanced or has a heavy left subtree:
            return self.right_rotation(node) # do right rotation on the node
        
        if balance > 1 and self.balance_factor(node.left) < 0: # if the left subtree is too heavy and the left child of the node is right heavy: 
            node.left= self.left_rotation(node.left) # left rotate the left child so it doesn't remain right heavy
            return self.right_rotation(node) # do a right rotation on the node
        
        if balance < -1 and self.balance_factor(node.right) <=0: # if the right subtree is too heavy and the right child of the node is balanced or has a heavy right subtree:
            return self.left_rotation(node) # do left rotation on the node
        
        if balance < -1 and self.balance_factor(node.right) > 0: # if the right subtree is too heavy and the right child of the node is left heavy:
            node.right= self.right_rotation(node.right) # right rotate the right child so it doesn't remain left heavy
            return self.left_rotation(node) # do left rotation on the node
        
        return node
    
    def insert_root(self, data):
        self.root= self.insert(self.root,data) # when adding a node to an empty tree, make the new node the root
    
    def insert(self, node, data):
        if not node: # if an empty spot is reached, place the new node in this empty spot
            return Node(data)
        elif data < node.data: # if the data of the new node is less than the value of the current node
            node.left = self.insert(node.left,data) # insert the new node as the left child of the current node as long as the current node doesn't have a left child, else, keep recursively calling this insert method till an empty spot as a left child is found
        else: # else it means the data is bigger than the value of the current node
            node.right= self.insert(node.right,data) # insert the new node as the right child of the current node as long as the current node doesn't have a right child, else, keep recursively calling this insert method till an empty spot as a right child is found

        # update the height after each node added
        node.height= 1 + max(self.get_height(node.left), self.get_height(node.right))

        # rebalance the node by calling the rebalance method
        return self.rebalance(node)
    
    # the get_min method finds the smallest value in the tree by keeping on going left, till the leftmost node is reached
    def get_min(self, node):
        while node.left:
            node= node.left
        return node
    
    def delete_node(self, node):
        if not node.left and not node.right: # if the node has no children, just remove it
            return None
        elif not node.left: # if the node doesn't have a left child
            return node.right # remove the node and make the right child take its place
        elif not node.right: # if the node doesn't have a right child
            return node.left # remove the node and make the left child take its place
        else: # if the node has right and left children:
            successor= self.get_min(node.right) # call the get_min method to find the smallest value in the right subtree and store this value in successor
            node.data= successor.data # copy the successor's data to the current node
            node.right= self.delete(node.right, successor.data) # start from the right child and go through this method again till the successor's node is found and deleted
            # the reason we need to recursively call this method to delete the successor is because the successor might have a child, so if it does, the code in this method deletes the successor and handles its child
    
            return node
    def delete(self, node, key):
        if not node: # if the key we want to delete is not found, return None
            return None
        
        if key < node.data: # if the key is less than the value of the node, check its left child
            node.left= self.delete(node.left, key) # recursively check if the value of the left child is the same as the key, else, continue with this method and repeat till key is found
        elif key > node.data: # if the key is greater than the value of the node, check its right child
            node.right= self.delete(node.right, key)# recursively check if the value of the right child is the same as the key, else, continue with this method and repeat till key is found
        else:
            node= self.delete_node(node) # if the value of the current node is the same as key, delete it by calling the delete_node method
        # after deletion, if the subtree is now empty, stop here as there are nothing to rebalance
        if not node:
            return None
        # update the height
        node.height= 1 +max(self.get_height(node.left), self.get_height(node.right))
        return self.rebalance(node) # in case the tree needs to be rebalanced



# TEST RUN FOR THE AVL TREE

# helper function to print the tree in sorted order
def print_inorder(node):
    # print the values of the tree using inorder traversal (left → root → right).
    if node is not None:
        print_inorder(node.left)
        print(node.data, end=" ")
        print_inorder(node.right)

# create a new AVL Tree
avl = AVLTree()
root = None  # start with an empty tree

# step 1: insert values into the tree
print("Step 1: Inserting values into the AVL tree...")
values_to_insert = [10, 20, 30, 40, 50, 25]
for value in values_to_insert:
    root = avl.insert(root, value)

# step 2: show the tree after insertions
print("\nTree after insertions (inorder traversal):")
print_inorder(root)  # This should print: 10 20 25 30 40 50
print("\n")

# step 3: delete a value from the tree
print("Step 3: Deleting a value from the tree...")
value_to_delete = 20
root = avl.delete(root, value_to_delete)

# step 4: show the tree after deletion
print("\nTree after deleting 20 (inorder traversal):")
print_inorder(root)  # This should print: 10 25 30 40 50
print("\n")