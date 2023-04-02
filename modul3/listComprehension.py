a = [x**2 for x in range(3)]
b = [(x,x**2) for x in range(7)]
c = [x**2 for x in range(15)]
d = [3 for i in range(5)]
e = [[0 for j in range(3)] for i in range(3)]
f = [[1 if j == i else 0 for j in range(3)] for i in range(3)]
vokal = "yogyakarta dan surakarta"
g = [x for x in vokal if x in "aiueoAIUEO"]
def prima(num):
    if num > 1:
        for i in range(2 , num):
            if(num % i ) == 0 :
                return(False)
                break
        else:
            return(True)
    else:
        return(False)
h = [x for x in range (20,50) if prima(x)]
print(h)