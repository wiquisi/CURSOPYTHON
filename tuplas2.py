casaDiego=[
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
]
contador=4
for i in range(0,len(casaDiego)):
    for j in range (0,len(casaDiego[i])):
        casaDiego[i][j] ='1'
        casaDiego[i][i]='0'
        casaDiego[i][contador]='0'
    if contador>=0:
            contador=contador-1
    print(casaDiego[i], end='\n')