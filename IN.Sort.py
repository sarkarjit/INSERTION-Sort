def insertion_Sort(myList, len):
    for i in range(1, len):
        key=myList[i]
        j=i-1
        while j>=0 and key<mylist[j]:
            mylist[j+1]=mylist[j]
            j-=1
        mylist[j+1]=key

mylist=[]
len = int(input("Enter your size of the list"))

i = 0
for i in range (len):
    temp = int(input())
    mylist.append(temp)

print("Before Sorting.....")
for i in mylist:
    print(i, end=", ")

insertion_Sort(mylist, len)

print("After Sorting.....")
for i in mylist:
    print(i, end=", ")