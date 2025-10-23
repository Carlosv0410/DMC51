# poo_app1_estudiantes.py
import streamlit as st
import pandas as pd

st.title("🎓 Gestor de Estudiantes y Cursos")

# ==== Definición de Clases ====
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas)/len(self.notas) if self.notas else 0

# ==== Interfaz Streamlit ====
nombre = st.text_input("Nombre del estudiante")
edad = st.number_input("Edad", min_value=0, max_value=120)
matricula = st.text_input("Número de matrícula")

if "estudiantes" not in st.session_state:
    st.session_state.estudiantes = []

if st.button("Registrar estudiante"):
    est = Estudiante(nombre, edad, matricula)
    st.session_state.estudiantes.append(est)
    st.success(f"✅ Estudiante {nombre} registrado correctamente.")

st.subheader("📚 Agregar notas")
if st.session_state.estudiantes:
    seleccionado = st.selectbox("Selecciona estudiante", [e.nombre for e in st.session_state.estudiantes])
    nota = st.number_input("Nota", 0.0, 10.0)
    if st.button("Agregar nota"):
        for e in st.session_state.estudiantes:
            if e.nombre == seleccionado:
                e.agregar_nota(nota)
                st.success(f"Nota {nota} agregada a {e.nombre}")

    # Mostrar promedios
    data = [{"Nombre": e.nombre, "Edad": e.edad, "Promedio": round(e.promedio(), 2)} for e in st.session_state.estudiantes]
    st.dataframe(pd.DataFrame(data))