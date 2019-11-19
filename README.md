<!-- PROJECT LOGO -->
<p align="center">
  <a href="https://github.com/Mappets">
    <img src="https://avatars3.githubusercontent.com/u/57954053?s=200&v=4" width="200px" alt="Mappets brand">
  </a>

  <h3 align="center">Mappets Back-End</h3>
</p>

----

### About this repository

This repository contains the Back-End of the application. 

### App description

Plataforma colaborativa, onde qualquer pessoa pode se cadastrar. Haverá um Mapa listando o posicionamento de: 

- Animais para adoção
- Lares temporários
- Clínicas voluntárias 

Em cada um desses itens, será possível obter mais informações a respeito deste. Por ser colaborativa, qualquer pessoa pode fotografar um animal de rua, subir para a plataforma e classificar seu estado.

### Settings 

Create a virtualenv to start the settings. Install if you don't have using the following commands: `sudo apt install python-virtualenv` and `sudo apt-get install python3-venv`.

Create the local virtualenv: `python3 -m venv env`

Activate the virtualenv: `source env/bin/activate`

### Installation

Mappets requires [Python3](https://www.python.org/) v3+ to run.

Install the dependencies and devDependencies and start the server.

```shell
cd mappets
```

Use the `pip install` to install from `requirements.txt` file.

```python
pip install -r requirements.txt
```

Use the `manage.py` file to run the server.

```python
python manage.py runserver
```
