import streamlit as st
import pandas as pd

# 1. QUESTA DEVE ESSERE LA PRIMA ISTRUZIONE ASSOLUTA
# Se metti qualsiasi altra cosa prima di st.set_page_config, l'app darà errore su Streamlit Cloud.
st.set_page_config(
    page_title="La Messa Medievale",
    page_icon="📜",
    layout="wide"
)

# Funzione per generare il testo della dispensa
def genera_testo():
    return """SINTESI DIDATTICA: LA MESSA E LA POLIFONIA MEDIEVALE

1. LA MESSA
- Ordinario: Testi fissi (Kyrie, Gloria, Credo, Sanctus, Agnus Dei).
- Proprio: Testi variabili (Introitus, Graduale, Alleluia, Offertorium, Communio).

2. POLIFONIA PRIMITIVA
- Organum Parallelo: Quinta/quarta parallela.
- Organum Melismatico: Note lunghe al Tenore.
- Scuola di Notre Dame: Nascita dei modi ritmici.

3. INTEGRAZIONE DEL PROFANO
- Cantus Firmus: Melodia di chanson 'fissata' nel Tenore.
- L'Homme Armé: Cristo Soldato che vince il male.

4. AUTORI
- Machaut: Messe de Nostre Dame (unità ciclica).
- Dufay: Missa L'homme armé (proporzioni matematiche).
"""

# Stile estetico "Medievale"
st.markdown("""
    <style>
    .main { background-color: #fdf6e3; }
    .stMarkdown h1, h2, h3 { color: #5d4037; font-family: 'serif'; }
    .medieval-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #fff9c4;
        border-left: 5px solid #8b4513;
        margin-bottom: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Barra laterale con download
with st.sidebar:
    st.header("📜 Strumenti")
    st.download_button(
        label="📥 Scarica Dispensa",
        data=genera_testo(),
        file_name="dispensa_medievale.txt",
        mime="text/plain"
    )
    st.info("Usa questa app per ripassare le parti della messa e la teoria dei modi.")

# Titolo e Contenuto
st.title("📜 La Liturgia Medievale")
st.markdown("#### *Dalla Monodia alla Polifonia Ciclica*")
st.divider()

# Sezione 1: Messa
st.header("1. La Struttura della Messa")
col_ord, col_prop = st.tabs(["🏛️ Ordinarium", "📅 Proprium"])

with col_ord:
    st.table(pd.DataFrame({
        "Parte": ["Kyrie", "Gloria", "Credo", "Sanctus", "Agnus Dei"],
        "Stile": ["Melismatico", "Neumatico", "Sillabico", "Neumatico", "Neumatico"]
    }))

with col_prop:
    st.table(pd.DataFrame({
        "Parte": ["Introitus", "Graduale", "Alleluia", "Offertorium", "Communio"],
        "Funzione": ["Ingresso", "Meditazione", "Acclamazione", "Offerta", "Comunione"]
    }))

# Sezione 2: Polifonia
st.header("2. Lo Sviluppo della Polifonia")
c1, c2, c3 = st.columns(3)
with c1:
    st.subheader("Organum Parallelo")
    st.write("Raddoppio della melodia a intervalli fissi (4ª o 5ª).")
with c2:
    st.subheader("Organum Melismatico")
    st.write("Tenore a note lunghissime, voce superiore ornata.")
with c3:
    st.subheader("Notre Dame")
    st.write("Leoninus e Perotinus: invenzione del ritmo misurato.")

# Sezione 3: Il Profano nel Sacro
st.header("3. Integrazione del Profano")
st.markdown("""
<div class="medieval-box">
<b>Cantus Firmus:</b> Una melodia di chanson (come <i>L'Homme Armé</i>) viene <b>fissata</b> 
nel Tenore come impalcatura per l'intera Messa.
</div>
""", unsafe_allow_html=True)

# Sezione 4: Maestri
st.header("4. I Grandi Maestri")
st.write("**Guillaume de Machaut**: La prima messa ciclica unitaria.")
st.write("**Guillaume Dufay**: L'uso magistrale del Cantus Firmus profano.")

# Sezione 5: Modi
st.header("5. Sistema dei Modi (Octoechos)")
modi = {
    "N.": [1, 2, 3, 4, 5, 6, 7, 8],
    "Nome": ["Protus Aut.", "Protus Plag.", "Deuterus Aut.", "Deuterus Plag.", "Tritus Aut.", "Tritus Plag.", "Tetrardus Aut.", "Tetrardus Plag."],
    "Finalis": ["Re", "Re", "Mi", "Mi", "Fa", "Fa", "Sol", "Sol"]
}
st.dataframe(pd.DataFrame(modi), hide_index=True, use_container_width=True)

st.divider()
st.caption("Risorsa didattica per studenti.")