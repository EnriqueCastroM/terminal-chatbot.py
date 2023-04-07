# terminal-chatbot.py
# Crear un Chat Bot con Python y Open AI

Este tutorial le mostrará cómo crear un chat bot con Python y Open AI. Un chat bot es un programa informático que simula una conversación con un humano.

## Prerequisitos

Para seguir este tutorial, necesitarás lo siguiente:

- Una cuenta de Open AI
- Python 3.6 o superior
- Un editor de texto o IDE

## Crear una cuenta de Open AI

La primera cosa que necesitas hacer es crear una cuenta de Open AI. Visite la página de registro de Open AI y siga las instrucciones para crear una cuenta.

##Crear entorno virtual e instalacion de dependencias

```
 python -n venv venv
```

```
 code .
```

##Activar el entorno virtual
```
 .\venv\Scripts\activate "en este caso puede cambiar segun la pc" .\venv\bin\activate
```
Una vez que haya creado una cuenta, debe instalar Open AI. Esto se hace usando el comando pip:

```
pip install openai
```

## Crear un archivo Python

Ahora que ya tienes Open AI instalado, es hora de crear un archivo Python para tu chat bot. Abre tu editor de texto o IDE y crea un archivo llamado `chat_gpt.py`.     

## Escribir el código

Ahora es el momento de escribir el código para tu chat bot. Abre tu archivo `chat_gpt.py` y agrega el siguiente código:

```
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

response = openai.Completion.create(
    engine="davinci",
    prompt="¿Cómo estás hoy?",
    max_tokens=100
)

print(response.choices[0].text)
```

Reemplace `YOUR_OPENAI_API_KEY` con la clave de API de su cuenta de Open AI.

## Ejecutar el código

Ahora que ya has escrito el código para tu chat bot, es hora de ejecutarlo. Para ejecutar el código, abre una terminal y ejecuta el siguiente comando:

```
python chatbot.py
```

Si todo ha ido bien, verás una respuesta del chat bot en la terminal.

## Conclusion

Comandos de salida:
'exit','salir','terminar','quit'
