from datetime import date
name = ""
usia = 0
def askingforname():
    name = input("masukan nama anda")
    return name
def askingforusia():
    dob = int(input("masukan tahun lahir"))
    currentyear = date.today().year
    usia = currentyear - dob
    return usia
def printresult(name,usia):
    print("nama anda adalah",name,"dan usia anda adalah",usia)
def main():
    name = askingforname()
    usia = askingforusia()
    printresult(name,usia)

main()