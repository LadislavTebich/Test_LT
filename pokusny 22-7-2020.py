f = [0,1]
print(f[0])
print(f[1])
for i in range (2,20):
    f.append(f[i-2]+f[i-1])
    print(f[i])

