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
        <p style='font-size:18px;'>Temukan gugus fungsi dari spektrum IR dengan mudah dan cepat.</p>
        <img src='https://i.imgur.com/mg8OaRG.png' width='300'/>
    </div>
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
Spektroskopi Inframerah (IR) adalah teknik untuk mengidentifikasi gugus fungsi dalam senyawa kimia berdasarkan interaksi antara cahaya inframerah dan molekul.

### 🔬 Prinsip Dasar
Ketika molekul menyerap sinar inframerah, energi tersebut menyebabkan ikatan antar atom bergetar. Jenis getaran ini dapat berupa:
- *Regangan (stretching)*: perubahan panjang ikatan  
- *Tekukan (bending)*: perubahan sudut ikatan  

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

    nilai1 = st.number_input("Panjang gelombang IR pertama (cm⁻¹)", min_value=400, max_value=4000, step=1)
    nilai2 = st.number_input("Panjang gelombang IR kedua (opsional)", min_value=0, max_value=4000, step=1)

    gugus_fungsi = [
        {"rentang": (1820, 1660), "gugus": "C=O (Karbonil: Aldehid, Keton, Ester, Asam Karboksilat, Amida, Anhidrida)"},
        {"rentang": (3400, 2400), "gugus": "O–H (Asam Karboksilat) – sangat lebar"},
        {"rentang": (3600, 3300), "gugus": "O–H (Alkohol/Fenol)"},
        {"rentang": (3500, 3500), "gugus": "N–H (Amina/Amida)"},
        {"rentang": (2850, 2750), "gugus": "C–H (Aldehid) – dua pita lemah"},
        {"rentang": (1810, 1710), "gugus": "C=O (Anhidrida) – dua pita"},
        {"rentang": (1300, 1000), "gugus": "C–O (Ester, Alkohol, Eter, Asam Karboksilat)"},
        {"rentang": (1650, 1650), "gugus": "C=C (Alkena)"},
        {"rentang": (1650, 1450), "gugus": "C=C (Aromatik)"},
        {"rentang": (3000, 3000), "gugus": "C–H aromatik/vinil"},
        {"rentang": (3000, 3000), "gugus": "C–H alifatik"},
        {"rentang": (2250, 2250), "gugus": "C≡N (Nitril)"},
        {"rentang": (2150, 2150), "gugus": "C≡C (Alkuna)"},
        {"rentang": (3300, 3300), "gugus": "≡C–H (asetilenik)"},
        {"rentang": (1600, 1500), "gugus": "NO₂ – pita kuat"},
        {"rentang": (1390, 1300), "gugus": "NO₂ – pita tambahan"},
        {"rentang": (1450, 1450), "gugus": "C–H bending (CH₃, CH₂)"},
        {"rentang": (1375, 1375), "gugus": "C–H bending (CH₃, CH₂)"},
    ]

    if st.button("Identifikasi"):
        hasil = []

        if (
            (1820 >= nilai1 >= 1660 and 3400 >= nilai2 >= 2400) or
            (1820 >= nilai2 >= 1660 and 3400 >= nilai1 >= 2400)
        ):
            hasil.append("🔴 Kemungkinan besar: Asam Karboksilat (–COOH)")

        for nilai in [nilai1, nilai2]:
            if nilai == 0:
                continue
            cocok = False
            for item in gugus_fungsi:
                low, high = item["rentang"]
                if low >= nilai >= high or low <= nilai <= high:
                    hasil.append(f"✓ {nilai} cm⁻¹ → {item['gugus']}")
                    cocok = True
            if not cocok:
                hasil.append(f"✖ {nilai} cm⁻¹ → Tidak dikenali dalam daftar.")

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
