
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

st.set_page_config(page_title="TFM: Explorador Biomédico", layout="wide")
st.title("🧬 Explorador de relaciones biomédicas con amoxicilina")

# Cargar datos
df = pd.read_csv("relaciones_contextuales_amoxicilina.csv")

# Filtro por tipo de relación
tipo = st.selectbox("🔎 Selecciona el tipo de relación", df["relación"].unique())
df_tipo = df[df["relación"] == tipo]

# Filtro por fármaco (CHEMICAL)
quimicos = df_tipo["CHEMICAL"].value_counts().index.tolist()
quimico_sel = st.selectbox("💊 Filtrar por sustancia química (CHEMICAL)", ["(todos)"] + quimicos)

if quimico_sel != "(todos)":
    df_filtrado = df_tipo[df_tipo["CHEMICAL"] == quimico_sel]
else:
    df_filtrado = df_tipo

# Mostrar tabla
st.subheader("📋 Relaciones encontradas")
st.dataframe(df_filtrado[["CHEMICAL", "DISEASE", "oración"]].reset_index(drop=True))

# Mostrar gráfico de barras
st.subheader("📊 Condiciones clínicas más frecuentes")
top_disease = df_filtrado["DISEASE"].value_counts().head(10)
fig_bar, ax = plt.subplots(figsize=(8, 4))
sns.barplot(y=top_disease.index, x=top_disease.values, ax=ax, palette="Reds_r")
ax.set_xlabel("Frecuencia")
ax.set_ylabel("Condición clínica (DISEASE)")
st.pyplot(fig_bar)

# Mostrar red de relaciones
if tipo in ["efecto_adverso", "causa", "tratamiento"]:
    st.subheader("🕸️ Red de relaciones CHEMICAL–DISEASE")

    G = nx.Graph()
    for row in df_filtrado.itertuples():
        G.add_edge(row.CHEMICAL, row.DISEASE)

    fig, ax = plt.subplots(figsize=(10, 6))
    pos = nx.spring_layout(G, k=0.9, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=800,
            font_size=10, edge_color="gray", ax=ax)
    st.pyplot(fig)

# Opción de descarga
st.subheader("⬇️ Descargar resultados filtrados")
st.download_button("Descargar CSV", data=df_filtrado.to_csv(index=False), file_name="resultados_filtrados.csv", mime="text/csv")
