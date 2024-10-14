Q = int(input('Cidadãos: '))

if Q < 4 and Q > 233000:
    print('Valor inválido!')
    Q = int(input('Digite novamente: '))
   
else:
    Vi = list(map(int,input('Digite 1 ou 0: ').split()))[:Q]
    
    S = 0
    N = 0
    for i in Vi:
        if i == 0:
            S += 1
        elif i == 1:
            N += 1
            
    if S > N:
        print(S)
    elif N > S:
        print(N)
    else:
        print('Empate')