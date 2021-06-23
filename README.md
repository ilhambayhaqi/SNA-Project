# SNA-Project

Rafif Ridho - 05111840000058

Muhammad Ilham Bayhaqi - 0511184000069

## Notebook

Terdapat 2 Jupyter Notebook yang ada pada project ini, sebagai berikut.

- *Twitter_Selenium.ipynb* - merupakan notebook yang digunakan untuk mengambil tweet menggunakan Twint dan mengambil interaksi like dan retweet menggunakan Selenium dan visualisasi serta analisi graph berupa directed graph pada jaringan sosial batch-1 dan batch-2.

- *Twitter_2Mode.ipynb* - merupakan notebook yang digunakan untuk melakukan visualisasi graph dan analisis tweet dengan menggunakan 2 mode node yaitu node akun dan node tweet dengan graph berupa undirected graph.

## Resourse Gambar

Gambar untuk jaringan yang terbentuk bisa diakses pada folder _Resource/image_ dengan nama prefix pada nama file sesuai gambar pada file laporan Word.

## Resource JSON

Data twitter yang telah diambil diletakkan dalam folder _Resource_. Dengan ketentuan sebagai berikut.

- Untuk nama file awalan / prefix _before..._ merupakan data tweet yang diambil pada rentang Batch-1. Untuk nama file berawalan _after..._ tweet merupakan data yang diambil pada rentang Batch-2.

- Untuk kedalaman dari snowball sampling untuk tiap kedalaman di tulis dengan _[prefix]\_d[no]_ dengan no merupakan tingkat kedalamannya. Untuk depth 0 dinotasikan hanya _[prefix]_

- Untuk nama file berawalan _beforeInteraction..._ merupakan data hasil interaksi yang terhadap setiap tweet yang ada pada file _before..._ dengan depth yang sama. Begitu pula dengan yang after

- Untuk snowball ulang pada akun "@dr_koko28" memiliki prefix *before_koko*


### Before

- _before_ -> _beforeInteraction_
- _before_d1_ -> _beforeInteraction_d1
- _before_d2_ -> _beforeInteraction_d2_

### After

- _after_ -> _afterInteraction_
- _after_d1_ -> _afterInteraction_d1_
- _after_d2_ -> _afterInteraction_d2_

## Resource CSV 

File Resource dalam bentuk csv diletakkan pada folder /Resource/csv/ yang merupakan file hasil konversi dari json ke csv. Ketentuan penamaan file juga mirip dengan ketentuan penamaan file pada file json.
