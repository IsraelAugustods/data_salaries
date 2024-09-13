[![author](https://img.shields.io/badge/author-IsraelAugustods-red.svg)](https://www.linkedin.com/in/israelaugustoalmeida/) ![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
# Salário na Área de Dados

<p align="center">
  <img alt="data" width="60%" src="https://s3.amazonaws.com/ibc-portal/wp-content/uploads/2021/06/21123308/perguntar-salario-entrevista.jpg">
</p>

## Objetivo do Estudo
Este estudo tem como foco a análise de salários na área de dados, com o objetivo de gerar insights e responder a perguntas de negócio.

## Fonte dos Dados

Todos os dados utilizados neste projeto foram obtidos de um dataset disponível no [***Kaggle***](https://www.kaggle.com/), acessível [neste link](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries?select=ds_salaries.csv).

O ***Kaggle*** é uma plataforma online voltada para a comunidade de ciência de dados e aprendizado de máquina. Fundada em 2010, o Kaggle permite que usuários de todos os níveis de habilidade participem de competições, acessem datasets gratuitos, pratiquem e desenvolvam habilidades em ciência de dados, além de colaborar com outros membros da comunidade.

## Tecnologias Utilizadas
<p align="left">  
  <a href="https://www.microsoft.com/pt-br/microsoft-365/excel" rel="noreferrer"> <img src="https://marcas-logos.net/wp-content/uploads/2019/11/microsoft-excel-logo.jpg" alt="excel" width="30" height="30"/> </a> 
  <a href="https://www.jamovi.org/"> <img src="https://upload.wikimedia.org/wikipedia/commons/2/26/Jamovi_logo.png" alt="jamovi" width="30" height="30"/> </a> 

## Destaques do Projeto

### Distribuição de tipos de trabalho (Mais de 1000 pessoas atuando)

Neste conjunto de dados, observei que há uma maior representação de Data Engineers, seguidos por Data Scientists e, por último, Data Analysts. Isso pode refletir tanto a demanda do mercado quanto a amostragem disponível para cada uma dessas profissões.

<p align="center">
  <img alt="g1" width="50%" src="https://github.com/user-attachments/assets/b8e2c32e-2db6-4734-a9ca-9580497bc77a">
</p>


### Média Salarial por Nível de Experiência e Tamanho da Empresa						

Com a análise desse gráfico, observei que o nível Executive apresenta consistentemente os maiores salários em todas as categorias (L, M, S). Para as categorias L e M, os salários de Mid-level e Senior estão muito próximos, o que sugere que, dependendo do setor ou do tamanho da empresa, a diferença entre esses dois níveis de experiência pode ser mínima. Além disso, o nível Entry-level possui os menores salários em todas as categorias.

<p align="center">
  <img alt="g1" width="50%" src="https://github.com/user-attachments/assets/9979182d-a24d-4052-a129-60ba6adc83d4">
</p>




## Estatística

###  Um cientista de dados ganha mais, em média, do que um analista de dados?

<p align="center">
  <img alt="t1" width="50%" src="https://github.com/user-attachments/assets/fb39bfd0-7659-47f2-895a-d5e3c4c3a64f">
</p>

Ao analisar a tabela acima, parece que os cientistas de dados ganham mais. No entanto, eu precisei realizar uma análise estatística para confirmar essa suposição.

Como meu objetivo era descobrir se, na média, os cientistas de dados ganham mais do que os analistas de dados, apliquei o **teste t**. Esse teste possui alguns pressupostos, como a **distribuição normal dos dados** e a **homogeneidade das variâncias**. Dependendo do resultado desses pressupostos, diferentes variações do teste t podem ser aplicadas.

Primeiro, verifiquei a normalidade dos dados aplicando o teste de **Kolmogorov-Smirnov**, e obtive o seguinte resultado:

<p align="center">
  <img alt="r1" width="50%" src="https://github.com/user-attachments/assets/281f5c10-5916-420d-8399-68129cc0baf4">
</p>

Com base nessa tabela, concluo que os dados **não possuem distribuição normal**, já que o p-valor foi menor que 0,05, o que me levou a rejeitar a hipótese nula (que os dados são normais).

Apesar da ausência de normalidade nos dados, apliquei o **Teorema do Limite Central** (TLC), uma vez que estou lidando com um número considerável de dados. Isso me permitiu considerar que, na média, a distribuição segue uma normalidade.

Ao utilizar o TLC, é essencial analisar os gráficos de frequência ou densidade de cada variável:

<p align="center">
  <img alt="r2" width="50%" src="https://github.com/user-attachments/assets/5393afee-f91a-459a-b94b-61ca48a69135">
</p>

Escolhi o teste de **Kolmogorov-Smirnov** devido à grande quantidade de dados. Caso eu estivesse trabalhando com menos amostras, o **teste de Shapiro-Wilk** seria mais adequado.

Em seguida, conferi a **homogeneidade das variâncias** utilizando o **teste de Levene**, e obtive o seguinte resultado:

<p align="center">
  <img alt="r3" width="50%" src="https://github.com/user-attachments/assets/0ff32d49-40d0-4d3e-9f14-f88f80918b6b">
</p>

O teste revelou que as variâncias dos dois grupos são **estatisticamente diferentes**, já que o p-valor foi menor que 0,05, o que me levou a rejeitar a hipótese nula (de que há homogeneidade nas variâncias).

Gostaria de salientar que apliquei esses testes em **amostras independentes**, ou seja, estou comparando dois grupos distintos: **Data Scientists** e **Data Analysts**.

Diante dos resultados (distribuição normal dos dados, mas variâncias diferentes), optei por utilizar o **teste t de Welch**, ajustado para diferenças nas variâncias:

<p align="center">
  <img alt="r4" width="50%" src="https://github.com/user-attachments/assets/82c1c0e4-105c-44f7-8123-7baa2df9f5d5">
</p>

Com isso, concluo que **os cientistas de dados ganham mais que os analistas de dados**, em média, nesse conjunto de dados. O p-valor do **teste t de Welch** foi menor que 0,05, o que me levou a rejeitar a hipótese nula (de que os cientistas de dados ganham menos ou igual aos analistas de dados).


## Considerações finais

É essencial reconhecer o papel crucial da estatística para um analista de dados. A estatística não apenas ajuda a interpretar dados de maneira eficaz, mas também fornece as ferramentas necessárias para revelar insights profundos e responder a perguntas de negócios com precisão. Sem ela tudo estaria no campo do "achismo". 
Com uma base de dados como essa, é possível gerar diversos insights valiosos. Aqui, trouxe somente dois que julguei mais interessantes. Para acessar meu trabalho completo e explorar mais insights, [acesse aqui](https://docs.google.com/spreadsheets/d/1S-7tAX4mwNYQxynilAlijx8YZk04gkug/edit?usp=sharing&ouid=103139050864633488874&rtpof=true&sd=true).




