casaWilliams=[
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
]
for i in range(0,len(casaWilliams)):
    for j in range (0,len(casaWilliams[i])):
        casaWilliams[i][j]='1'
        casaWilliams[i][i] ='0'

        print(casaWilliams)