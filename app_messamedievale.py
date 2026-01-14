# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

# 1. Configurazione obbligatoria (Deve essere la prima istruzione)
st.set_page_config(
    page_title="La Liturgia Medievale: Guida Completa",
    page_icon="S",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FUNZIONE PER GENERARE IL TESTO DELLA DISPENSA ---
def genera_contenuto_dispensa():
    return """GUIDA DIDATTICA: LA LITURGIA E IL CANTO NEL MEDIOEVO

1. LA STRUTTURA DELLA MESSA
- Ordinarium (Testi Fissi): Kyrie, Gloria, Credo, Sanctus, Agnus Dei.
- Proprium (Testi Variabili): Introitus, Graduale, Alleluia/Tractus, Offertorium, Communio.

2. IL CANTO GREGORIANO E LA NOTAZIONE
- Origine: Unificazione carolingia (VIII-IX sec.).
- Evoluzione Scrittura: Neumi in campo aperto -> Diastemazia -> Notazione Quadrata.
- Scuole Regionali: Sangallese, Francese, Aquitana, Beneventana, Gotica.
- Principali Neumi: Punctum, Virga, Pes, Clivis, Scandicus, Climacus, Torculus, Porrectus, ecc.
- Guido d'Arezzo: Tetragramma e nomi delle note.

3. ESEMPIO PRATICO: KYRIE ORBIS FACTOR
- Analisi della notazione quadrata e dello stile melismatico.

4. SVILUPPO DELLA POLIFONIA PRIMITIVA
- Organum Parallelo, Melismatico e Scuola di Notre Dame.

5. INTEGRAZIONE DEL PROFANO E MESSA CICLICA
- Cantus Firmus, L'Homme Armé, Machaut e Dufay.

6. GLI 8 MODI (OCTOECHOS)
- Suddivisi in Autentici (dispari) e Plagali (pari) con i nomi greci e moderni.
"""

# --- CSS PER L'ESTETICA "MEDIEVALE" E LEGGIBILITÀ ---
st.markdown("""
    <style>
    .main { background-color: #fdf6e3; }
    .stMarkdown h1, h2, h3 { color: #4e342e; font-family: 'serif'; }
    
    .medieval-container {
        padding: 1.5rem;
        border-radius: 0.8rem;
        background-color: #fffde7;
        border-left: 6px solid #795548;
        color: #2e1a16;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .poly-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #d7ccc8;
        color: #3e2723;
        height: 100%;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .timeline-item {
        border-left: 2px solid #8d6e63;
        padding-left: 20px;
        margin-bottom: 20px;
        position: relative;
    }

    .dark-section {
        background-color: #2d1b15;
        color: #f5f5f5;
        padding: 2.5rem;
        border-radius: 1rem;
        margin: 1.5rem 0;
        border: 1px solid #4e342e;
    }
    .dark-section h3 {
        color: #ffd54f !important;
        margin-top: 1.5rem;
    }

    .tech-box {
        padding: 1.2rem;
        background-color: #efebe9;
        border-radius: 0.5rem;
        border: 1px solid #8d6e63;
        color: #3e2723;
        font-size: 0.95rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header("Area Studio")
    st.markdown("---")
    st.info("**Obiettivi Didattici:**\n- Distinguere Ordinario e Proprio.\n- Evoluzione della notazione e scuole regionali.\n- Analizzare l'Octoechos con nomi moderni.")
    
    st.download_button(
        label="Scarica Dispensa Completa",
        data=genera_contenuto_dispensa(),
        file_name="dispensa_messa_medievale.txt",
        mime="text/plain"
    )
    st.divider()
    st.caption("Versione 2.7 - Reintegro nomi modi (Dorico ecc.)")

# --- TITOLO ---
st.title("La Liturgia e il Canto nel Medioevo")
st.markdown("#### *Dalla Monodia Gregoriana alla Polifonia Fiamminga*")
st.divider()

# --- SEZIONE 1: LA MESSA ---
st.header("1. La Struttura della Messa")
st.markdown('<div class="medieval-container">La Messa si divide in due cicli: l\'<b>Ordinarium</b> (testi fissi immutabili) e il <b>Proprium</b> (testi variabili secondo la festa del giorno).</div>', unsafe_allow_html=True)

tab_ord, tab_prop = st.tabs(["Ordinarium Missae", "Proprium Missae"])

with tab_ord:
    df_ord = pd.DataFrame({
        "Parte": ["Kyrie Eleison", "Gloria", "Credo", "Sanctus", "Agnus Dei"],
        "Descrizione": ["Invocazione alla misericordia (Greco)", "Inno di lode solenne", "Professione di fede", "Inno angelico", "Preghiera per la frazione del pane"],
        "Stile Tipico": ["Melismatico", "Neumatico/Sillabico", "Sillabico", "Neumatico", "Neumatico"]
    })
    st.table(df_ord)

with tab_prop:
    df_prop = pd.DataFrame({
        "Parte": ["Introitus", "Graduale", "Alleluia / Tractus", "Offertorium", "Communio"],
        "Momento": ["Ingresso", "Dopo l'Epistola", "Prima del Vangelo", "Offerta", "Comunione"],
        "Funzione": ["Processionale", "Meditativa", "Acclamativa", "Processionale", "Processionale"]
    })
    st.table(df_prop)

# --- SEZIONE 2: IL CANTO GREGORIANO ---
st.header("2. Il Canto Gregoriano e gli Stili")
col_g1, col_g2 = st.columns(2)

with col_g1:
    st.subheader("Storia e Caratteristiche")
    st.write("""
    Nato dall'unificazione carolingia (VIII-IX sec.), il canto gregoriano è la base della musica occidentale. 
    È **monodico**, a cappella, in latino e segue il ritmo del testo (ritmo libero).
    """)

with col_g2:
    st.subheader("I Tre Stili Melodici")
    st.markdown("""
    - **Sillabico**: Ogni sillaba corrisponde a una nota (es. Salmi, Credo).
    - **Neumatico**: Piccoli gruppi di note (2-4) per sillaba (es. Introitus).
    - **Melismatico**: Lunghe fioriture su una sola sillaba (es. Alleluia).
    """)

# --- SEZIONE 3: EVOLUZIONE DELLA NOTAZIONE ---
st.header("3. Evoluzione della Scrittura Musicale")
col_time, col_guido = st.columns([2, 1.2])

with col_time:
    st.subheader("Linea del Tempo della Notazione")
    st.markdown("""
    <div class="timeline-item">
        <strong>IX - X Secolo: Neumi in "Campo Aperto"</strong><br>
        Segni posti sopra il testo senza linee di riferimento. Servivano come ausilio mnemonico.
    </div>
    <div class="timeline-item">
        <strong>X - XI Secolo: Diastemazia</strong><br>
        Introduzione di linee colorate (rossa per il FA, gialla per il DO).
    </div>
    <div class="timeline-item">
        <strong>XI Secolo: Il Tetragramma</strong><br>
        Sistematizzazione del rigo a quattro linee da parte di Guido d'Arezzo.
    </div>
    """, unsafe_allow_html=True)

    # Tabella Comparativa Scuole Regionali
    st.subheader("Confronto tra Scuole Regionali di Notazione")
    scuole_df = pd.DataFrame({
        "Scuola": ["Sangallese", "Aquitana", "Beneventana", "Gotica (Hufnagel)", "Quadrata"],
        "Caratteristiche Grafiche": [
            "Segni sottili e corsivi, alta precisione ritmica, senza rigo.",
            "Notazione 'a punti' (punti staccati), precorritrice della diastemazia.",
            "Tratti spessi e inclinati, tipica dell'area di Montecassino.",
            "Segni simili a chiodi da maniscalco (ferri di cavallo), area germanica.",
            "Note a forma di quadrato su tetragramma, standard liturgico finale."
        ]
    })
    st.table(scuole_df)

    st.subheader("I Principali Neumi (Semplici e Composti)")
    neumi_df = pd.DataFrame({
        "Neuma": ["Punctum / Virga", "Pes (Podatus)", "Clivis", "Scandicus / Climacus", "Torculus / Porrectus", "Pes subbipunctis", "Torculus resupinus"],
        "Movimento Melodico": ["Nota singola", "Ascendente (2 note)", "Discendente (2 note)", "3 note (Asc. / Disc.)", "3 note (B-A-B / A-B-A)", "4 note (1 acuta + 3 gravi)", "4 note (B-A-B-A)"]
    })
    st.table(neumi_df)

with col_guido:
    st.markdown("""
    <div class="medieval-container" style="background-color: #f5f5f5; border-left-color: #4e342e;">
        <h3 style="margin-top:0;">Focus: Guido d'Arezzo</h3>
        <p>Monaco teorico, inventore del rigo e della solmisazione:</p>
        <ul>
            <li><strong>Tetragramma:</strong> Rigo di 4 linee.</li>
            <li><strong>Inno a S. Giovanni:</strong> Ut, Re, Mi, Fa, Sol, La.</li>
            <li><strong>Mano Guidoniana:</strong> Metodo mnemonico per l'insegnamento.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- SEZIONE ESEMPIO PRATICO KYRIE ---
st.divider()
st.header("Esempio Pratico: Kyrie 'Orbis Factor' (Mass XI)")

st.markdown("""
<div class="tech-box">
    <strong>Analisi Tecnica dell'Esempio:</strong><br><br>
    Il <b>Kyrie Orbis Factor</b> illustra perfettamente la maturità della <b>notazione quadrata</b> su tetragramma:<br>
    <ul>
        <li><b>Melismi:</b> Grandi gruppi di neumi concentrati su singole sillabe, che creano una linea melodica ricca e ornata.</li>
        <li><b>Custos:</b> Il piccolo segno a fine rigo che anticipa la posizione della prima nota del rigo successivo.</li>
        <li><b>Alterazioni:</b> L'uso del <i>B-mollis</i> (Si bemolle), l'unica alterazione ammessa nel gregoriano.</li>
        <li><b>Chiavi:</b> Presenza delle chiavi di DO o FA all'inizio del rigo per fissare l'altezza dei suoni.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- SEZIONE 4: SVILUPPO DELLA POLIFONIA ---
st.header("4. Lo Sviluppo della Polifonia Primitiva")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="poly-card"><b>Organum Parallelo</b><br><br>Raddoppio della melodia a distanza di 4ª o 5ª costante.</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="poly-card"><b>Organum Melismatico</b><br><br>Tenore a note lunghe, voce superiore con melismi liberi.</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="poly-card"><b>Scuola di Notre Dame</b><br><br>Introduzione del ritmo misurato (Leoninus e Perotinus).</div>', unsafe_allow_html=True)

# --- SEZIONE 5: INTEGRAZIONE DEL PROFANO ---
st.header("5. Il Sacro e il Profano: Chansons e Messe")
col_p1, col_p2 = st.columns([2, 1])

with col_p1:
    st.subheader("L'uso delle Chansons nella Messa")
    st.write("Dal XV secolo, l'uso del **Cantus Firmus** profano permetteva coesione strutturale e simbolismo teologico (es. L'Homme Armé).")

with col_p2:
    st.markdown('<div class="tech-box"><b>Cantus Firmus</b>: Melodia profana <b>fissata</b> nel <b>Tenor</b> a note lunghe.</div>', unsafe_allow_html=True)

# --- SEZIONE 6: I GRANDI MAESTRI ---
st.header("6. I Maestri della Messa Ciclica")
st.markdown("""
<div class="dark-section">
    <h3>Guillaume de Machaut</h3>
    <p>Messe de Nostre Dame (1365): prima messa ciclica unitaria basata sull'Isoritmia.</p>
    <hr style='border-color: #5d4037; margin: 1.5rem 0;'>
    <h3>Guillaume Dufay</h3>
    <p>Missa L'homme armé: applicazione di proporzioni ritmiche matematiche al tema profano nel Tenore.</p>
</div>
""", unsafe_allow_html=True)

# --- SEZIONE 7: MODI GREGORIANI ---
st.header("7. Il Sistema dell'Octoechos (8 Modi)")
modi_data = {
    "N.": [1, 2, 3, 4, 5, 6, 7, 8],
    "Nome Liturgico": ["Protus Aut.", "Protus Plag.", "Deuterus Aut.", "Deuterus Plag.", "Tritus Aut.", "Tritus Plag.", "Tetrardus Aut.", "Tetrardus Plag."],
    "Nome Moderno": ["Dorico", "Ipodorico", "Frigio", "Ipofrigio", "Lidio", "Ipolidio", "Misolidio", "Ipomisolidio"],
    "Finalis": ["Re", "Re", "Mi", "Mi", "Fa", "Fa", "Sol", "Sol"],
    "Tenor": ["La", "Fa", "Do", "La", "Do", "La", "Re", "Do"]
}
st.dataframe(pd.DataFrame(modi_data), hide_index=True, use_container_width=True)

st.divider()
st.caption("Risorsa didattica sulla Musica Medievale - Analisi Formale e Storica.")