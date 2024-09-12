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

## Estatisca

- Um cientista de dados ganha mais, na média, do que um análista de dados?

<p align="center">
  <img alt="g1" width="50%" src="https://github.com/user-attachments/assets/868e7f34-be47-4988-ad2d-6133adceb681">
</p>

- De acordo com a tabela, os cientistas de dados ganham mais. Porém precisamos olhar isso de modo estatistico para poder afirmar essa inforamção.
- Como eu quero descobrir se o cientista de dados ganha mais que o análista de dados na média, o teste estatistico ideial é o teste t, que possui alguns pressupostos: Distribuição normal dos dados e homogenização da variancia
- Primeiramente, verifiquei se dos dados tinham distruição normal, dessa forma foi feito o teste Shapiro-Wilk, que mostra isso estatisticamente, e teve esse resultado:

<p align="center">
  <img alt="r2" width="50%" src="https://github.com/user-attachments/assets/94d0cc61-dabe-466a-89a2-b94fc76135b4">
</p>
- Com base nesse tabela é possivel afirmar que os dados não possuem distribuição normal. Isso ocorre devido o p-valor menor do que 0.05. Logo nós rejeitamos a hipotese nula (que os dados são normais). Um dos pressupostos para o test t, que é a normalidade nos dados não foi atingido, porém nesse caso me utilizei do teorema do Limite do Central, que pode ser aplicado, ja que as variaveis tem muitos valores e por isso considerei que os dados tinham uma distruição normal. Quando utilizamos isso, é imporntante analisar os graficos de frequencia  de cada uma das variaveis. 

<p align="center">
  <img alt="g1" width="50%" src="">
</p>


- É importante salientar que eu utilizei o teste de Shapiro-Wilk já que estou trabalhando com esse dataset que possui poucos dados. Caso tivessemos mais dados o teste correto seria o de Kolmogorov-Smirnov. 



-  Segundo, eu conferi se a variancia dos dois grupos ( Data Analyst e Data Especialist) é igual. E isso foi feito pelo teste de Levene que deu esse resultado:

<p align="center">
  <img alt="r1" width="50%" src="https://github.com/user-attachments/assets/878e339d-1e4d-496a-a64c-6522d5472007">
</p>
- Esse teste nos mostrou que os dois grupos possuem variancia estatisticamente diferentes. Porquê o p-valor é menor do que 0.05, logo rejeitamos a hipotese nula (que as havia homegeneidade nas variancias). 
-  Importante salientar que as Amostras independentes, estamos falando de dois grupos diferentes os Data Sciestist e Data Analyst
- 



## Considerações finais

## Descrição das Colunas 
- work_year:	The year the salary was paid.
- experience_level:	The experience level in the job during the year with the following possible values: EN Entry-level / Junior MI Mid-level / Intermediate SE Senior-level / Expert EX Executive-level / Director
- employment_type:	The type of employement for the role: PT Part-time FT Full-time CT Contract FL Freelance
- job_title:	The role worked in during the year.
- salary:	The total gross salary amount paid.
- salary_currency:	The currency of the salary paid as an ISO 4217 currency code.
- salary_in_usd:	The salary in USD (FX rate divided by avg. USD rate for the respective year via fxdata.foorilla.com).
- employee_residence:	Employee's primary country of residence in during the work year as an ISO 3166 country code.
- remote_ratio:	The overall amount of work done remotely, possible values are as follows: 0 No remote work (less than 20%) 50 Partially remote 100 Fully remote (more than 80%)
- company_location:	The country of the employer's main office or contracting branch as an ISO 3166 country code.
- company_size:	The average number of people that worked for the company during the year: S less than 50 employees (small) M 50 to 250 employees (medium) L more than 250 employees (large)
