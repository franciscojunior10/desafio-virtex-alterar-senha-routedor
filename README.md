<h3 align="center">
Desafio – Login TP-LINK WR840N
</h3>

<p align="center">Realizar login e alterar de senha no roteador TP-LINK WR840N via Script</p>

<p align="center">
<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/franciscojunior10/desafio-virtex-alterar-senha-routedor">

<a href="https://www.linkedin.com/in/franciscojunior10/" target="_blank" rel="noopener noreferrer">
<img alt="Made by" src="https://img.shields.io/badge/made%20by-franciscojunior10-blue">
</a>

<img alt="Repository size" src="https://img.shields.io/github/repo-size/franciscojunior10/desafio-virtex-alterar-senha-routedor?color=blue">

<a href="https://github.com/franciscojunior10/desafio-virtex-alterar-senha-routedor/commits/master">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/franciscojunior10/desafio-virtex-alterar-senha-routedor?color=blue">
</a>

<a href="https://github.com/franciscojunior10/desafio-virtex-alterar-senha-routedor/stargazers">
<img alt="Stargazers" src="https://img.shields.io/github/stars/franciscojunior10/desafio-virtex-alterar-senha-routedor?color=blue">
</a>
</p>

<p align="center">
<a href="#sobre-o-desafio-open_file_folder">Sobre o desafio</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#tecnologias-rocket">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#executando-script-desktop_computer">Executando script</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#autor-man_technologist">Autor</a>
</p>


<p align="center">
<img alt="Gif" src="https://user-images.githubusercontent.com/33940202/89652656-2f670580-d89c-11ea-96e7-8b35d771e13a.gif" />
</p>

## Sobre o desafio :open_file_folder::

O desafio consiste em realizar login e alterar senha no roteador WR840N (ou modelos da TP-Link) via Script (em qualquer linguagem).

## Tecnologias :rocket::

Tecnologias que usei para realizar este desafio:

- [Python](https://www.python.org/)
- [Telnetlib](https://docs.python.org/3.1/library/telnetlib.html)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Executando script :desktop_computer::

**Configuração no Roteador**
```bash
Antes de começar o desafio tive que que realizar uma configuração no roteador, que foi liberar a porta 23 que o Telnet utliza.
```

**Clone o projeto e acesse a pasta**

```bash
$ https://github.com/franciscojunior10/desafio-virtex-alterar-senha-routedor.git && cd desafio-virtex-alterar-senha-routedor
```

**Criar o ambiente virtual**

##### Caso não possua o virtualenv instalado é acessar [aqui](https://virtualenv.pypa.io/en/latest/installation.html#) para instalar.

```bash
# Criar o ambiente virtual
$ virtualenv --python=python3 env

# Ativar o ambiente virtual
$ source env/bin/activate

# Desativar o ambiente virtual
$ deactivate
```

**Executando o script**
```bash
# Executar o script
$ python main.py
```

# Autor :man_technologist::

Feito com :heart: by **franciscojunior10** meu :point_right: [Linkedin](https://www.linkedin.com/in/franciscojunior10/)