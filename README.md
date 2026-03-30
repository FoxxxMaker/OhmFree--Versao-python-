# OhmFree ⚡

O **OhmFree** é um projeto em **Python** desenvolvido para calcular o valor de resistores a partir do **código de cores**.

A aplicação possui uma **interface gráfica simples com Tkinter**, permitindo que o usuário selecione as faixas do resistor e visualize o valor calculado de forma prática, rápida e intuitiva.

---

## 📌 Objetivo

Este projeto foi desenvolvido com os seguintes objetivos:

* praticar lógica de programação com Python;
* reforçar o entendimento sobre resistores e código de cores;
* aplicar conceitos de interface gráfica com Tkinter;
* criar um projeto simples, útil e apresentável para portfólio.

---

## 🚀 Funcionalidades

* Seleção da **primeira faixa** do resistor;
* Seleção da **segunda faixa** do resistor;
* Seleção da **terceira faixa** (multiplicador);
* Cálculo automático do valor da resistência;
* Exibição do resultado em uma janela pop-up.

O cálculo é realizado com base em um dicionário que associa cada cor ao seu respectivo valor numérico, junto de uma função responsável por montar o valor final do resistor a partir das três faixas selecionadas.

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **Tkinter**
* **ttk**
* **tkinter.messagebox**

---

## 📂 Estrutura do projeto

```bash
OhmFree/
└── Main/
    ├── Back.py
    └── front.py
```

### `Back.py`

Responsável pela lógica do sistema:

* define o dicionário de cores;
* realiza o cálculo da resistência;
* retorna o valor calculado.

### `front.py`

Responsável pela interface gráfica:

* cria a janela principal;
* exibe instruções para o usuário;
* monta os campos de seleção das cores;
* chama o backend para calcular o resistor e exibir o resultado.

---

## ▶️ Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. Baixe os arquivos do projeto.
3. Coloque `Back.py` e `front.py` na mesma pasta.
4. Execute o arquivo principal com o comando:

```bash
python front.py
```

---

## 🎨 Cores suportadas

As cores aceitas pelo sistema são:

* preto
* marrom
* vermelho
* laranja
* amarelo
* verde
* azul
* violeta
* cinza
* branco

Essas cores estão definidas diretamente no backend por meio de um dicionário de equivalência numérica.

---

## 💡 Exemplo de uso

Se o usuário selecionar as cores:

* **marrom**
* **preto**
* **vermelho**

O programa calculará automaticamente o valor correspondente da resistência com base na regra das três faixas.

---

## 📚 Aprendizados com este projeto

Durante o desenvolvimento deste projeto, foram praticados conceitos como:

* dicionários em Python;
* funções;
* interface gráfica com Tkinter;
* integração entre frontend e backend;
* entrada de dados com `Combobox`;
* exibição de mensagens com `messagebox`.

---

## 🔮 Melhorias futuras

Algumas melhorias que podem ser adicionadas futuramente:

* suporte à **quarta faixa** (tolerância);
* validação para impedir cálculo sem selecionar todas as cores;
* melhoria visual da interface;
* exibição formatada dos valores em **Ω, kΩ e MΩ**;
* suporte a mais tipos de resistores.

---

## 👨‍💻 Autor

Desenvolvido por **Levi Soares**
GitHub: **FoxxxMaker**

---

## 📄 Licença

Este projeto foi desenvolvido para fins de **estudo**, **prática** e **portfólio**.
