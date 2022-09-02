# get A Lowest Number and A Highest Number and show odd and even numbers between them 
LN = int(input("enter lowest num"))
hN =int(input("enter highest num"))
i=LN
evenNum = []
oddNum = []
while i<hN:
    if i % 2 ==0:
        # print(i,"is a even number") 
        evenNum.append(i)
    else:
        # print(i,"is a odd number") 
        oddNum.append(i)
    i+=1
print("Even Numbers are: ",evenNum)
print("Odd Numbers are: ",oddNum)