import streamlit as st

# Atur halaman
st.set_page_config(page_title="Aplikasi IR Spektrum", page_icon="🌈")

# Sidebar navigasi
menu = st.sidebar.selectbox(
    "📂 Navigasi",
    ["🏠 Beranda", "📖 Teori IR", "🛠 Petunjuk Penggunaan", "🎯 Tujuan Aplikasi", "🔍 Identifikasi IR", "👨‍💻 Pembuat Aplikasi"]
)

# Header umum
st.title("🌈 Interpretasi Spektrum IR")
st.write("Aplikasi untuk membantu identifikasi gugus fungsi berdasarkan spektrum inframerah (IR).")

# Halaman Beranda
if menu == "🏠 Beranda":
    st.markdown("""
    <div style='text-align: center;'>
        <h2>👋 Selamat Datang di Aplikasi Spektrum IR!</h2>
        <p style='font-size:18px;'>Temukan gugus fungsi dari spektrum Infra Red dengan mudah dan cepat.</p>
       
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("🎓 Aplikasi ini cocok digunakan oleh:")
    st.markdown("""
    - Mahasiswa kimia atau farmasi  
    - Praktikan di laboratorium  
    - Pengajar yang ingin memberikan alat bantu ajar  
    - Peneliti atau analis spektrum senyawa organik
    """)
    st.success("📌 Silakan pilih menu di sidebar kiri untuk mulai menggunakan aplikasi.")

# Halaman Teori IR
elif menu == "📖 Teori IR":
    st.markdown("## 🧪 Teori Dasar Spektroskopi Inframerah (IR)")
    st.markdown("""
Spektroskopi Inframerah (IR) adalah teknik untuk mengidentifikasi gugus fungsi dalam senyawa kimia berdasarkan interaksi antara cahaya inframerah dan molekul. Jenis analisis ini dapat digunakan untuk mengarakterisasi sampel dalam bentuk cairan, larutan, pasta, bubuk, film, serat, dan gas. Analisis ini juga memungkinkan untuk menganalisis material di permukaan substrat.

### 🔬 Prinsip Dasar
Ketika molekul menyerap sinar inframerah, energi tersebut menyebabkan ikatan antar atom bergetar. Jenis getaran ini dapat berupa:
- *Regangan (stretching)*: perubahan panjang ikatan  
- *Tekukan (bending)*: perubahan sudut ikatan  
Sampel akan dikenai radiasi inframerah (IR). Radiasi IR ini kemudian memengaruhi getaran atom dari molekul dalam sampel, menghasilkan penyerapan dan/atau transmisi energi yang spesifik.
### 📏 Bilangan Gelombang (cm⁻¹)
Setiap gugus fungsi menyerap energi IR pada rentang bilangan gelombang tertentu.

### 📌 Contoh Pita Serapan Umum
| Bilangan Gelombang | Gugus Fungsi         | Keterangan                        |
|--------------------|----------------------|-----------------------------------|
| ~1700 cm⁻¹         | C=O                  | Karbonil (keton, aldehid, ester) |
| >3200 cm⁻¹         | O–H (lebar)          | Alkohol, Asam karboksilat        |
| ~2250 cm⁻¹         | C≡N atau C≡C         | Nitril atau Alkuna               |
| 1600–1500 cm⁻¹     | C=C aromatik         | Senyawa aromatik                 |
| ~3300 cm⁻¹         | N–H atau ≡C–H        | Amina, Asetilenik                |

### 🎯 Fungsi Spektroskopi IR
- Mengidentifikasi struktur senyawa organik/anorganik  
- Menentukan gugus fungsi spesifik  
- Mendukung analisis kualitatif dalam bidang kimia, farmasi, lingkungan  
""", unsafe_allow_html=True)

# Halaman Petunjuk Penggunaan
elif menu == "🛠 Petunjuk Penggunaan":
    st.markdown("## 🛠 Petunjuk Penggunaan")
    st.markdown("""
1. Siapkan data spektrum IR Anda (misalnya hasil FTIR).  
2. Perhatikan puncak-puncak utama dan nilai bilangan gelombangnya (dalam cm⁻¹).  
3. Bandingkan dengan tabel referensi atau gunakan fitur identifikasi otomatis jika tersedia.  
4. Cocokkan dengan kemungkinan gugus fungsi.  
""")

# Halaman Tujuan Aplikasi
elif menu == "🎯 Tujuan Aplikasi":
    st.markdown("## 🎯 Tujuan Aplikasi")
    st.markdown("""
- Membantu mahasiswa dalam menginterpretasi spektrum IR  
- Menjadi media pembelajaran interaktif dalam kimia organik  
- Mempermudah identifikasi gugus fungsi dari data eksperimen  
""")

# Halaman Identifikasi IR
elif menu == "🔍 Identifikasi IR":
    st.subheader("🔍 Identifikasi Gugus Fungsi Berdasarkan Spektrum IR")
    st.markdown("""
Masukkan satu atau dua nilai panjang gelombang IR (cm⁻¹) untuk mengidentifikasi kemungkinan gugus fungsi.  
Gunakan dua input jika ingin mendeteksi gugus kompleks seperti asam karboksilat.
""")

    nilai1 = st.number_input("Bilangan gelombang Infra Red pertama (cm⁻¹)", min_value=650, max_value=3700, step=1)
    nilai2 = st.number_input("Bilangan gelombang Infra Red kedua (opsional)", min_value=0, max_value=3700, step=1)

    # --- Data Gugus Fungsi (untuk tampilan) ---
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
    
]

# --- Data Gugus Fungsi (untuk logika) ---
gugus_fungsi_logika = [
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
if st.button("Identifikasi"):
    hasil = []

    # Deteksi asam karboksilat
    if (
        (1820 >= nilai1 >= 1660 and 3400 >= nilai2 >= 2400) or
        (1820 >= nilai2 >= 1660 and 3400 >= nilai1 >= 2400)
    ):
        hasil.append("🔴 Kemungkinan besar: Asam Karboksilat (–COOH)")

    # Pencocokan gugus fungsi
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

   
           
                
        

# Halaman Pembuat Aplikasi
elif menu == "👨‍💻 Pembuat Aplikasi":
    st.markdown("## 👨‍💻 Tentang Pembuat Aplikasi")
    st.markdown("""
Aplikasi ini dibuat oleh:

- *Annisa Balqis*  
- *Fachria*  
- *Marsya Putri*  
- *Nasywa*  
- *Silmi*

📍 *Institusi*: Politeknik AKA Bogor  
🎯 *Tujuan: Mendukung kegiatan praktikum dan tugas akhir pada mata kuliah **Kimia Instrumental* dengan bantuan aplikasi berbasis Python dan Streamlit.
""")
