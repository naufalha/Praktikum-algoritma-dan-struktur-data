num = int (input("masukan angka :"))
def prima(num):
    if num > 1:
        for i in range(2 , num):
            if(num % i ) == 0 :
                print(num,"bukan bilangan prima")
                return(False)
                break
        else:
            return(True)
    else:
        return(False)

 