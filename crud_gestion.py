# Importando las librerías necesarias
import streamlit as st  # Streamlit permite crear interfaces interactivas para tus aplicaciones web.
import pandas as pd  # Pandas es una librería poderosa para manipulación de datos.

# Inicializando las bases de datos en `st.session_state` si no existen.
# `st.session_state` se usa para almacenar variables en memoria durante una sesión en Streamlit.
if 'productos' not in st.session_state:
    st.session_state['productos'] = {}  # Diccionario vacío para almacenar los productos.
if 'proyecto' not in st.session_state:
    st.session_state['proyecto'] = {}  # Diccionario vacío para almacenar los proyectos.
if 'estudiantes' not in st.session_state:
    st.session_state['estudiantes'] = {}  # Diccionario vacío para almacenar los estudiantes.

# --- CLASES Y FUNCIONES CRUD --- # Este bloque contiene las funciones que realizan las operaciones CRUD

# Función para agregar un producto.
def agregar_producto(id_creacion, nombre_creacion, precio, cantidad):
    """
    Esta función recibe los datos del producto y lo agrega a la base de datos en memoria.
    """
    st.session_state['productos'][id_creacion] = {'id':id_creacion, 'Nombre': nombre_creacion, 'Precio': precio, 'Cantidad': cantidad}
    st.success(f"Producto '{nombre_creacion}' agregado.")  # Muestra un mensaje de éxito.
    mostrar_producto()  # Muestra el DataFrame con los productos actualizados.

# Función para ver un producto.
def ver_producto(id_busqueda):
    """
    Esta función permite ver un producto usando su ID.
    """
    if id_busqueda in st.session_state['productos']:
        st.write(st.session_state['productos'][id_busqueda])  # Muestra los detalles del producto.
    else:
        st.error(f"Producto con ID '{id_busqueda}' no encontrado.")  # Mensaje de error si no se encuentra el producto.
    mostrar_producto()  # Muestra el DataFrame con los productos.

# Función para eliminar un producto.
def eliminar_producto(id_eliminacion):
    """
    Esta función elimina un producto de la base de datos utilizando su ID.
    """
    if id_eliminacion in st.session_state['productos']:
        del st.session_state['productos'][id_eliminacion]  # Elimina el producto del diccionario.
        st.success(f"Producto con ID '{id_eliminacion}' eliminado.")  # Mensaje de éxito.
    else:
        st.error(f"Producto con ID '{id_eliminacion}' no encontrado.")  # Mensaje de error si no se encuentra el producto.
    mostrar_producto()  # Muestra el DataFrame con los productos actualizados.

# Función para actualizar un producto.
def actualizar_producto(id_actualizacion, nombre_actualizado, precio_actualizado, cantidad_actualizada):
    """
    Esta función actualiza los detalles de un producto utilizando su ID.
    """
    if id_actualizacion in st.session_state['productos']:
        st.session_state['productos'][id_actualizacion] = {
            'Nombre': nombre_actualizado,
            'Precio': precio_actualizado,
            'Cantidad': cantidad_actualizada
        }
        st.success(f"Producto con ID '{id_actualizacion}' actualizado.")  # Mensaje de éxito.
        mostrar_producto()  # Muestra el DataFrame con los productos actualizados.
    else:
        st.error(f"Producto con ID '{id_actualizacion}' no encontrado.")  # Mensaje de error si no se encuentra el producto.

# --- Funciones para los Proyectos ---

# Función para agregar un proyecto.
def agregar_proyecto(id_creacion, nombre_creacion, responsable, presupuesto):
    """
    Esta función agrega un proyecto al sistema con los parámetros dados.
    """
    st.session_state['proyecto'][id_creacion] = {'id':id_creacion, 'Nombre': nombre_creacion, 'Responsable': responsable, 'Presupuesto': presupuesto}
    st.success(f"Proyecto '{nombre_creacion}' agregado.")  # Mensaje de éxito.
    mostrar_proyecto()  # Muestra el DataFrame con los proyectos actualizados

# Función para ver una proyecto.
def ver_proyecto(id_busqueda):
    """
    Esta función permite ver un proyecto usando su ID.
    """
    if id_busqueda in st.session_state['proyecto']:
        st.write(st.session_state['proyecto'][id_busqueda])  # Muestra los detalles del proyecto.
    else:
        st.error(f"Proyecto con ID '{id_busqueda}' no encontrada.")  # Mensaje de error si no se encuentra los proyectos.
    mostrar_proyecto()  # Muestra el DataFrame con los proyecto.

# Función para eliminar un proyecto.
def eliminar_proyecto(id_eliminacion):
    """
    Esta función elimina un proyecto usando su ID.
    """
    if id_eliminacion in st.session_state['proyecto']:
        del st.session_state['proyecto'][id_eliminacion]  # Elimina el proyecto del diccionario.
        st.success(f"Proyecto con ID '{id_eliminacion}' eliminada.")  # Mensaje de éxito.
    else:
        st.error(f"Proyecto con ID '{id_eliminacion}' no encontrada.")  # Mensaje de error si no se encuentra el proyecto.
    mostrar_proyecto()  # Muestra el DataFrame con los proyectos actualizadas.

# Función para actualizar una proyecto.
def actualizar_proyecto(id_actualizacion, nombre_actualizado, responsable_actualizado, presepuesto_actualizado):
    """
    Esta función actualiza un proyecto con los nuevos valores dados.
    """
    if id_actualizacion in st.session_state['proyecto']:
        st.session_state['proyecto'][id_actualizacion] = {
            'Nombre': nombre_actualizado,
            'Responsable': responsable_actualizado,
            'Presupuesto': presepuesto_actualizado
        }
        st.success(f"Proyecto con ID '{id_actualizacion}' actualizado.")  # Mensaje de éxito.
        mostrar_proyecto()  # Muestra el DataFrame con los proyectos actualizados.
    else:
        st.error(f"Proyecto con ID '{id_actualizacion}' no encontrado.")  # Mensaje de error si no se encuentra el proyecto.

# --- Funciones para los Estudiantes ---

# Función para agregar un estudiante.
def agregar_estudiante(id_creacion, nombre_creacion, matricula):
    """
    Esta función agrega un estudiante al sistema con los parámetros dados.
    """
    st.session_state['estudiantes'][id_creacion] = {'id':id_creacion, 'Nombre': nombre_creacion, 'Matrícula': matricula}
    st.success(f"Estudiante '{nombre_creacion}' agregado.")  # Mensaje de éxito.
    mostrar_estudiante()  # Muestra el DataFrame con los estudiantes actualizados.

# Función para ver un estudiante.
def ver_estudiante(id_busqueda):
    """
    Esta función permite ver un estudiante usando su ID.
    """
    if id_busqueda in st.session_state['estudiantes']:
        st.write(st.session_state['estudiantes'][id_busqueda])  # Muestra los detalles del estudiante.
    else:
        st.error(f"Estudiante con ID '{id_busqueda}' no encontrado.")  # Mensaje de error si no se encuentra el estudiante.
    mostrar_estudiante()  # Muestra el DataFrame con los estudiantes.

# Función para eliminar un estudiante.
def eliminar_estudiante(id_eliminacion):
    """
    Esta función elimina un estudiante usando su ID.
    """
    if id_eliminacion in st.session_state['estudiantes']:
        del st.session_state['estudiantes'][id_eliminacion]  # Elimina al estudiante del diccionario.
        st.success(f"Estudiante con ID '{id_eliminacion}' eliminado.")  # Mensaje de éxito.
    else:
        st.error(f"Estudiante con ID '{id_eliminacion}' no encontrado.")  # Mensaje de error si no se encuentra el estudiante.
    mostrar_estudiante()  # Muestra el DataFrame con los estudiantes actualizados.

# Función para actualizar un estudiante.
def actualizar_estudiante(id_actualizacion, nombre_actualizado, matricula_actualizada):
    """
    Esta función actualiza los datos de un estudiante con los nuevos valores dados.
    """
    if id_actualizacion in st.session_state['estudiantes']:
        st.session_state['estudiantes'][id_actualizacion] = {
            'Nombre': nombre_actualizado,
            'Matrícula': matricula_actualizada
        }
        st.success(f"Estudiante con ID '{id_actualizacion}' actualizado.")  # Mensaje de éxito.
        mostrar_estudiante()  # Muestra el DataFrame con los estudiantes actualizados.
    else:
        st.error(f"Estudiante con ID '{id_actualizacion}' no encontrado.")  # Mensaje de error si no se encuentra el estudiante.

# Funciones para mostrar los DataFrames
def mostrar_producto():
    df = pd.DataFrame.from_dict(st.session_state['productos'], orient='index')
    st.subheader("Listado de Productos")
    st.write(df)

def mostrar_proyecto():
    df = pd.DataFrame.from_dict(st.session_state['proyecto'], orient='index')
    st.subheader("Listado de Proyectos")
    st.write(df)

def mostrar_estudiante():
    df = pd.DataFrame.from_dict(st.session_state['estudiantes'], orient='index')
    st.subheader("Listado de Estudiantes")
    st.write(df)

# --- INTERFAZ STREAMLIT ---

# Página Principal
st.title("📊 Sistema CRUD Interactivo 🚀")

# Título con gradiente en HTML
st.markdown("""
    <h1 style="background: linear-gradient(to right, #ff7e5f, #feb47b); 
    color: white; text-align: center; padding: 30px;">
    Aplicación CRUD para Proyectos, Productos y Estudiantes
    </h1>
    """, unsafe_allow_html=True)

# Descripción
st.write("""
    Este aplicativo permite gestionar **Proyectos**, **Productos** y **Estudiantes** con operaciones CRUD (Crear, Leer, Eliminar, Actualizar).
    Puedes realizar varias operaciones de manera sencilla y rápida con una interfaz interactiva.
    🚀 ¡Comienza a gestionar tus datos de manera eficiente!
""")

# Menú de selección de página
pagina = st.sidebar.selectbox("Selecciona una página:", ["🏠 Home", "📋 Ejemplos CRUD"])

if pagina == "🏠 Home":
    st.write("""
        **Bienvenido a la página de ejemplos CRUD!** 🛠️
        
        Selecciona **"Ejemplos CRUD"** para gestionar **Estudiantes**, **Proyectos** o **Productos**.
    """)

elif pagina == "📋 Ejemplos CRUD":
    tabs = st.tabs(["👤 Ejemplo de Estudiantes", "🛠️ Ejemplo de Proyectos", "📦 Ejemplo de Productos"])

    with tabs[0]:
        st.header("👤 Gestión de Estudiantes")
        
        # Expander para agregar estudiante
        with st.expander("Agregar Estudiante"):
            id_creacion = st.text_input("ID del Estudiante")
            nombre_creacion = st.text_input("Nombre del Estudiante")
            matricula = st.text_input("Matrícula del Estudiante")
            if st.button("Agregar Estudiante"):
                agregar_estudiante(id_creacion, nombre_creacion, matricula)

        # Expander para ver estudiante
        with st.expander("Ver Estudiante"):
            id_busqueda = st.text_input("ID del Estudiante para ver detalles")
            if st.button("Ver Estudiante"):
                ver_estudiante(id_busqueda)

        # Expander para actualizar estudiante
        with st.expander("Actualizar Estudiante"):
            id_actualizacion = st.text_input("ID del Estudiante para actualizar")
            nombre_actualizado = st.text_input("Nuevo Nombre del Estudiante")
            matricula_actualizada = st.text_input("Nueva Matrícula del Estudiante")
            if st.button("Actualizar Estudiante"):
                actualizar_estudiante(id_actualizacion, nombre_actualizado, matricula_actualizada)

        # Expander para eliminar estudiante
        with st.expander("Eliminar Estudiante"):
            id_eliminacion = st.text_input("ID del Estudiante para eliminar")
            if st.button("Eliminar Estudiante"):
                eliminar_estudiante(id_eliminacion)

        # Boton para generar excel de estudiantes
        if st.button('Generar Excel Estudiantes'):
            df_estudiantes = pd.DataFrame.from_dict(st.session_state['estudiantes'], orient='index')
            df_estudiantes.to_excel('Excel_Estudiantes.xlsx', index= False)

    with tabs[1]:
        st.header("🛠️ Gestión de Proyectos")
        
        # Expander para agregar proyecto
        with st.expander("Agregar Proyecto"):
            id_creacion = st.text_input("ID del Proyecto")
            nombre_creacion = st.text_input("Nombre del Proyecto")
            responsable = st.text_input("Nombre del Responsable")
            presupuesto = st.number_input("Presupuesto ($)")
            if st.button("Agregar Proyecto"):
                agregar_proyecto(id_creacion, nombre_creacion, responsable, presupuesto)

        # Expander para ver el proyecto
        with st.expander("Ver Proyecto"):
            id_busqueda = st.text_input("ID del Proyecto para ver detalles")
            if st.button("Ver Proyecto"):
                ver_proyecto(id_busqueda)

        # Expander para actualizar proyecto
        with st.expander("Actualizar Proyecto"):
            id_actualizacion = st.text_input("ID del Proyecto para actualizar")
            nombre_actualizado = st.text_input("Nuevo Nombre del Proyecto")
            responsable_actualizado = st.text_input("Nuevo Responsable del Proyecto")
            presupuesto_actualizado = st.number_input("Nuevo Presupuesto del Proyecto", value=0)
            if st.button("Actualizar Proyecto"):
                actualizar_proyecto(id_actualizacion, nombre_actualizado, responsable_actualizado, presupuesto_actualizado)

        # Expander para eliminar Proyecto
        with st.expander("Eliminar Proyecto"):
            id_eliminacion = st.text_input("ID del Proyecto para eliminar")
            if st.button("Eliminar Proyecto"):
                eliminar_proyecto(id_eliminacion)

        # Boton para generar excel de proyectos
        if st.button('Generar Excel de Proyectos'):
            df_proyecto = pd.DataFrame.from_dict(st.session_state['proyecto'], orient='index')
            df_proyecto.to_excel('Excel_Proyectos.xlsx', index= False)


    with tabs[2]:
        st.header("📦 Gestión de Productos")
        
        # Expander para agregar producto
        with st.expander("Agregar Producto"):
            id_creacion = st.text_input("ID del Producto")
            nombre_creacion = st.text_input("Nombre del Producto")
            precio = st.number_input("Precio del Producto")
            cantidad = st.number_input("Cantidad en Stock")
            if st.button("Agregar Producto"):
                agregar_producto(id_creacion, nombre_creacion, precio, cantidad)

        # Expander para ver producto
        with st.expander("Ver Producto"):
            id_busqueda = st.text_input("ID del Producto para ver detalles")
            if st.button("Ver Producto"):
                ver_producto(id_busqueda)

        # Expander para actualizar producto
        with st.expander("Actualizar Producto"):
            id_actualizacion = st.text_input("ID del Producto para actualizar")
            nombre_actualizado = st.text_input("Nuevo Nombre del Producto")
            precio_actualizado = st.number_input("Nuevo Precio del Producto", value=0)
            cantidad_actualizada = st.number_input("Nueva Cantidad en Stock", value=0)
            if st.button("Actualizar Producto"):
                actualizar_producto(id_actualizacion, nombre_actualizado, precio_actualizado, cantidad_actualizada)

        # Expander para eliminar producto
        with st.expander("Eliminar Producto"):
            id_eliminacion = st.text_input("ID del Producto para eliminar")
            if st.button("Eliminar Producto"):
                eliminar_producto(id_eliminacion)

        # Boton para generar excel de productos
        if st.button('Generar Excel Productos'):
            df_productos = pd.DataFrame.from_dict(st.session_state['productos'], orient='index')
            df_productos .to_excel('Excel_Productos.xlsx', index= False)