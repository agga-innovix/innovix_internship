class A:
    def do_something(self,x,y):
        z = x+y

        return self.sample(z)

    def sample(self,z):
        return z

if __name__ == '__main__':
    a = A()
    x,y=10,35
    a.do_something(x,y)