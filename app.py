import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="SafeBet IA", layout="wide")

# --- INTERFACE ---
st.title("🛡️ SafeBet IA - Gestão & Scanner")

# Inicializar histórico na memória
if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=[
        'Data', 'Evento', 'Mercado', 'Odd', 'Stake', 'Resultado', 'Lucro'
    ])

# --- ABAS DO APP ---
tab1, tab2, tab3 = st.tabs(["📡 Scanner", "📈 Dashboard ROI", "📊 Gráficos"])

with tab1:
    st.subheader("Oportunidades Pré-Live")
    st.info("Scanner ativo: Buscando odds desreguladas...")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("**Exemplo: Real Madrid x Barcelona** | Mercado: Cantos | Odd: 2.10")
    with col2:
        if st.button("Registrar Aposta"):
            nova_aposta = {
                'Data': datetime.now().strftime("%d/%m/%Y"),
                'Evento': "Real Madrid x Barcelona",
                'Mercado': "Cantos",
                'Odd': 2.10,
                'Stake': 100.0,
                'Resultado': 'Green',
                'Lucro': 110.0
            }
            st.session_state.historico = pd.concat([st.session_state.historico, pd.DataFrame([nova_aposta])], ignore_index=True)
            st.success("Aposta registrada!")

with tab2:
    st.subheader("Minha Gestão")
    df = st.session_state.historico
    if not df.empty:
        total_lucro = df['Lucro'].sum()
        st.metric("Lucro Total", f"R$ {total_lucro:.2f}")
        st.dataframe(df, use_container_width=True)
    else:
        st.write("Nenhuma aposta ainda.")

with tab3:
    st.subheader("Desempenho")
    if not df.empty:
        fig = px.line(df, y='Lucro', title="Evolução do Lucro")
        st.plotly_chart(fig, use_container_width=True)
