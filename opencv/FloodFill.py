def check(j,i):
    try:
        if pix[j,i] == 0 and matrix[j][i] != -1:
            return True
        else:
            return False
    except:
        return False
                
def juli(r,s):
    return abs(r[0]-s[0])+abs(r[1]-s[1])+abs(r[2]-s[2])
    
for i in range(w):
    for j in range(h):
        r = [0,0,0]
        s = [0,0,0]
        if pix[j,i] == 0:
            if check(j-1,i):
                r[0],r[1],r[2] = im2.getpixel((j,i)) 
                s[0],s[1],s[2] = im2.getpixel((j-1,i))
                print r
                print s
                print "-"*55
                if juli(r,s) <=l:
                    matrix[j][i] = matrix[j-1][i]
                    maps[str(matrix[j][i])]+=1
            elif check(j-1,i-1):
                r[0],r[1],r[2] = im2.getpixel((j,i)) 
                s[0],s[1],s[2] = im2.getpixel((j-1,i-1))
                if juli(r,s) <=l:
                    matrix[j][i] = matrix[j-1][i-1]
                    maps[str(matrix[j][i])]+=1
            elif check(j,i-1):
                r[0],r[1],r[2] = im2.getpixel((j,i)) 
                s[0],s[1],s[2] = im2.getpixel((j-1,i))
                if juli(r,s) <=l:
                    matrix[j][i] = matrix[j][i-1]
                    maps[str(matrix[j][i])]+=1
            elif check(j+1,i+1):
                r[0],r[1],r[2] = im2.getpixel((j,i)) 
                s[0],s[1],s[2] = im2.getpixel((j+1,i+1))
                if juli(r,s) <=l:
                    matrix[j][i] = matrix[j+1][i+1]
                    maps[str(matrix[j][i])]+=1
            elif check(j,i+1):
                r[0],r[1],r[2] = im2.getpixel((j,i)) 
                s[0],s[1],s[2] = im2.getpixel((j,i+1))
                if juli(r,s) <=l:
                    matrix[j][i] = matrix[j][i+1]
                    maps[str(matrix[j][i])]+=1
            elif check(j-1,i+1):
                pr[0],r[1],r[2] = im2.getpixel((j,i)) 
                s[0],s[1],s[2] = im2.getpixel((j-1,i+1))
                if juli(r,s) <=l:
                    matrix[j][i] = matrix[j-1][i+1]
                    maps[str(matrix[j][i])]+=1
            elif check(j+1,i-1):
                r[0],r[1],r[2] = im2.getpixel((j,i)) 
                s[0],s[1],s[2] = im2.getpixel((j+1,i-1))
                if juli(r,s) <=l:
                    matrix[j][i] = matrix[j+1][i-1]
                    maps[str(matrix[j][i])]+=1
            elif check(j+1,i):
                r[0],r[1],r[2] = im2.getpixel((j,i)) 
                s[0],s[1],s[2] = im2.getpixel((j+1,i))
                if juli(r,s) <=l:
                    matrix[j][i] = matrix[j+1][i]
                    maps[str(matrix[j][i])]+=1
            else:
                n+=1
                maps[str(n)]=1
                matrix[j][i] = n

for i in range(w):
    for j in range(h):
        if matrix[j][i]!=-1 and maps[str(matrix[j][i])]<=2:
            im.putpixel((j,i),255)