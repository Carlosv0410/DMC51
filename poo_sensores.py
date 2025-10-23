import streamlit as st  # Importa la librería Streamlit y la referencia como 'st' para construir la UI web.

st.set_page_config(page_title="Alarma", page_icon="🚨")  # Configura la página: título del navegador e ícono. Debe ir antes de dibujar la UI.
st.title("🚨 Sensor con rango")  # Muestra un encabezado grande en la app.

class Sensor:  # Declara una clase que modela un sensor con límites mínimo y máximo (POO).
    def __init__(self, nombre, unidad):     # Constructor: recibe el nombre del sensor y su unidad de medida.
        self.nombre = nombre                # Guarda el nombre (ej.: "Temperatura" o "Vibración").
        self.unidad = unidad                # Guarda la unidad (ej.: "°C" o "mm/s").
        self.min_v = 0                      # Inicializa el umbral mínimo en 0 (valor por defecto).
        self.max_v = 0                      # Inicializa el umbral máximo en 0 (valor por defecto).
    def set_rango(self, minimo, maximo):    # Método para definir/actualizar los límites permitidos del sensor.
        self.min_v = minimo                 # Asigna el nuevo límite mínimo.
        self.max_v = maximo                 # Asigna el nuevo límite máximo.
    def estado(self, valor):                # Método que evalúa una lectura y devuelve un estado textual.
        # Expresión condicional: si valor < min → "bajo"; si valor > max → "alto"; en otro caso → "ok".
        return "bajo" if valor < self.min_v else ("alto" if valor > self.max_v else "ok")

# Crea un selector tipo radio para elegir el tipo de sensor; el resultado es una cadena del ítem elegido.
tipo = st.radio("Tipo", ["Temperatura (°C)", "Vibración (mm/s)"], horizontal=True)

unidad, low, high, dmin, dmax, dval = (("°C", 0, 120, 20, 60, 55) if "Temp" in tipo else ("mm/s", 0, 50, 2, 10, 12))  # Selecciona presets según la opción elegida:
s = Sensor(tipo.split()[0], unidad)  # Crea el objeto Sensor; split()[0] toma solo la palabra "Temperatura" o "Vibración".
mn = st.number_input("Mínimo", low, high, dmin)  # Input numérico para el umbral mínimo; acotado entre 'low' y 'high'.
mx = st.number_input("Máximo", mn,  high, dmax)  # Input numérico para el umbral máximo; su mínimo permitido es 'mn' (garantiza max ≥ min).
val = st.slider("Lectura", low, high, dval)      # Slider para la lectura actual del sensor; también acotado entre 'low' y 'high'.
s.set_rango(mn, mx)  # Actualiza en el objeto los límites elegidos por el usuario.

e = s.estado(val)    # Calcula el estado de la lectura: "bajo", "ok" o "alto" según el rango definido.
if   e == "ok":
    st.success(f"✅ {tipo} dentro del intervalo operativo: {val}{unidad}") # Mensaje verde si el valor está dentro del intervalo; se muestra el valor y la unidad.
elif e == "bajo":
    st.warning(f" ▼ {tipo} por debajo del mínimo operativo: {val}{unidad}") # Mensaje amarillo si el valor está por debajo del mínimo.
else:
    st.error  (f"🔺 {tipo} por encima del máximo operativo: {val}{unidad}") # Mensaje rojo si el valor está por encima del máximo.