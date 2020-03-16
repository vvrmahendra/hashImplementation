class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class Hash:
    def __init__(self, totLen = 7):
        self.totLen = totLen
        self.curLen = 0
        self.arr = [None for i in range(self.totLen)]

    def display(self):
        print("{", end = " ")
        for i in self.arr:
            if i == None:
                pass
            temp = i
            print("---debug")   
            while temp != None:
                print(f"{temp.key} : {temp.val}")
                temp = temp.next
             

        print("}")

    def hashFunc(self, key):
        sum_ = 0
        factor = 1
        key = str(key)
        for i in key:
            sum_ = sum_+ord(i)*factor
            sum_ = sum_%self.totLen
            factor = (factor * 37)%self.totLen

        return sum_
    def insert(self, key, value):
        idx = self.hashFunc(key)
        newNode = Node(key, value)
        if self.arr[idx] == None:
            self.arr[idx] = newNode
        
        else:
            temp = self.arr[idx]
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
        self.curLen += 1
        loadfactor = self.curLen/self.totLen
        if loadfactor > 0.5:
            self.rehash()

        return

    def rehash(self):
        old_size = self.totLen
        self.totLen = self.totLen*2
        # self.arr.extend([None for i in range(old_size)])
        old_arr = [self.arr[i] for i in range(len(self.arr))]
        self.arr = [None for i in range(self.totLen)]
        for i in range(old_size):
            if old_arr[i]:
                temp = old_arr[i]
                while temp:
                    self.insert(temp.key, temp.val)
                    temp = temp.next

        # self.arr = new_arr
        return

    def search(self, key):
        idx = self.hashFunc(key)
        temp = self.arr[idx]
        while temp != None:
            if temp.key == key:
                return temp.val
            temp = temp.next

        return None
    def print_arr(self):
        for i in self.arr:
            if i:
                print(i)

    def get_len(self):
        return self.totLen


if __name__ == "__main__":
    dict_ = Hash()
    dict_.insert("mango", 27)
    dict_.insert("apple", 7)
    dict_.insert("appy", 2)        
    dict_.insert("apipie", 207)
    dict_.insert("banana", 217)
    dict_.insert("bananapie", 271)
    dict_.insert("mangopie", 27)
    dict_.insert("piepie", 272)
    dict_.insert("applepie", 217)
    dict_.insert("api", 27)
    print(dict_.search('apple'))
    # print(dict_.get_len())
    

        
        


