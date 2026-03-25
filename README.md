## OhmFree ⚡

O OhmFree é um projeto em Python criado para calcular o valor de resistores a partir do código de cores.
A aplicação possui uma interface gráfica simples feita com Tkinter, permitindo que o usuário selecione as três faixas do resistor e visualize o valor calculado de forma prática.

##📌 Objetivo

Este projeto foi desenvolvido com o objetivo de:

praticar lógica de programação em Python;
reforçar o entendimento sobre resistores e código de cores;
aplicar conceitos de interface gráfica com Tkinter;
criar um projeto simples e útil para portfólio.


## 🚀 Funcionalidades
Seleção da primeira faixa do resistor;
Seleção da segunda faixa do resistor;
Seleção da terceira faixa (multiplicador);
Cálculo automático do valor da resistência;
Exibição do resultado em uma janela pop-up.

O cálculo é feito com base em um dicionário que relaciona cada cor a um número e em uma função que monta o valor do resistor usando as três faixas.

##🛠️ Tecnologias utilizadas
Python 3
Tkinter
ttk
tkinter.messagebox

## 📂 Estrutura do projeto
OhmFree/
Main/
├── Back.py
└── front.py


Responsável pela lógica do sistema:

define o dicionário de cores;
realiza o cálculo da resistência;
retorna o valor calculado.
front.py

Responsável pela interface gráfica:

cria a janela principal;
exibe instruções para o usuário;
monta os campos de seleção das cores;
chama o backend para calcular o resistor e mostrar o resultado.

##▶️ Como executar
Certifique-se de ter o Python 3 instalado.
Baixe os arquivos do projeto.
Coloque Back.py e front.py na mesma pasta.
Execute o arquivo principal:
python front.py

##🎨 Cores suportadas

As cores aceitas pelo sistema são:

preto
marrom
vermelho
laranja
amarelo
verde
azul
violeta
cinza
branco

Essas cores estão definidas diretamente no backend como um dicionário de equivalência numérica.

##💡 Exemplo de uso

Se o usuário selecionar:

marrom
preto
vermelho

O programa irá calcular o valor correspondente da resistência com base na regra das três faixas.

## 📚 Aprendizados com este projeto

Durante o desenvolvimento deste projeto, foram praticados conceitos como:

dicionários em Python;
funções;
interface gráfica com Tkinter;
integração entre frontend e backend;
entrada de dados com Combobox;
exibição de mensagens com messagebox.

## 🔮 Melhorias futuras

Algumas melhorias que podem ser adicionadas no futuro:

suporte à quarta faixa (tolerância);
validação para impedir cálculo sem selecionar todas as cores;
melhoria visual da interface;
exibição formatada de valores em ohms, kΩ e MΩ;
suporte a mais tipos de resistores.
## 👨‍💻 Autor

Desenvolvido por Levi Soares
GitHub: FoxxxMaker

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo, prática e portfólio.
