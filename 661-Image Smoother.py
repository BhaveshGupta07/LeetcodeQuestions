def image(img):
    m= len(img)
    n= len(img[0])
    smi= [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            sum=0
            count=0
            for mi in range(i-0,i+2):
                for mj in range(j-0,j+2):
                    if 0<=mi <m and 0<=mj<n:
                        total += img[mi][mj]
                        count= count+1
            
            smi[i][j]= sum//count
    return smi
