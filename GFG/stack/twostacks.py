class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * n
        self.mid = n // 2
        
        # top1 starts from 0
        self.top1 = -1      
        
        # top2 starts from mid
        self.top2 = self.mid - 1  

    def push1(self, x):
        if self.top1 == self.mid - 1:
            
            # top1 reaches middle of the array
            # so stack1 is full
            return
        self.top1 += 1
        self.arr[self.top1] = x

    def push2(self, x):
        if self.top2 == self.size - 1:
            
            # top2 reaches end of the array
            # so stack2 is full
            return
        self.top2 += 1
        self.arr[self.top2] = x

    def pop1(self):
        if self.top1 == -1:
            
            # that means stack in empty so return -1
            return -1
        ele = self.arr[self.top1]
        self.top1 -= 1
        return ele

    def pop2(self):
        if self.top2 == self.mid - 1:
            
            # that means stack in empty so return -1
            return -1
        ele = self.arr[self.top2]
        self.top2 -= 1
        return ele


if __name__ == '__main__':
    ts = TwoStacks(5)
    ts.push1(2)
    ts.push1(3)
    ts.push2(4)
    print(ts.pop1(), end=' ')
    print(ts.pop2(), end=' ')
    print(ts.pop2(), end=' ')