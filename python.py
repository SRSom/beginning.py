# sorting numbers present in the list using selection  of sort method
def sort(l):
    for i in range(len(l)):
        small = i
        for j in range(i,len(l)):

            if l[small]>l[j]:
               small=j

        t=l[i]
        l[i]=l[small]
        l[small]=t


list=[5,4,2,1,9,0]
sort(list)

print(list)
