cpf = "746.824.890-70"
array_multiplicacoes = []

# Retirada dos pontos e traço
cpf_sem_formatacao = cpf.replace(".", "").replace("-", "")

# Multiplicação dos números do CPF em contagem regressiva a partir de 10
for i in range(len(cpf_sem_formatacao) - 2):
    resultado_multiplicacao = int(cpf_sem_formatacao[i]) * (10 - i)
    array_multiplicacoes.append(resultado_multiplicacao)

# Soma dos resultados das multiplicações
soma_multiplicacoes = sum(array_multiplicacoes)

# Multiplicação do número anterior por 10
multiplicacao_da_soma = soma_multiplicacoes * 10

# Divisão do resultado por 11
resto_da_divisao_por_onze = multiplicacao_da_soma % 11

# Verificação do resto da divisão
if resto_da_divisao_por_onze > 9:
    primeiro_digito_cpf = 0
else:
    primeiro_digito_cpf = resto_da_divisao_por_onze

# Mostrar primeiro dígito na tela
print("O primeiro dígito do CPF é: ", primeiro_digito_cpf)