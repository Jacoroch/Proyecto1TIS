import requests

def obtener_clima(ciudad):
    api_key = "e74ede156a884459ffe35aafb71f34a6"  # Reemplaza con tu clave de OpenWeatherMap
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if respuesta.status_code == 200:
        # Procesar datos del clima
        clima = datos['weather'][0]['description']
        temperatura = datos['main']['temp']
        return f"{clima.capitalize()}, {temperatura}°C"
    else:
        return "No se pudo obtener el clima."
