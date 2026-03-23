
Copy

import streamlit as st
 
# --- Page Config ---
st.set_page_config(
    page_title="GreenLog",
    page_icon="🌿",
    layout="wide"
)
 
# --- Strain Database ---
STRAINS = {
    "Indica": [
        "Granddaddy Purple", "Northern Lights", "Blueberry", "Bubba Kush",
        "Afghan Kush", "Hindu Kush", "Purple Punch", "Blackberry Kush",
        "G13", "MK Ultra", "Skywalker", "Kosher Kush", "Purple Urkle",
        "Pre-98 Bubba Kush", "LA Confidential", "Death Star", "Master Kush",
        "Purple Afghani", "Obama Kush", "Grape Ape", "Platinum OG",
        "Ice Cream Cake", "Forbidden Fruit", "Do-Si-Dos", "Wedding Cake"
    ],
    "Sativa": [
        "Sour Diesel", "Jack Herer", "Green Crack", "Durban Poison",
        "Super Silver Haze", "Strawberry Cough", "Trainwreck", "Maui Wowie",
        "Amnesia Haze", "Super Lemon Haze", "Chocolope", "Ghost Train Haze",
        "Tangie", "Lemon Haze", "Pineapple Express", "Acapulco Gold",
        "Panama Red", "Laughing Buddha", "Kali Mist", "Neville's Haze",
        "Hawaiian", "Candy Jack", "Voodoo", "Sage", "Cinderella 99"
    ],
    "Hybrid": [
        "OG Kush", "Girl Scout Cookies", "Blue Dream", "Gelato",
        "Wedding Cake", "Gorilla Glue #4", "White Widow", "AK-47",
        "Chemdawg", "Bruce Banner", "Runtz", "Sherbet", "Sunset Sherbet",
        "Zkittlez", "Mimosa", "Cereal Milk", "Gary Payton", "Biscotti",
        "London Pound Cake", "Permanent Marker", "Grease Monkey",
        "Animal Cookies", "Alien OG", "Fire OG", "Headband",
        "Skywalker OG", "Trinity", "Tahoe OG", "Chem 91",
        "Cookies and Cream", "Mac 1", "Tropicana Cookies", "Purple Gelato",
        "Jealousy", "Zerbert", "Papaya", "Watermelon Zkittlez"
    ],
    "CBD": [
        "Charlotte's Web", "ACDC", "Harlequin", "Cannatonic",
        "Sour Tsunami", "Ringo's Gift", "Canna-Tsu", "Harle-Tsu",
        "Sweet and Sour Widow", "Stephen Hawking Kush", "Pennywise",
        "Remedy", "Valentine X", "Elektra", "Special Sauce"
    ]
}
 
# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Unbounded:wght@400;700;900&display=swap');
 
:root {
    --green: #3ddc84;
    --dark-green: #1a5c38;
    --bg: #0d1a12;
    --card: #111f16;
    --border: #1e3a26;
    --text: #e8f5ec;
    --muted: #6b9e7e;
}
 
html, body, [class*="css"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Space Mono', monospace !important;
}
 
.main { background-color: var(--bg) !important; }
 
.stApp {
    background: radial-gradient(ellipse at top left, #0d2e1a 0%, #0d1a12 60%) !important;
}
 
h1, h2, h3 {
    font-family: 'Unbounded', sans-serif !important;
    color: var(--green) !important;
}
 
.big-title {
    font-family: 'Unbounded', sans-serif;
    font-size: 3.5rem;
    font-weight: 900;
    color: var(--green);
    letter-spacing: -2px;
    line-height: 1;
    margin-bottom: 0;
}
 
.tagline {
    color: var(--muted);
    font-size: 0.85rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 6px;
    margin-bottom: 30px;
}
 
.stat-box {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 24px;
    text-align: center;
}
 
.stat-number {
    font-family: 'Unbounded', sans-serif;
    font-size: 2.8rem;
    font-weight: 900;
    color: var(--green);
    line-height: 1;
}
 
.stat-label {
    color: var(--muted);
    font-size: 0.7rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 6px;
}
 
.category-header {
    font-family: 'Unbounded', sans-serif;
    font-size: 0.75rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--green);
    border-bottom: 1px solid var(--border);
    padding-bottom: 10px;
    margin-bottom: 16px;
    margin-top: 32px;
}
 
.strain-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 8px;
    transition: all 0.2s;
}
 
.strain-card:hover {
    border-color: var(--green);
}
 
.strain-tried {
    border-color: var(--dark-green);
    background: #0d2e1a;
}
 
.progress-bar-bg {
    background: var(--border);
    border-radius: 99px;
    height: 6px;
    width: 100%;
    margin-top: 8px;
}
 
.progress-bar-fill {
    background: var(--green);
    border-radius: 99px;
    height: 6px;
    transition: width 0.4s ease;
}
 
.badge {
    background: var(--dark-green);
    color: var(--green);
    font-size: 0.65rem;
    letter-spacing: 1px;
    padding: 2px 8px;
    border-radius: 99px;
    text-transform: uppercase;
    font-weight: 700;
}
 
.search-note {
    color: var(--muted);
    font-size: 0.75rem;
    margin-top: -12px;
    margin-bottom: 20px;
}
 
div[data-testid="stCheckbox"] label {
    color: var(--text) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.85rem !important;
}
 
div[data-testid="stTextInput"] input {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
    font-family: 'Space Mono', monospace !important;
}
 
div[data-testid="stSelectbox"] > div {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
}
 
.stButton button {
    background: var(--dark-green) !important;
    color: var(--green) !important;
    border: 1px solid var(--green) !important;
    border-radius: 8px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}
 
.stButton button:hover {
    background: var(--green) !important;
    color: var(--bg) !important;
}
 
section[data-testid="stSidebar"] {
    background: var(--card) !important;
    border-right: 1px solid var(--border) !important;
}
 
</style>
""", unsafe_allow_html=True)
 
# --- Session State ---
if "tried" not in st.session_state:
    st.session_state.tried = set()
 
# --- Header ---
st.markdown('<div class="big-title">🌿 GreenLog</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Track every strain you\'ve explored</div>', unsafe_allow_html=True)
 
# --- Stats ---
total_strains = sum(len(v) for v in STRAINS.values())
tried_count = len(st.session_state.tried)
pct = int((tried_count / total_strains) * 100) if total_strains > 0 else 0
 
col1, col2, col3, col4 = st.columns(4)
 
with col1:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{tried_count}</div>
        <div class="stat-label">Strains Tried</div>
    </div>""", unsafe_allow_html=True)
 
with col2:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{total_strains - tried_count}</div>
        <div class="stat-label">Left to Try</div>
    </div>""", unsafe_allow_html=True)
 
with col3:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{pct}%</div>
        <div class="stat-label">Complete</div>
    </div>""", unsafe_allow_html=True)
 
with col4:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{total_strains}</div>
        <div class="stat-label">Total Strains</div>
    </div>""", unsafe_allow_html=True)
 
# Progress bar
st.markdown(f"""
<div style="margin: 24px 0 32px 0;">
    <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
        <span style="color:var(--muted);font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;">Overall Progress</span>
        <span style="color:var(--green);font-size:0.7rem;">{pct}%</span>
    </div>
    <div class="progress-bar-bg">
        <div class="progress-bar-fill" style="width:{pct}%"></div>
    </div>
</div>
""", unsafe_allow_html=True)
 
# --- Sidebar Filters ---
with st.sidebar:
    st.markdown('<h3 style="margin-top:0">Filters</h3>', unsafe_allow_html=True)
 
    search = st.text_input("🔍 Search strains", placeholder="e.g. OG Kush...")
 
    category_filter = st.selectbox(
        "Category",
        ["All", "Indica", "Sativa", "Hybrid", "CBD"]
    )
 
    show_filter = st.selectbox(
        "Show",
        ["All Strains", "Tried Only", "Not Tried Yet"]
    )
 
    st.markdown("---")
    if st.button("Reset All"):
        st.session_state.tried = set()
        st.rerun()
 
    st.markdown(f"""
    <div style="margin-top:24px">
        <div class="stat-label" style="margin-bottom:12px">By Category</div>
    """, unsafe_allow_html=True)
 
    for cat, strains in STRAINS.items():
        cat_tried = len([s for s in strains if s in st.session_state.tried])
        cat_pct = int((cat_tried / len(strains)) * 100)
        st.markdown(f"""
        <div style="margin-bottom:14px">
            <div style="display:flex;justify-content:space-between;margin-bottom:4px">
                <span style="font-size:0.72rem;color:var(--text)">{cat}</span>
                <span style="font-size:0.72rem;color:var(--muted)">{cat_tried}/{len(strains)}</span>
            </div>
            <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="width:{cat_pct}%"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
 
    st.markdown("</div>", unsafe_allow_html=True)
 
# --- Strain List ---
categories_to_show = [category_filter] if category_filter != "All" else list(STRAINS.keys())
 
for category in categories_to_show:
    strains = STRAINS[category]
 
    # Apply search
    if search:
        strains = [s for s in strains if search.lower() in s.lower()]
 
    # Apply tried filter
    if show_filter == "Tried Only":
        strains = [s for s in strains if s in st.session_state.tried]
    elif show_filter == "Not Tried Yet":
        strains = [s for s in strains if s not in st.session_state.tried]
 
    if not strains:
        continue
 
    cat_tried = len([s for s in STRAINS[category] if s in st.session_state.tried])
    st.markdown(f"""
    <div class="category-header">
        {category} &nbsp;·&nbsp; {cat_tried}/{len(STRAINS[category])} tried
    </div>
    """, unsafe_allow_html=True)
 
    cols = st.columns(3)
    for i, strain in enumerate(strains):
        with cols[i % 3]:
            tried = strain in st.session_state.tried
            checked = st.checkbox(
                f"{'✅ ' if tried else ''}{strain}",
                value=tried,
                key=f"strain_{strain}"
            )
            if checked and strain not in st.session_state.tried:
                st.session_state.tried.add(strain)
                st.rerun()
            elif not checked and strain in st.session_state.tried:
                st.session_state.tried.discard(strain)
                st.rerun()
 
# --- Empty state ---
if all(
    len([s for s in strains
         if (not search or search.lower() in s.lower()) and
            (show_filter != "Tried Only" or s in st.session_state.tried) and
            (show_filter != "Not Tried Yet" or s not in st.session_state.tried)
         ]) == 0
    for strains in STRAINS.values()
):
    st.markdown("""
    <div style="text-align:center;padding:60px 0;color:var(--muted)">
        <div style="font-size:2rem;margin-bottom:12px">🔍</div>
        <div style="font-family:'Unbounded',sans-serif;font-size:0.9rem">No strains found</div>
        <div style="font-size:0.75rem;margin-top:8px">Try adjusting your filters</div>
    </div>
    """, unsafe_allow_html=True)
