import streamlit as st

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="Spektrum IR", page_icon="🔬")

# --- Background Gambar ---
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1616593968993-c2208f86f485?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    [data-testid="stHeader"] {
        background: rgba(255, 255, 255, 0);
    }

    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.7);
    }

    .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Judul Utama ---
st.title("🔬 Interpretasi Spektrum IR Berdasarkan Panjang Gelombang")
st.markdown("""
Masukkan satu atau dua nilai bilangan gelombang IR (cm⁻¹) untuk mengidentifikasi kemungkinan gugus fungsi.
Gunakan dua input jika ingin mendeteksi gugus kompleks seperti asam karboksilat.
""")

# --- Input Pengguna ---
nilai1 = st.number_input("Panjang gelombang IR pertama (cm⁻¹)", min_value=400, max_value=4000, step=1)
nilai2 = st.number_input("Panjang gelombang IR kedua (opsional)", min_value=0, max_value=4000, step=1)

# --- Data Gugus Fungsi (untuk tampilan) ---
gugus_fungsi_display = [
    {"rentang": "3700–3584", "gugus": "O–H bebas - non-terikat H - alkohol"},
    {"rentang": "3550–3200", "gugus": "O–H terikat H - alkohol - asam karboksilat"},
    {"rentang": "3500–3300", "gugus": "N–H - amina - amida"},
    {"rentang": "3400–3250", "gugus": "≡C–H - alkuna terminal"},
    {"rentang": "3100–3000", "gugus": "C–H - sp² - alkena - aromatik"},
    {"rentang": "3000–2850", "gugus": "C–H - sp³ - alkana"},
    {"rentang": "2260–2220", "gugus": "C≡N - nitril"},
    {"rentang": "2150–2100", "gugus": "C≡C - alkuna"},
    {"rentang": "1870–1800", "gugus": "C=O - anhidrida asam"},
    {"rentang": "1750–1735", "gugus": "C=O - ester - asam karboksilat"},
    {"rentang": "1740–1720", "gugus": "C=O - aldehid - keton"},
    {"rentang": "1720–1680", "gugus": "C=O - umum - aldehid - keton - asam - ester - amida"},
    {"rentang": "1680–1600", "gugus": "C=C - alkena - aromatik"},
    {"rentang": "1600–1500", "gugus": "C=C - aromatik"},
    {"rentang": "1550–1510", "gugus": "N–O - NO₂ simetris"},
    {"rentang": "1370–1340", "gugus": "N–O - NO₂ asimetris"},
    {"rentang": "1450–1375", "gugus": "C–H bending - CH₃ - CH₂"},
    {"rentang": "1300–1000", "gugus": "C–O stretching - alkohol - ester - asam"},
    {"rentang": "1000–650",  "gugus": "C–H out-of-plane - aromatik"},
]

# --- Data Gugus Fungsi (untuk logika) ---
gugus_fungsi_numerik = [
    {"rentang": (3700, 3584), "gugus": "O–H bebas - non-terikat H - alkohol"},
    {"rentang": (3550, 3200), "gugus": "O–H terikat H - alkohol - asam karboksilat"},
    {"rentang": (3500, 3300), "gugus": "N–H - amina - amida"},
    {"rentang": (3400, 3250), "gugus": "≡C–H - alkuna terminal"},
    {"rentang": (3100, 3000), "gugus": "C–H - sp² - alkena - aromatik"},
    {"rentang": (3000, 2850), "gugus": "C–H - sp³ - alkana"},
    {"rentang": (2260, 2220), "gugus": "C≡N - nitril"},
    {"rentang": (2150, 2100), "gugus": "C≡C - alkuna"},
    {"rentang": (1870, 1800), "gugus": "C=O - anhidrida asam"},
    {"rentang": (1750, 1735), "gugus": "C=O - ester - asam karboksilat"},
    {"rentang": (1740, 1720), "gugus": "C=O - aldehid - keton"},
    {"rentang": (1720, 1680), "gugus": "C=O - umum - aldehid - keton - asam - ester - amida"},
    {"rentang": (1680, 1600), "gugus": "C=C - alkena - aromatik"},
    {"rentang": (1600, 1500), "gugus": "C=C - aromatik"},
    {"rentang": (1550, 1510), "gugus": "N–O - NO₂ simetris"},
    {"rentang": (1370, 1340), "gugus": "N–O - NO₂ asimetris"},
    {"rentang": (1450, 1375), "gugus": "C–H bending - CH₃ - CH₂"},
    {"rentang": (1300, 1000), "gugus": "C–O stretching - alkohol - ester - asam"},
    {"rentang": (1000, 650),  "gugus": "C–H out-of-plane - aromatik"},
]

# --- Identifikasi Gugus Fungsi ---
if st.button("🔍 Identifikasi"):
    hasil = []

    # Pengecekan kombinasi asam karboksilat
    if (
        (1820 >= nilai1 >= 1660 and 3550 >= nilai2 >= 3200) or
        (1820 >= nilai2 >= 1660 and 3550 >= nilai1 >= 3200)
    ):
        hasil.append("🔴 Kemungkinan besar: Asam Karboksilat (–COOH)")

    # Cek tiap nilai
    for nilai in [nilai1, nilai2]:
        if nilai == 0:
            continue
        cocok = False
        for item in gugus_fungsi_numerik:
            low, high = item["rentang"]
            if low >= nilai >= high or high >= nilai >= low:
                hasil.append(f"✓ {nilai} cm⁻¹ → {item['gugus']}")
                cocok = True
        if not cocok:
            hasil.append(f"✖ {nilai} cm⁻¹ → Tidak cocok dengan data referensi")

    # Tampilkan hasil
    if hasil:
        st.markdown("### Hasil Identifikasi:")
        for h in hasil:
            st.markdown(h)
    else:
        st.warning("Tidak ada nilai yang dikenali.")

# --- Tabel Referensi ---
with st.expander("📚 Lihat Daftar Referensi Gugus Fungsi IR"):
    for item in gugus_fungsi_display:
        st.markdown(f"- *{item['rentang']} cm⁻¹* → {item['gugus']}")
