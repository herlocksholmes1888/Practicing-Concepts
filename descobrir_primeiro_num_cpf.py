cpf = "746.824.890-70"
cpf_sem_formatacao = cpf.replace(".", "").replace("-", "")
 
array_multiplicacoes = []
for i in range(9):  
    resultado_multiplicacao = int(cpf_sem_formatacao[i]) * (10 - i)
    array_multiplicacoes.append(resultado_multiplicacao)
 
soma_multiplicacoes = sum(array_multiplicacoes)
primeiro_digito_calculado = (soma_multiplicacoes * 10) % 11
primeiro_digito_calculado = 0 if primeiro_digito_calculado > 9 else primeiro_digito_calculado
 
primeiro_digito_real = int(cpf_sem_formatacao[9])
if primeiro_digito_calculado == primeiro_digito_real:
    print(f"O primeiro dígito verificador está correto: {primeiro_digito_calculado}")
else:
    print(f"Erro: dígito calculado ({primeiro_digito_calculado}) não corresponde ao real ({primeiro_digito_real}).")