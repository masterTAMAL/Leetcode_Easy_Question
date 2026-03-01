def largestelement():
    list=[1,5,9,8,10,25,15]
    max=list[0]
    for i in list:
        if i>max:
            max=i
    print("largest element is:-",max)

if __name__=="__main__":
    largestelement()
    
    
#return max
#print(largestelement())