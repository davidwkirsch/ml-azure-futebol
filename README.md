# Previsão de Resultados de Jogos com Machine Learning da Azure

Este projeto utiliza o serviço de Machine Learning da Azure para criar um modelo que prevê o resultado de jogos de futebol. Os dados utilizados foram fornecidos pelo site [Base dos Dados](https://basedosdados.org/dataset/c861330e-bca2-474d-9073-bc70744a1b23?table=18835b0d-233e-4857-b454-1fa34a81b4fa).

## Processamento dos Dados

1. **Limpeza dos Dados**:
   - Removi todas as linhas que continham valores em branco para garantir a integridade dos dados.

2. **Criação de Coluna de Resultado**:
   - Adicionei uma coluna indicando o vencedor com base no placar dos jogos.

3. **Separação da Data**:
   - Separei a data em colunas distintas para meses e dias.
   - Criei uma coluna adicional indicando o dia da semana.

4. **Codificação de Strings**:
   - Criei índices para as colunas que continham strings, permitindo que o modelo trabalhasse apenas com números.

## Treinamento do Modelo

Utilizei o serviço de Machine Learning da Azure para treinar o modelo com os dados processados. O objetivo era prever o resultado dos jogos com base nas características fornecidas.

## Resultados

Utilizando os testes para confirmar resultados de jogos passados deu certo, no entanto, após conversar com um amigo que acompanha futebol, ele me apontou que os dados da tabela que usei não estavam muito corretos, e após verificar melhor foi constatado algumas incoerências, como o mesmo nome de técnico para times diferentes no mesmo período.
