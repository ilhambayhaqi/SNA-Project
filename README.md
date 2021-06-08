# SNA-Project

Rafif Ridho - 05111840000058

Muhammad Ilham Bayhaqi - 0511184000069

## File Resource

Data twitter yang telah diambil diletakkan dalam folder _Resource_. Dengan ketentuan sebagai berikut.

- Untuk nama file awalan / prefix _before ..._ merupakan data tweet yang diambil pada rentang Batch-1. Untuk nama file berawalan _after ..._ tweet merupakan data yang diambil pada rentang Batch-2.

- Untuk kedalaman dari snowball sampling untuk tiap kedalaman di tulis dengan _[prefix]\_d[no]_ dengan no merupakan tingkat kedalamannya. Untuk depth 0 dinotasikan hanya _[prefix]_

- Untuk nama file berawalan _beforeInteraction ..._ merupakan data hasil interaksi yang terhadap setiap tweet yang ada pada file _before ..._ dengan depth yang sama. Begitu pula dengan yang after

- Untuk snowball ulang pada akun "@dr*koko28" memiliki prefix \_before_koko*

## Urutan pengambilan

## Before

_before_ -> _beforeInteraction_

_before_d1_ -> _beforeInteraction_d1_

_before_d2_ -> _beforeInteraction_d2_

## After

_after_ -> _afterInteraction_

_after_d1_ -> _afterInteraction_d1_

_after_d2_ -> _afterInteraction_d2_
