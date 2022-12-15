# batatinha-quando-nasce-esparrama-pelo-chao

Trabalho final da disciplina de Introdução à Computação em Física.
O nome do código em Python que corresponde a esse projeto é "batatinha.py".


**O QUE ESSE PROGRAMA FAZ?**

*   Esse programa recebe:

      <> Valores de range de energia (apenas o número, em MeV) do usuário, sendo 1 valor para a energia inicial e 1 valor para a energia final
      
      <> Um valor percentual que deve ser acrescido ou subtraído dos valores de seção de choque para a faixa de energia selecionada
      
      <> Um arquivo do tipo ".ace" formatado contendo dados de energias e seções de choque microscópicas para certo isótopo.

*   Ele retorna um arquivo com a mesma formatação original, e com os mesmos dados originais, exceto para as seções de choque microscópicas de fissão correspondentes à faixa de energia informada pelo usuário. Para essas seções de choque microscópicas, os valores retornados serão a % inserida maiores ou menores que os originais.


**PARA QUÊ ESSE RESULTADO SERVE?**

*    Todas as seções de choque microscópicas são obtidas por meios experimentais ou interpolações realizadas através de dados prévios. Não há, ainda, uma forma teórica de calculá-las, especialmente para todas as faixas de energias e para todos os isótopos. Por conta disso, esses dados contêm inerentemente um erro de medição. A questão importante a se fazer é: o quanto esses erros interferem em um sistema que utiliza os valores das seções de choque micrsoscópicas como base para os cálculos que permitem o seu funcionamento?

*    Com o arquivo novo contendo seções de choques microscópicas diferentes das originais, é possível utilizar outros programas, como o software Serpent, para realizar simulações de sistemas nucleares com esses novos dados. Isso permite avaliar o quão sensível é um certo sistema para pequenas flutuações das seções de choque microscópicas, e o quanto o resultado final (observado em função da criticalidade, por exemplo) é alterado para o caso de utilizarmos bibliotecas de dados diferentes, que é importante também pelo fato de que diferentes bibliotecas podem possuir discrepâncias entre si.


**O que está disponível no respositório?**

*    Um arquivo de nome "92-U-235g-900.ace" que contém vários dados de seções de choque e energias para o Urânio-235 à temperatura de 600K, que pode ser inserido no programa para realizar as alterações das seções de choque de fissão do mesmo.
*    Um arquivo chamado "Exemplo de Execução Batatinha", que contém a forma como o programa insere as mensagens para o usuário, e o tipo de resposta que deve ser inserida por ele no momento de execução do programa.
*    Um arquivo "batatinha.py", que é o programa em questão.
*    Um "pin", que é um arquivo que o Serpent roda. No nosso caso, fizemos para simular as diferenças geradas pela mudança da seção de choque microscópica, para um pin (tubo) formado por uma mistura de U-235 e U-238 no combustível, revestimento de Zircônio natural, e rodeado por água leve para resfriamento (H2O). As mudanças de seções de choque microscópicas foram feitas para o arquivo .ace do U-235, disponibilizado no repositório. O "pin_Thermal_1" foi o pin utilizado para rodar a simulação do aumento de 1% da seção de choque microscópica no código Serpent. Os resultados dessa simulação, junto com outras explicações sobre as seções de choque, estão disponíveis no PDF (conteúdo detalhado a seguir).
*    Um arquivo de apresentação de nome "nuclear icf.pdf", contendo informações sobre as seções de choque, o projeto desenvolvido, e um caso exemplo do U-235, a 600 K, simulado no Serpent com aumento de 1% para as seções de choque microscópicas na faixa térmica.
*    Um "resultado_1porcento_92-U-235g-900.ace", que contém uma saída de teste. Foi alterado o arquivo "92-U-235g-900.ace", em 1% para as seções de choque microscópicas de fissão, para as faixas de energia entre 0 eV e 0.025 eV.
*    Esse arquivo README.md, que contém algumas orientações.

