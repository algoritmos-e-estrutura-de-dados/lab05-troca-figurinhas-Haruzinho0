def maximizar_troca_de_figurinhas(figurinha_Maria, figurinha_Joao, A, B):

    indice_Maria = 0
    indice_Joao = 0 
    i = 0
    j = 0
    m = 0
    n = 0

    for i in range(int(A)):
      for j in range(int(B)):
        if figurinha_Maria[i] == figurinha_Joao[j]:
          indice_Maria += 1
 
    for m in range(int(B)):
      for n in range(int(A)):
        if figurinha_Joao[m] == figurinha_Maria[n]:
          indice_Joao += 1
   
    if (int(A) - int(indice_Maria)) < (int(B) - int(indice_Joao)):
        return print(f"O máximo de figurinhas para troca é:{int(A) - int(indice_Maria)}")
    else:
        return print(f"O máximo de figurinhas para troca é:{int(B) - int(indice_Joao)}")

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao, A, B)