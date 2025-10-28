#celebrity-> sab celebrity ko jante hai or celebrity kise ko na janta ho

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if(self.is_empty()):
            return "empty stack"
        else:
            data = self.top.data
            self.top = self.top.next
            return data 
    
    def is_empty(self):
        return self.top == None
    
    def size(self):
        temp = self.top
        counter = 0
        while temp != None:
            counter +=1
            temp = temp.next
        return counter    


    def traverse(self):
        temp = self.top

        while temp != None:
            print(temp.data)
            temp = temp.next

L = [
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0],
]
def find_celebrity(L):
    s = Stack()

    for i in range(len(L)):
        s.push(i)
    
    while s.size() >=2:
        i = s.pop()
        j = s.pop()

        if L[i][j] == 0:   # i j ko nhi janta yani ki j is not a celebrity
            s.push(i)
        else:
            # i is not a celebrity
            s.push(j)
    
    celeb = s.pop()

    # to check the remain one person in stack is celebrity or not(mateb jo bacha hai usko sab jante hai or bo kise ko nhi janta hai)

    for i in range(len(L)):
        if i != celeb:  # khud ka khud se relation ke alawa
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                print("no one is a celebrity")
                return
    
    print("the celebrity is:", celeb)

find_celebrity(L)
