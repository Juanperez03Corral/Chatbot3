#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 11:11:11 2025

@author: juan
"""

import streamlit as st

# Configuración de la app
st.set_page_config(page_title="Chin Chin - Tu Sumiller Virtual", page_icon="🍷", layout="centered")

# Estado de sesión
if 'bodega' not in st.session_state:
    st.session_state.bodega = []
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []
if 'supermercado_vinos' not in st.session_state:
    st.session_state.supermercado_vinos = [
        ("Lidl", "Albariño - 3,99€"),
        ("Mercadona", "Ribera del Duero - 5,99€"),
        ("Carrefour", "Rioja Crianza - 6,49€"),
        ("El Corte Inglés", "Verdejo - 7,50€")
    ]

# === FUNCIONES ===

def mostrar_planes():
    st.markdown("## 🧾 Planes de suscripción")
    st.info("""
    **Plan 1 – Gratis**  
    - Comparación de vinos en supermercados  
    - Acceso a rankings  
    - 3 recomendaciones semanales  

    **Plan 2 – 9,99€/mes**  
    - Recomendaciones ilimitadas  
    - Registro y control de bodega  

    **Plan 3 – 24,99€/mes**  
    - Todo lo anterior  
    - Pack mensual de 3 vinos  
    - Catas virtuales  

    **Plan 4 – 49,99€/mes**  
    - Todo lo anterior  
    - Acceso a eventos y visitas a bodegas  
    - Descuentos en vinos y actividades  
    """)

def recomendaciones_comida(plan):
    st.subheader("🍽️ ¿Qué estás comiendo?")
    comida = st.selectbox("Tipo de comida", [
        "Carne roja", "Carne blanca", "Pescado", "Marisco",
        "Pasta con salsa", "Quesos fuertes", "Quesos suaves", "Dulces",
        "Ensaladas", "Vegetariano", "Barbacoa"
    ])

    recomendaciones = {
        "Carne roja": "Cabernet Sauvignon, Syrah, Ribera del Duero",
        "Carne blanca": "Garnacha suave, Chardonnay con barrica",
        "Pescado": "Albariño, Verdejo, Godello",
        "Marisco": "Rías Baixas, Sauvignon Blanc",
        "Pasta con salsa": "Chianti, Tempranillo joven",
        "Quesos fuertes": "Oporto, Syrah",
        "Quesos suaves": "Rosado seco o Chardonnay",
        "Dulces": "Moscatel, PX, cava semiseco",
        "Ensaladas": "Verdejo, rosado joven",
        "Vegetariano": "Pinot Noir, Riesling",
        "Barbacoa": "Zinfandel, Malbec"
    }

    st.success(f"🍷 Recomendación: {recomendaciones[comida]}")
    if plan != "Gratis" and st.button("Guardar en favoritos"):
        st.session_state.favoritos.append(f"{comida}: {recomendaciones[comida]}")
        st.toast("¡Añadido a favoritos!")

def gestion_bodega(plan):
    if plan in ["9,99€/mes", "24,99€/mes", "49,99€/mes"]:
        st.subheader("📦 Tu Bodega Personal")
        for vino in st.session_state.bodega:
            st.write(f"🍾 {vino}")
        nuevo = st.text_input("Añadir vino")
        if st.button("Agregar"):
            if nuevo:
                st.session_state.bodega.append(nuevo)
                st.success(f"'{nuevo}' añadido a tu bodega.")
            else:
                st.warning("Introduce un nombre válido.")
    else:
        st.warning("Función disponible a partir del Plan 2.")

def comparar_supermercados():
    st.subheader("🛒 Comparativa de Vinos en Supermercados")
    for tienda, vino in st.session_state.supermercado_vinos:
        st.write(f"**{tienda}** → {vino}")

def ver_favoritos():
    st.subheader("⭐ Favoritos")
    if st.session_state.favoritos:
        for fav in st.session_state.favoritos:
            st.write(f"👉 {fav}")
    else:
        st.info("No tienes favoritos guardados.")

def suscripcion_mensual(plan):
    if plan in ["24,99€/mes", "49,99€/mes"]:
        st.success("""
        Tu pack mensual de 3 vinos está en camino.  
        Incluye cata virtual con nota de cata y maridaje.
        """)
    else:
        st.warning("Disponible desde el Plan 3.")

def actividades_y_visitas(plan):
    if plan == "49,99€/mes":
        st.balloons()
        st.markdown("""
        ### 🍇 Próximas experiencias
        - Visita a bodega en Ribera del Duero – 12 de mayo  
        - Cata sensorial avanzada – 25 de mayo  
        - Degustación premium con maridaje – 2 de junio  
        **Descuento aplicado automáticamente.**
        """)
    else:
        st.warning("Disponible solo para el Plan 4.")

# === APP ===

st.title("🍷 Chin Chin – Tu Sumiller Virtual para Particulares")

mostrar_planes()

plan = st.selectbox("Selecciona tu plan actual", ["Gratis", "9,99€/mes", "24,99€/mes", "49,99€/mes"])

seccion = st.radio("¿Qué quieres hacer?", [
    "📌 Recomendaciones por comida",
    "📦 Mi bodega",
    "⭐ Favoritos",
    "📬 Suscripción mensual",
    "🎟️ Actividades y eventos",
    "🛒 Comparar vinos de supermercado"
])

if seccion == "📌 Recomendaciones por comida":
    recomendaciones_comida(plan)

elif seccion == "📦 Mi bodega":
    gestion_bodega(plan)

elif seccion == "⭐ Favoritos":
    ver_favoritos()

elif seccion == "📬 Suscripción mensual":
    suscripcion_mensual(plan)

elif seccion == "🎟️ Actividades y eventos":
    actividades_y_visitas(plan)

elif seccion == "🛒 Comparar vinos de supermercado":
    comparar_supermercados()