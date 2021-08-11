def remove (data):
    count=0
    size = len(data)
    for i in range(0, size-1):
        if(data[i]==-1):
            count+=1
    for i in range(0, count+1):
        data.remove(-1)

    return (data)
    
