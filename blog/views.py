from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        "articles": [
            {
                "title": "نتیجه باورنکردنی و عجیب در والیبال؛ ۲۵-۳!",
                "description": "تیم‌ملی والیبال ترکیه در یک ست با نتیجه ٢۵-٣ ازبکستان را شکست داد.",
                "img": "https://news-cdn.varzesh3.com/pictures/2022/08/01/B/zp1vsekn.jpg?w=315"
            },
            {
                "title": "داماش گیلان؛ یک قدم تا صعود به لیگ 2",
                "description": "داماش گیلان با مربیگری بهزاد داداش زاده در آستانه صعود به لیگ 2 قرار دارد.",
                "img": "https://static.farakav.com/files/pictures/01689977.jpg?w=315"
            },
            {
                "title": "سوپرجام اروپا؛ ما رئالیم و به این آلمانی‌ها نمی‌بازیم!",
                "description": "رئال مادرید در حالی قدم به بازی برابر آینتراخت فرانکفورت می‌گذارد که به دنبال حفظ آمار درخشانش در دیدار برابر رقبای آلمانی است.",
                "img": "https://news-cdn.varzesh3.com/pictures/2022/06/07/C/pc1qfdod.jpg?w=315"
            }
        ]
    }
    return render(request, "blog/home.html", context)
