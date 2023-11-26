import streamlit as st
import PIL

def app():
    st.title("WELLCOME🖐")
    st.title("Aplikasi Prediksi Klasifikasi Tinggi Rendah Daging Unggas🐔")
    
    with st.container():
        processor, title_text, artificial = st.columns([1,3,1])

        # st.markdown("""
        #     <h1 class="title" style='text-align: center;'>Welcome to Our Blog!</h1>
        #     <br><br>
        # """, unsafe_allow_html=True)


    blog1, blog2, blog3, blog4 = st.tabs(["What is Poultry? ", "high production scale", "What is klasifikasi?", "classification with decision tree!"])

    with blog1:
        st.markdown("""
            <h1 class="title" style='text-align: center;'>📝 Blog 1</h1>
            <div class="des-title" style='text-align: center;'>This is a blog post about Poultry</div>
            <br><br>
        """, unsafe_allow_html=True)

        st.image("img/poultry.jpg")

        # st.markdown(unsafe_allow_html=True)

        st.markdown("""
        ## What is Poultry?
        Daging unggas merujuk pada daging yang berasal dari hewan unggas, terutama burung seperti ayam, bebek, kalkun, dan burung puyuh. Daging unggas sering menjadi bagian penting dari diet manusia di berbagai belahan dunia.
        \n\n
        Daging unggas umumnya diketahui memiliki nilai gizi yang tinggi, rendah lemak (khususnya daging tanpa kulit), kandungan protein yang baik, serta kaya akan vitamin dan mineral. Daging unggas juga dapat disajikan dalam berbagai cara, seperti dipanggang, digoreng, direbus, atau ditumis, sesuai dengan preferensi pribadi dan kebiasaan kuliner masyarakat setempat.
        
        """)

    with blog2:
        st.markdown("""
            <h1 class="title" style='text-align: center;'>📝 Blog 2</h1>
            <div class="des-title" style='text-align: center;'>This is a blog post about high production scale, low poultry meat in East Java</div>
            <br><br>
        """, unsafe_allow_html=True)

        st.image("img/grafik.jpg")

        st.markdown("""
        ## high production scale, low poultry meat in East Java!
        Skala produksi daging unggas di Jawa Timur, seperti di wilayah lainnya, dapat bervariasi antara tinggi dan rendah tergantung pada beberapa faktor seperti permintaan pasar, infrastruktur peternakan, teknologi, dan faktor-faktor lingkungan lainnya. Meskipun tidak ada data terkini yang saya miliki setelah September 2021, Jawa Timur merupakan salah satu provinsi di Indonesia dengan tingkat produksi daging unggas yang signifikan.

        Jawa Timur memiliki banyak peternakan ayam komersial, peternakan bebek, serta beberapa peternakan kalkun dan burung puyuh yang beroperasi di berbagai skala produksi. Beberapa wilayah di Jawa Timur, seperti Kabupaten Mojokerto, Kabupaten Nganjuk, Kabupaten Jombang, dan Kabupaten Lamongan, dikenal sebagai pusat produksi daging unggas yang cukup signifikan.
        \n\n
        Skala produksi tinggi daging unggas di Jawa Timur biasanya melibatkan peternakan modern dengan teknologi canggih, penggunaan pakan komersial yang baik, manajemen kesehatan unggas yang optimal, dan kapasitas produksi yang besar. Biasanya, peternakan skala besar ini menghasilkan daging unggas dalam jumlah yang cukup besar untuk memenuhi permintaan pasar lokal maupun ekspor.

        Di sisi lain, skala produksi rendah daging unggas di Jawa Timur biasanya melibatkan peternakan skala kecil hingga menengah, yang mungkin memiliki jumlah unggas yang lebih sedikit dan menggunakan metode tradisional dalam operasionalnya. Peternakan skala kecil ini mungkin melayani pasar lokal di sekitar wilayah tersebut.
        \n\n
        Namun, penting untuk dicatat bahwa informasi ini mungkin tidak mencerminkan situasi terkini karena skala produksi daging unggas dapat berubah seiring waktu. Jika Anda membutuhkan data terbaru atau informasi yang lebih rinci mengenai skala produksi daging unggas di Jawa Timur, disarankan untuk menghubungi instansi pemerintah terkait, seperti Dinas Pertanian atau Badan Pusat Statistik (BPS), yang dapat memberikan informasi yang lebih akurat dan terkini.
        

        """)
    with blog3:
        st.markdown("""
            <h1 class="title" style='text-align: center;'>📝 Blog 3</h1>
            <div class="des-title" style='text-align: center;'>This is a blog post about Klasifikasi</div>
            <br><br>
        """, unsafe_allow_html=True)

        st.image("img/klasifikasi.jpg")

        st.markdown("""
        ## What is klasifikasi?
        Klasifikasi merujuk pada proses pengelompokkan objek atau data ke dalam kategori atau kelas yang berbeda berdasarkan atribut-atribut yang dimiliki. Tujuan utama dari klasifikasi adalah untuk mempelajari pola-pola atau hubungan di antara data dan kemudian mengeneralisasi pola tersebut untuk mengklasifikasikan data yang baru atau belum diketahui ke dalam kelas yang sesuai.

        Dalam konteks data dan pembelajaran mesin, klasifikasi adalah salah satu tugas yang umum dilakukan. Ini melibatkan penggunaan algoritma pembelajaran mesin untuk mempelajari pola-pola dari data latihan yang diketahui kelasnya dan kemudian menghasilkan model klasifikasi yang dapat digunakan untuk memprediksi kelas atau label dari data baru.
        \n\n
        Proses klasifikasi melibatkan beberapa tahapan, antara lain:

        Pemilihan atribut: Memilih atribut-atribut yang relevan atau penting dari data yang akan digunakan sebagai fitur untuk melakukan klasifikasi.

        Pembuatan model: Menggunakan algoritma pembelajaran mesin untuk mempelajari pola-pola dari data latihan dan membuat model klasifikasi. Beberapa algoritma klasifikasi populer termasuk Naive Bayes, Decision Tree, Random Forest, Support Vector Machines (SVM), dan Neural Networks.

        Pelatihan model: Memasukkan data latihan ke dalam model klasifikasi untuk melatih model agar dapat mengenali pola dan menghubungkannya dengan kelas yang sesuai.

        Evaluasi model: Mengukur kinerja model klasifikasi dengan menggunakan data pengujian yang belum diketahui untuk mengevaluasi sejauh mana model dapat mengklasifikasikan dengan benar.

        Penggunaan model: Setelah model dianggap memadai, itu dapat digunakan untuk melakukan prediksi pada data yang baru atau belum diketahui dengan memberikan atribut dan mendapatkan keluaran kelas yang dihasilkan oleh model.
        \n\n
        Dalam pembelajaran mesin, klasifikasi merupakan salah satu topik yang penting dan digunakan dalam berbagai aplikasi yang melibatkan analisis data, pengenalan pola, dan pengambilan keputusan.
        """)

    with blog4:
        st.markdown("""
            <h1 class="title" style='text-align: center;'>📝 Blog 4</h1>
            <div class="des-title" style='text-align: center;'>This is a blog post about classification with decision tree</div>
            <br><br>
        """, unsafe_allow_html=True)

        st.image("img/tree.jpg")

        st.markdown("""
        ## Classification With Decision Tree
        Klasifikasi dengan decision tree (pohon keputusan) adalah salah satu metode populer dalam pembelajaran mesin untuk melakukan klasifikasi. Decision tree adalah representasi visual dari serangkaian keputusan atau aturan yang menghasilkan prediksi kelas atau label untuk data yang baru.
        \n\n
        Decision tree memiliki kelebihan dalam kemampuan interpretasi yang baik, mudah dimengerti, dan dapat menangani data yang tidak terstruktur dengan baik. Namun, kelemahannya termasuk kecenderungan overfitting jika tidak diatur dengan baik dan sensitivitas terhadap perubahan kecil dalam data latihan.

        Pustaka Python seperti scikit-learn menyediakan implementasi decision tree yang dapat digunakan dengan mudah untuk melakukan klasifikasi. Dengan menggunakan pustaka tersebut, Anda dapat membuat decision tree, melatihnya, dan menggunakannya untuk melakukan prediksi pada data baru.
        \n\n


        """)