fibbonachi=int(input("what do you want the fibbonachi squence to count to? "))
last_last = 0
last = 1

print(last_last)
print(last)
new=0
while new<fibbonachi:
    new=(last_last+last)
    print(last)
    last_last=last
    last=new