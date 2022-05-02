opção=0
while (int(opção)!=3):
    opção=input('Digite (1) para bits, (2) para números ou (3) para sair: ')
    if(int(opção) == 1):
        numero1 = input('Digite o primeiro número binário [use espaço para separar cada número]: ' )
        vnumero1=numero1.split()
        vet1=list(map(int,vnumero1))
        numero2 = input('Digite o segundo número binário [use espaço para separar cada número]: ' )
        vnumero2= numero2.split()
        vet2=list(map(int,vnumero2))
        vetorRespostaE= []
        vetorRespostaOU=[]
        vetorRespostaXOR=[]
        if (len(vetor1)==len(vetor2)):
            for i in range (len(vetor1)):
                # o vetor para o E
                if ((vetor1[i]==vetor2[i])and(vetor1[i]!=0)):
                    vetorRespostaE.append(1)
                else:
                    vetorRespostaE.append(0)
                # o vetor para o OU
                if ((vetor1[i]==vetor2[i])and(vetor1[i]==0)):
                    vetorRespostaOU.append(0)
                else:
                    vetorRespostaOU.append(1)
                # o vetor para o XOR
                if ((vetor1[i]==vetor2[i])):
                    vetorRespostaXOR.append(0)
                else:
                    vetorRespostaXOR.append(1)
            #resposta dos vetores
            print("Resposta E: " ,vetorRespostaE)
            print("Resposta OU: ",vetorRespostaOU)
            print("Resposta XOR: ",vetorRespostaXOR)
        else:
            print("O tamanho do primeiro e do segundo número são diferentes.")
        
    if(int(opção)==2):
        priNum=input("Indique o primeiro par de números [use espaço para separar cada número]: ")
        secNum=input("Indique o segundo par de números [use espaço para separar cada número]: ")
        vpriNUM=priNum.split()
        vsecNUM=secNum.split()
        vetorPRINUM=list(map(float,vpriNUM))
        vetorSECNUM=list(map(float,vsecNUM))
        fuzzyE=[]
        fuzzyOR=[]
        fuzzyE.append(min(vetorPRINUM))
        fuzzyE.append(min(vetorSECNUM))
        fuzzyOR.append(max(vetorPRINUM))
        fuzzyOR.append(max(vetorSECNUM))
        fuzzyOR.sort()
        fuzzyE.sort()
        print("E Fuzzy= ",fuzzyE)
        print("OR Fuzzy= ",fuzzyOR)
