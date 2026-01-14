import streamlit as st
import pandas as pd

# 1. Configurazione obbligatoria (Deve essere la prima istruzione)
st.set_page_config(
    page_title="La Liturgia Medievale: Guida Completa",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FUNZIONE PER GENERARE IL TESTO DELLA DISPENSA ---
def genera_contenuto_dispensa():
    return """GUIDA DIDATTICA: LA LITURGIA E IL CANTO NEL MEDIOEVO

1. LA STRUTTURA DELLA MESSA
- Ordinarium (Testi Fissi): Kyrie, Gloria, Credo, Sanctus, Agnus Dei.
- Proprium (Testi Variabili): Introitus, Graduale, Alleluia/Tractus, Offertorium, Communio.

2. IL CANTO GREGORIANO
- Origine: Unificazione carolingia (VIII-IX sec.). Canto monodico, a cappella, ritmo libero.
- Stili: Sillabico (1 nota/sillaba), Neumatico (2-4 note/sillaba), Melismatico (ornato).

3. SVILUPPO DELLA POLIFONIA PRIMITIVA
- Organum Parallelo: Raddoppio a intervalli di 4ª o 5ª.
- Organum Melismatico: Note lunghissime al Tenore (tenere), fioriture superiori.
- Scuola di Notre Dame: Leoninus e Perotinus introducono la misura del tempo.

4. INTEGRAZIONE DEL PROFANO E MESSA CICLICA
- Cantus Firmus: Melodia di una 'chanson' fissata nel Tenore come impalcatura.
- L'Homme Armé: Simbolo di Cristo Soldato.
- Guillaume de Machaut: Prima messa ciclica unitaria (Messe de Nostre Dame).
- Guillaume Dufay: Proporzioni matematiche applicate al tema profano.

5. GLI 8 MODI (OCTOECHOS)
- Suddivisi in Autentici (dispari) e Plagali (pari) con diverse Finalis e Tenor.
"""

# --- CSS PER L'ESTETICA "MEDIEVALE" E LEGGIBILITÀ ---
st.markdown("""
    <style>
    /* Sfondo generale */
    .main { background-color: #fdf6e3; }
    
    /* Titoli */
    .stMarkdown h1, h2, h3 { color: #4e342e; font-family: 'serif'; }
    
    /* Contenitore giallo chiaro (Sezione 1 e 4) */
    .medieval-container {
        padding: 1.5rem;
        border-radius: 0.8rem;
        background-color: #fffde7;
        border-left: 6px solid #795548;
        color: #2e1a16;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Card polifonia (Sezione 3) */
    .poly-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #d7ccc8;
        color: #3e2723;
        height: 100%;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Sezione Scura (Sezione 5) - Ottimizzata per contrasto */
    .dark-section {
        background-color: #2d1b15;
        color: #f5f5f5;
        padding: 2.5rem;
        border-radius: 1rem;
        margin: 1.5rem 0;
        border: 1px solid #4e342e;
    }
    .dark-section h3 {
        color: #ffd54f !important; /* Giallo brillante per risaltare sul marrone scuro */
        margin-top: 1.5rem;
    }
    .dark-section p {
        color: #eceff1;
        line-height: 1.6;
    }

    /* Box evidenziatore tecnico (Cantus Firmus) */
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
    st.header("📜 Area Studio")
    st.markdown("---")
    st.info("**Obiettivi Didattici:**\n- Distinguere Ordinario e Proprio.\n- Comprendere l'evoluzione polifonica.\n- Analizzare il rapporto Sacro/Profano.")
    
    st.download_button(
        label="📥 Scarica Dispensa Completa",
        data=genera_contenuto_dispensa(),
        file_name="dispensa_messa_medievale.txt",
        mime="text/plain"
    )
    st.divider()
    st.caption("Versione 2.1 - Ottimizzazione Contrasto")

# --- TITOLO ---
st.title("📜 La Liturgia e il Canto nel Medioevo")
st.markdown("#### *Dalla Monodia Gregoriana alla Polifonia Fiamminga*")
st.divider()

# --- SEZIONE 1: LA MESSA ---
st.header("1. La Struttura della Messa")
st.markdown('<div class="medieval-container">La Messa si divide in due cicli: l\'<b>Ordinarium</b> (testi fissi immutabili) e il <b>Proprium</b> (testi variabili secondo la festa del giorno).</div>', unsafe_allow_html=True)

tab_ord, tab_prop = st.tabs(["🏛️ Ordinarium Missae", "📅 Proprium Missae"])

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

# --- SEZIONE 3: SVILUPPO DELLA POLIFONIA ---
st.header("3. Lo Sviluppo della Polifonia Primitiva")
st.write("Come la musica è passata da una singola linea melodica a strutture complesse.")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="poly-card"><b>Organum Parallelo (IX sec.)</b><br><br>La forma più antica. Una seconda voce segue la melodia gregoriana a distanza di 4ª o 5ª costante.</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="poly-card"><b>Organum Melismatico (XII sec.)</b><br><br>Tipico di San Marziale. Il Tenore tiene note lunghissime del gregoriano, mentre la voce superiore "vola" con melismi.</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="poly-card"><b>Scuola di Notre Dame (XIII sec.)</b><br><br>Leoninus e Perotinus introducono la misura del tempo e polifonie a 3 e 4 voci indipendenti.</div>', unsafe_allow_html=True)

# --- SEZIONE 4: INTEGRAZIONE DEL PROFANO ---
st.header("4. Il Sacro e il Profano: Chansons e Messe")
col_p1, col_p2 = st.columns([2, 1])

with col_p1:
    st.subheader("L'uso delle Chansons nella Messa")
    st.write("""
    Dal XV secolo, i compositori iniziano a usare melodie di **chansons** popolari come fondamento per le Messe. 
    Questa pratica garantiva unità strutturale e permetteva di omaggiare i committenti tramite il simbolismo.
    """)
    with st.expander("La Giustificazione Teologica (Allegoria)"):
        st.write("""
        L'uso di testi d'amore o di guerra era accettato tramite l'allegoria:
        - **Dufay**: Il "pallore d'amore" della chanson veniva associato al pallore di Cristo durante la Passione.
        - **L'Homme Armé**: Il guerriero diventava l'immagine di Cristo Soldato che trionfa sulla morte.
        """)

with col_p2:
    st.subheader("La Tecnica")
    st.markdown('<div class="tech-box"><b>Cantus Firmus</b>: La melodia profana viene <b>fissata</b> nel <b>Tenor</b> a note lunghe. Questa voce funge da spina dorsale per l\'intera composizione.</div>', unsafe_allow_html=True)

# --- SEZIONE 5: I GRANDI MAESTRI ---
st.header("5. I Maestri della Messa Ciclica")

st.markdown("""
<div class="dark-section">
    <h3>Guillaume de Machaut: La Messa Ciclica</h3>
    <p>Con la <b>Messe de Nostre Dame</b> (1365), Machaut crea il primo ciclo completo dell'Ordinario concepito come opera unitaria. 
    Utilizza la tecnica dell'<b>Isoritmia</b> per legare i movimenti matematicamente e stilisticamente.</p>
    <hr style='border-color: #5d4037; margin: 1.5rem 0;'>
    <h3>Guillaume Dufay e "L'homme armé"</h3>
    <p>Dufay consacra la melodia profana più famosa del secolo. Nella sua Messa, il tema de <i>L'homme armé</i> 
    compare nel Tenore con diverse <b>proporzioni ritmiche</b>, creando un'accelerazione progressiva verso l'Agnus Dei.</p>
</div>
""", unsafe_allow_html=True)

# --- SEZIONE 6: MODI GREGORIANI ---
st.header("6. Il Sistema dell'Octoechos (8 Modi)")
modi_data = {
    "N.": [1, 2, 3, 4, 5, 6, 7, 8],
    "Nome": ["Protus Aut.", "Protus Plag.", "Deuterus Aut.", "Deuterus Plag.", "Tritus Aut.", "Tritus Plag.", "Tetrardus Aut.", "Tetrardus Plag."],
    "Finalis": ["Re", "Re", "Mi", "Mi", "Fa", "Fa", "Sol", "Sol"],
    "Tenor (Repercussio)": ["La", "Fa", "Do", "La", "Do", "La", "Re", "Do"]
}
st.dataframe(pd.DataFrame(modi_data), hide_index=True, use_container_width=True)

with st.expander("Visualizza l'Ethos (Carattere) dei Modi"):
    st.write("""
    1. **Grave** (Maestà) | 2. **Triste** (Umiltà) | 3. **Ardente** (Severità) | 4. **Lusinghiero** (Dolcezza) | 
    5. **Lieto** (Gioia) | 6. **Devoto** (Sobrietà) | 7. **Angelico** (Forza) | 8. **Perfetto** (Equilibrio)
    """)

st.divider()
st.caption("Risorsa didattica sulla Musica Medievale e Fiamminga - Analisi Formale e Storica.")