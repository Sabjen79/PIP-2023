
class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        value = self.stack[len(self.stack)-1]
        self.stack = self.stack[:-1]
        return value
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack)-1]
    
s = MyStack()
s.push(1)
s.push(2)
print(s.pop())
print(s.peek())

#========================================

class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        value = self.queue[0]
        self.queue = self.queue[1:]
        return value
    
    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]
    

q = MyQueue()
q.push(10)
q.push(20)
q.push(30)
print(q.pop())
print(q.peek())

#========================================

class Matrix:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.mat = [None] * N * M

    def get(self, x, y):
        if x >= self.N or y >= self.M:
            raise Exception("Wrong indeces")
        return self.mat[x * self.M + y]
    
    def set(self, x, y, item):
        self.mat[x * self.M + y] = item

    def transpose(self):
        new_mat = Matrix(self.M, self.N)

        for i in range(self.N):
            for j in range(self.M):
                new_mat.set(j, i, self.mat[i*self.M + j])

        return new_mat

    def iterate(self, func):
        for i in range(self.N):
            for j in range(self.M):
                self.mat[i*self.M + j] = func(self.mat[i*self.M + j])

    def multiply(self, b):
        new_mat = Matrix(self.N, b.M)

        for i in range(self.N):
            for j in range(b.M):
                num = 0
                for k in range(self.M):
                    num += self.get(i, k) * b.get(k, j)
                new_mat.set(i, j, num)
        
        return new_mat

    def __str__(self):
        s = ""
        for i in range(self.N):
            s += " ".join([str(self.mat[self.M*i + x]) for x in range(self.M)])
            if i != self.N - 1:
                s += '\n'
        return s
    
mat = Matrix(3, 5)

for i in range(3):
    for j in range(5):
        mat.set(i, j, i*5+j+1)


print(mat)
print(mat.get(2, 1))

mat = mat.transpose()
print(mat)

print(mat.get(4, 2))

mat.iterate(lambda a: a*2)
print(mat)
mat.iterate(lambda a: a/2)
mat = mat.transpose()
print(mat.multiply(mat.transpose()))
