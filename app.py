import streamlit as st

from market_data import get_market_data
from analysis_engine import analyze_asset
from config.settings import ASSETS


st.set_page_config(page_title="Forex AI", layout="wide")

st.title("FOREX AI")
st.write("Análise automática de mercado")

if st.button("Analisar mercado"):

    for asset in ASSETS:

        data = get_market_data(asset)

        result = analyze_asset(asset, data)

        st.markdown("---")

        st.subheader(asset)

        st.write("Direção:", result["direction"])
        st.write("Confiança:", result["confidence"], "%")

        st.write("Entrada:", result["entry"])
        st.write("Stop:", result["stop"])

        st.write("Take 1:", result["take1"])
        st.write("Take 2:", result["take2"])
        st.write("Take 3:", result["take3"])

        st.write("Motivos da análise:")

        for r in result["summary"]:
            st.write("-", r)
