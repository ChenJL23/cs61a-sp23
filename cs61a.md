### lab02

```python
n = 7

def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)

f = f(g, n)
g = (lambda y: y())(f)
```

#### 环境图表

<iframe width="1000" height="700" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=n%20%3D%207%0A%0Adef%20f%28x%29%3A%0A%20%20%20%20n%20%3D%208%0A%20%20%20%20return%20x%20%2B%201%0A%0Adef%20g%28x%29%3A%0A%20%20%20%20n%20%3D%209%0A%20%20%20%20def%20h%28%29%3A%0A%20%20%20%20%20%20%20%20return%20x%20%2B%201%0A%20%20%20%20return%20h%0A%0Adef%20f%28f,%20x%29%3A%0A%20%20%20%20return%20f%28x%20%2B%20n%29%0A%0Af%20%3D%20f%28g,%20n%29%0Ag%20%3D%20%28lambda%20y%3A%20y%28%29%29%28f%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=18&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>



### lab04

```python
def virfib_sq(n):
    print(n)
    if n <= 1:
        return n
    return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2

r4 = virfib_sq(4)
```



<iframe width="1000" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20virfib_sq%28n%29%3A%0A%20%20%20%20print%28n%29%0A%20%20%20%20if%20n%20%3C%3D%201%3A%0A%20%20%20%20%20%20%20%20return%20n%0A%20%20%20%20return%20%28virfib_sq%28n%20-%201%29%20%2B%20virfib_sq%28n%20-%202%29%29%20**%202%0A%20%20%20%20%0Ar4%20%3D%20virfib_sq%284%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>