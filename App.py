import streamlit as st
import pandas as pd
import pdb


# ----- CLASES --------
# -----------------------------
# Definición de la clase
# -----------------------------
class Actividad:
    def __init__(self, nombre, tipo, ppto, gasto):
        self.nombre = nombre
        self.tipo = tipo
        self.ppto = ppto
        self.gasto = gasto

    # Método para calcular retorno
    def calcular_retorno(self, tasa, meses):
        return self.ppto * tasa * meses

    # Método para evaluar estado
    def esta_en_presupuesto(self):
        return self.gasto <= self.ppto
        
        
   # Nuevo método para mostrar contenido  
    def mostrar_info(self):
        info = f"""
        Nombre: {self.nombre}
        Tipo: {self.tipo}
        Presupuesto: {self.ppto}
        Gasto real: {self.gasto}
        Dentro del presupuesto: {self.esta_en_presupuesto()}
        """
        return info
        
# ----- FUNCIONES ----------------------------------------------------------------
# deben de ubicarse al inicio, de tal manera que cuando la llames ya esta definido

        # Función para calcular retorno
def calcular_retorno(tasa, meses):
    if "actividades" in st.session_state and st.session_state.actividades:
        # Crear DataFrame
        df = pd.DataFrame(st.session_state.actividades)

        # Calcular Retorno
        df["Retorno"] = df.apply(lambda row: row["ppto"] * tasa * meses, axis=1)

        # Mostrar tabla
        st.subheader("Lista de actividades calculadas")
        st.dataframe(df, use_container_width=True)

    else:
        st.info("No hay actividades registradas")
        
        
def proceso_a():
    st.header("Home")
    st.title("Home")
    st.write("Proyecto   : Python Fundamentals")
    st.write("Estudiante : Carlos Mesta Castro")
    st.write("Curso      : Python Fundamentals")
    st.write("Año        : 2026")
    st.write("Descripción : Poner en práctica lo aprendido a travéz de las sesiones")
    st.write("              para cada uno de los puntos solicitados")
    st.write("Se aplico   : Python, Streamlit, Librerias tales como Panda, Numpy")

def proceso_b():
    
    st.title("Ejercicio 1")

    ppto = st.number_input("Ingrese Presupuesto",1,5000 )
    gasto = st.number_input("Ingrese Gasto",1,5000 )


    if st.button("Clic para validar"):

        diferencia = ppto - gasto

        if ppto > gasto:
             st.success("Presupuesto válido, mayor al gasto")

        elif ppto == gasto:
            st.success("Presupuesto IGUAL al gasto")

        else:
            st.warning("Presupuesto es MENOR al gasto")

        st.write("Diferencia es:", diferencia)

def proceso_c():
    st.title("Ejercicio 2")

    #creamos lista en memoria
    if "actividades" not in st.session_state:
        st.session_state.actividades = []
    
    # solicitamos datos
    nombre = st.text_input("Nombre")
    tipo = st.text_input("Tipo(A-B-C)")
    ppto = st.number_input("Ingrese Presupuesto",1,5000 )
    gasto = st.number_input("Ingrese Gasto" , 1 , 5000)
    
    #Validamos datos
    if tipo.upper() in ["A", "B" , "C"]:
        st.success("Valor válido")
    else:
        st.error("En Tipo Solo se permite A B C")

    #Botón agregar
    if st.button("Agregar actividad"):

        nueva_actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "ppto": ppto,
            "gasto": gasto
        }

        st.session_state.actividades.append(nueva_actividad)
        st.success("Actividad agregada correctamente")

#Mostrar lista acumulada y definimos campo estado para comparar
    if st.session_state.actividades:

        df = pd.DataFrame(st.session_state.actividades)
        df["Estado"] = df.apply(
        lambda row:
            "OK" if row["gasto"] < row["ppto"]
            else "Exacto" if row["gasto"] == row["ppto"]
            else "Excedido",
        axis=1
    )

        st.subheader("Lista de actividades")
        st.dataframe(df, use_container_width=True)
        

    else:
            st.info("No hay actividades registradas")

    

def proceso_d():
    st.header("Ejercicio 3-Usa lista de actividades Ejercicio 2")
    tasa = st.number_input("Ingrese tasa" , min_value=0.01, value=0.01, step=0.01)
    meses = st.number_input("Ingrese meses" , 1, 12)
    if st.button("Clic para calcular"):
        if "actividades" in st.session_state:
            if st.session_state.actividades:
                
                df = pd.DataFrame(st.session_state.actividades)
                df["Retorno"] = df.apply(
                lambda row:
                    row["ppto"] * tasa * meses ,             
                axis=1
            )
            st.subheader("Lista de actividades calculadas")
            st.dataframe(df, use_container_width=True)
        
        else:
            st.info("No hay actividades registradas")
    

def proceso_d1():
    st.header("Ejercicio 3-Usa lista de actividades Ejercicio 2")
    tasa = st.number_input("Ingrese tasa" , min_value=0.01, value=0.01, step=0.01)
    meses = st.number_input("Ingrese meses" , 1, 12)
    if st.button("Clic para calcular"):
        calcular_retorno(tasa, meses)



def proceso_e():
    st.header("Ejercicio 4-Usa lista de actividades Ejercicio 2")
    #Usamos clase, metoddos
    if st.button("Clic para Mostrar"):
        if "actividades" in st.session_state:
            if st.session_state.actividades:
              
             lista_dict = st.session_state.actividades

            # Convertir diccionarios en objetos
            lista_objetos = [Actividad(d["nombre"], d["tipo"], d["ppto"], d["gasto"]) for d in lista_dict]

            # Mostrar info de cada objeto
            for act in lista_objetos:
                st.markdown(f"```\n{act.mostrar_info()}\n```")
        else:
                st.info("No hay actividades registradas")


#----------------------------
# ----- MENÚ PRINCIPAL -----
#----------------------------

st.sidebar.title("Menú Principal-Carlos Mesta Castro")
st.sidebar.image("Logo.png", width=150)

opcion = st.sidebar.selectbox(
    "Selecciona una opción:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3" ,"Ejercicio 4" ] ,
     index=None,  # no selecciona nada por defecto
     placeholder="Por favor eligir una opción..." #Mensaje para el usuario
)

if opcion is not None:
    
    if opcion == "Home":
        proceso_a()
    elif opcion == "Ejercicio 1":
        proceso_b()
    elif opcion == "Ejercicio 2":
        proceso_c()
    elif opcion == "Ejercicio 3":
        #proceso_d()
        proceso_d1()
    elif opcion == "Ejercicio 4":
        proceso_e()
        
