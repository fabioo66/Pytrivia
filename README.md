# Entrega tp Integrador
En esta primera entrega, el objetivo principal  es el uso de archivos csv en python, y un breve desarrollo de una pagina web utilizando la libreria 'streamlit'.

## Introducción a los archivos CSV
Los archivos CSV (Comma Separated Values) son una forma común de almacenar datos tabulares en formato de texto plano. Cada línea del archivo representa una fila de datos, y los valores en cada fila están separados por comas o cualquier otro delimitador definido.

## ¿Qué es Streamlit?
Streamlit es una biblioteca de Python que permite crear aplicaciones web interactivas con tan solo unas pocas líneas de código. Con Streamlit, podes construir interfaces de usuario intuitivas para visualizar datos, realizar análisis, etc.

### Miembros del grupo:

- Fabio Ignacio Torrejón
- Fermin Manuel Prida
- Valentin Capelli

## Instalación

## **requiere Python 3.11 o superior**

#### Windows

```bash
git clone https://github.com/fabioo66/Pytrivia
cd Pytrivia

# Crear el entorno virtual
python3.11 -m venv venv

# Activar entorno virtual
source venv/Scripts/activate

# Instalar librerias necesarias
pip install -r requirements.txt
```

#### Linux

```bash
git clone https://github.com/fabioo66/Pytrivia
cd Pytrivia
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecucion del programa

```bash
jupyter notebook
```

Una vez abierto el sitio web, posicionarse en el archivo 'tp_integrador1_p2.ipynb'. Aqui podras hacer consultas a los dastasets modificados previamente, que se encuentran en la carpeta 'custom_datasets'.

## Ejecucion de la pagina web

```bash
# Nos posicionamos en el directorio donde se encuentra la pagina web
cd app

# Abrimos la pagina web
streamlit run Inicio.py
```

## Observacion

Los comandos streamlit y jupyter notebook pueden fallar ejecutandose en linux. Para solucionar esto, ejecuta en la terminal los siguientes comandos.

```bash
# Comando para juypter notebook
sudo apt-get install libsqlite3-dev

# Comando para streamlit
sudo apt install libffi-dev
```

En el caso que siga fallando, desintala y vuelve a instalar python. Tenga en cuenta que estos comandos solo sirven para **distribuciones basadas en ubuntu**, si utilizas otra, debes buscar los comandos que sean compatibles a los mostrados anteriormente.
