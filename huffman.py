#huffman coding
class node:
    def __init__(self,freq,symbol,left=None,right=None):
        # freq of symbol
        self.freq=freq
        #symbol name (character)
        self.symbol=symbol
        # node left
        self.left=left
        # node right
        self.right=right
        #tree direction(0/1)
        self.huff=''
        
def printNodes(node,val=''):
    #huffman code for the current node
    newval=val+str(node.huff)
    #print(new val)
#if node isnot an edge node then traverse inside it    
    
    if(node.left):
        printNodes(node.left,newval)
    if(node.right):
        printNodes(node.right,newval)
 #if node is edge node then display its huffman code       
        
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newval}")
   
#characters of huffman tree
chars=['a','b','c','d','e','f']
#freq of characters
freq=[5,9,12,13,16,45]
# list  for unused node
nodes=[]
#converting  characters and frequancies  into huffman tree
for x in range(len(chars)):
    y=node(freq[x],chars[x])
    nodes.append(y)
    # build huffman tree
while len(nodes)>1:
    #sort all nodes in assending sort 
    #based on their freq
    nodes =sorted(nodes,key=lambda x: x.freq)
    #pick two smallest nodes
    left=nodes[0]
    right=nodes[1]
# asign directional values to these nodes
    left.huff=0
    right.huff=1   
 #combain the two smallest nodes
#new node as their parent  
    newNode=node(left.freq+right.freq, left.symbol+right.symbol, left, right)
  #remove the 2 nodes and add parent as new node among others 
   
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)
   #huffman tree is ready
printNodes(nodes[0])
 

   
   
   
   
    

