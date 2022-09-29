Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

untuk memastikan request sesuai.
jika tidak, request tidak dieksekusi.

Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

bisa, dengan <form>

Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

ketika submit, data dicek validitasnya. jika valid, data disimpan di database. lalu diakses dengan .objects.filter() lalu dimasukkan ke context di view, lalu di render html.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.