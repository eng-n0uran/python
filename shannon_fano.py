class Char:
    def __init__(self,name,freq):
        self._name=name
        self._freq=freq
        self._code=""
    def __lt__(self,other):
        return True if self._freq<other.get_freq()else False
    def __str__(self):
        return "{0}\t {1}\t {2}".format(self._name,str(self._freq),self._code)
    def get_freq(self):
        return self._freq
    def get_code(self):
        return self._code
    def append_code(self,code):
        self._code+= str(code)
def find_middle(lst): 
# s= total k= first half b= second half
# p=  frequancy of elements in the first half of list j= frequancy of elements in the second half in the list
    if len(lst)==1: return None
    s=k=b=0
    for p in lst: s+=p.get_freq()
    s /=2
    for p in range(len(lst)):
        k+=lst[p].get_freq()
        if k==s:return p
        elif k>s :
          j=len(lst)-1
          while b<s:
            b+= lst[j].get_freq()
            j-=1
        return p if abs(s-k)< abs(s-b)else j
def shannon_fano(lst):
    middle= find_middle(lst)
    if middle is None: return
    for i in lst[: middle + 1]:
        i.append_code(0)
    shannon_fano(lst[: middle + 1])
    for i in lst[middle + 1:]:
        i.append_code(1)
    shannon_fano(lst[middle + 1 :])    
    
def output():
    lst=list()
    lst.append(Char('A',0.22))
    lst.append(Char('B',0.28))
    lst.append(Char('C',0.15))
    lst.append(Char('D',0.30))
    lst.append(Char('E',0.05))
    
    lst.sort(reverse=True)
    shannon_fano(lst)
    print('char','freq','code')
    for c in lst:
        print(c)

output()


   
    
