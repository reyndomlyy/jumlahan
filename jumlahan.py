def jumlahan(x) :
    ''' argumen merupakan bilangan integer '''
    dataList = [1,2,4,4]
    lengthData = len(dataList)
    jml = False
    a = 0
    b = 0
    for i in range(lengthData-1) :
        for j in dataList[i:] :
            if (dataList[i] + j) == x :
                a = dataList[i]
                b = j
                jml = True
                break

    if jml == True :
        print(jml, "("+str(a)+"+"+str(b)+")")
    else :
        print(jml)
        
                
            
    
    
