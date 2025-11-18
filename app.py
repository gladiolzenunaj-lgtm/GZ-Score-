import streamlit as st

st.title("GZ Score 🩺")
st.write("Calcolatore di rischio di mortalità basato sul modello sviluppato da Dr. G. Zenunaj.")

st.header("Inserire le caratteristiche del paziente")

cad = st.checkbox("Coronaropatia documentata (CAD)")
fa = st.checkbox("Fibrillazione atriale (FA)")
dialisi = st.checkbox("Dialisi cronica")
ckd = st.checkbox("Insufficienza renale cronica (CKD ≥ stadio 3)")
clti = st.checkbox("Ischemia cronica critica (Rutherford 4–6)")
runoff_buono = st.checkbox("Run-off post-procedura BUONO")
des = st.checkbox("Impianto di DES (protettivo)")

beta = {
    "CAD": 0.45,
    "FA": 0.50,
    "CKD": 0.80,
    "Dialisi": 0.48,
    "CLTI": 1.60,
    "Runoff_buono": -0.36,
    "DES": -0.74
}

lp = 0
if cad: lp += beta["CAD"]
if fa: lp += beta["FA"]
if ckd: lp += beta["CKD"]
if dialisi: lp += beta["Dialisi"]
if clti: lp += beta["CLTI"]
if runoff_buono: lp += beta["Runoff_buono"]
if des: lp += beta["DES"]

st.subheader("Risultati del GZ Score")
st.write(f"**Linear Predictor (LP):** {lp:.2f}")

if lp < 0.5:
    rischio = "Basso"
elif lp < 2.0:
    rischio = "Intermedio"
else:
    rischio = "Alto"

st.write(f"**Classe di rischio:** {rischio}")

import math
def survival(t, lp):
    H0 = {1:0.005, 3:0.017, 5:0.026}
    return math.exp(-H0[t] * math.exp(lp))

st.write("### Sopravvivenza stimata")
st.write(f"**1 anno:** {survival(1, lp):.2%}")
st.write(f"**3 anni:** {survival(3, lp):.2%}")
st.write(f"**5 anni:** {survival(5, lp):.2%}")
