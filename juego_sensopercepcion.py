import streamlit as st
from PIL import Image

st.title("🧠 CognitiQuest: Sensopercepción Visual")

st.write("""
### Observa atentamente ambas imágenes y encuentra la diferencia:
""")

# Carga imágenes
img_original = Image.open("imagen_original.jpg")
img_modificada = Image.open("imagen_modificada.jpg")

# Mostrar imágenes lado a lado
col1, col2 = st.columns(2)

with col1:
    st.image(img_original, caption="Imagen Original", use_column_width=True)
with col2:
    st.image(img_modificada, caption="Imagen Modificada", use_column_width=True)

# Pregunta al jugador
respuesta = st.radio(
    "¿Cuál es la diferencia entre ambas imágenes?",
    ["Ninguna diferencia", "Falta un objeto", "Cambio de color", "Elemento adicional"]
)

# Verificación
if st.button("Revisar respuesta"):
    if respuesta == "Falta un objeto":
        st.success("¡Correcto! Identificaste correctamente la diferencia. 🎉")
    else:
        st.error("Respuesta incorrecta. ¡Inténtalo de nuevo!")

st.write("🔍 *Concéntrate y observa cuidadosamente antes de responder.*")
