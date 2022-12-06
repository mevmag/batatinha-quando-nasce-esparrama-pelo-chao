# batatinha-quando-nasce-esparrama-pelo-chao

Trabalho final da disciplina de Introdução à Computação em Física.
O nome do código em Python que corresponde a esse projeto é "batatinha.py".


**O QUE ESSE PROGRAMA FAZ?**

*   Esse programa recebe:

      <> Valores de range de energia (apenas o número, em eV) do usuário, sendo 1 valor para a energia inicial e 1 valor para a energia final
      
      <> Um valor percentual que deve ser acrescido ou subtraído dos valores de seção de choque para a faixa de energia selecionada
      
      <> Um arquivo do tipo ".ace" formatado contendo dados de energias e seções de choque microscópicas para certo isótopo.

*   Ele retorna um arquivo com a mesma formatação original, e com os mesmos dados originais, exceto para as seções de choque microscópicas de fissão correspondentes à faixa de energia informada pelo usuário. Para essas seções de choque microscópicas, os valores retornados serão a % inserida maiores ou menores que os originais.


**PARA QUÊ ESSE RESULTADO SERVE?**

*    Todas as seções de choque microscópicas são obtidas por meios experimentais ou interpolações realizadas através de dados prévios. Não há, ainda, uma forma teórica de calculá-las, especialmente para todas as faixas de energias e para todos os isótopos. Por conta disso, esses dados contêm inerentemente um erro de medição. A questão importante a se fazer é: o quanto esses erros interferem em um sistema que utiliza os valores das seções de choque micrsoscópicas como base para os cálculos que permitem o seu funcionamento?

*    Com o arquivo novo contendo seções de choques microscópicas diferentes das originais, é possível utilizar outros programas, como o software Serpent, para realizar simulações de sistemas nucleares com esses novos dados. Isso permite avaliar o quão sensível é um certo sistema para pequenas flutuações das seções de choque microscópicas, e o quanto o resultado final (observado em função da criticalidade, por exemplo) é alterado para o caso de utilizarmos bibliotecas de dados diferentes, que é importante também pelo fato de que diferentes bibliotecas podem possuir discrepâncias entre si.


