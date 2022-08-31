from django.shortcuts import render

kategori_liste = ["macera", "romantik", "dram", "bilimkurgu"]
film_liste = [
    {
        "film_adi": "film1",
        "aciklama": "film1 açıklama",
        "resim" : "1.jpeg",
        "anasayfa": True
    },
    {
        "film_adi": "film2",
        "aciklama": "film2 açıklama",
        "resim" : "2.jpeg",
        "anasayfa": True
    },
    {
        "film_adi": "film3",
        "aciklama": "film3 açıklama",
        "resim" : "3.jpeg",
        "anasayfa": False
    },
    {
        "film_adi": "film4",
        "aciklama": "film4 açıklama",
        "resim" : "4.jpeg",
        "anasayfa": False
    }
]
def home(request):
    data = {
        "kategoriler": kategori_liste,
        "filmler": film_liste
    }
    return render(request, "index.html", data)
def movies(request):
    data = {
        "kategoriler": kategori_liste,
        "filmler": film_liste
    }
    return render(request, "movies.html", data)