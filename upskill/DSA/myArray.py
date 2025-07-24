import ctypes

class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0

        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n
    
    def append(self,item):
        
        if self.n == self.size:
        
            self.__resize(self.size*2)

        self.A[self.n] = item
        self.n = self.n + 1 

    def __resize(self,new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of old array to new one
        for i in range(self.n):
            B[i] = self.A[i]
            # reassign A
            self.A = B


    def __getitem__(self,index):

        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'IndexError'

    def __delitem__(self,pos):
        # delete pos wala item
        if 0<= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]

        self.n = self.n - 1

    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'


    def pop(self):
        if self.n == 0:
            return 'Empty List'
        print(self.A[self.n-1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):

        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - not in list'

    def insert(self,pos,item):

        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1

    def remove(self,item):
        # search and get pos
        pos = self.find(item)
        if type(pos) == int:
        # delete
            self.__delitem__(pos)
        else:
            return pos


    def __make_array(self, capacity):
        return (capacity*ctypes.py_object)()
    

l = MyList()
print(l.__str__())
print(l.__len__())
l.append(3)
l.append(3)
print(l.__getitem__(1))
print(l.__str__())
print(l.__len__())

