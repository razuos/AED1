# SisCoPy

Sistema de correção de projetos em Python

## Requisitos

* [x] Login: Apenas usuários que conheçam a senha previamente determinada podem acessar o sistema.
* [x] Selecionar requisitos e pesos: No primeiro acesso, deve ser selecionados os requisitos e pesos para a correção. Em um segundo acesso, o sistema deve carregá-los automaticamente. Se o usuário inserir o comando `pesos`, o sistema mostrará os já salvos e perguntará se o usuário quer modificá-los.
* [x] Selecionar esquema de nomenclatura: Selecionar um esquema de nomenclatura dos arquivos python para identificação do estudante, da atividade ou da turma em questão.
* [x] Gerar arquivo de feedback:  Gerar uma cópia do arquivo de cada atividade dando feedback sobre quais características do código levaram o estudante a ter desconto na nota.
* [x] Exportar notas: Exportar as notas por turma, atividade ou estudante em formato CSV, permitindo ao usuário importar a tabela de notas numa planilha eletrônica.
* [x] Interface: A interface será em modo texto (terminal). Não será utilizada a biblioteca graphics.
* [x] Arquivos: Todos os dados serão armazenados em um ou mais arquivos.
* [x] Modularidade: O sistema será modulado usando funções, classes e arquivos separados.

## Limitações

Necessita de uma nomenclatura especificada nos projetos.

## Comandos

`ajuda`: mostra uma lista dos comandos disponíveis e uma pequena descrição.

`pesos`: seleciona os requisitos e pesos para a correção.

`nomenclatura`: Seleciona o esquema de nomenclatura esperado.

`corrigir`: pergunta onde os arquivos estão e realiza a sua correção utilizando os requisitos e pesos, exportando as notas para uma tabela CSV.

### Requisitos e pesos:

Toda função requer um comentário
