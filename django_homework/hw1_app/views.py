import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

index_html = """
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Главная</title>
    </head>
    <body>
        <h1>Приветствую всех в нашем онлайн магазине!</h1>
        <ul>
            <li><a href="/">Главная</a></li>
            <li><a href="/about">О нас</a></li>
        </ul>
        <img src="https://st4.depositphotos.com/1001877/40565/i/380/depositphotos_405650078-stock-photo-car-parts-spares-accesoires-auto.jpg" alt="Наш магазин" style="width: 600px">
        <p>Это главна страница нашего интернет магазина, на ней Вы всегда сможете найти самую актуальную информацию по действующим акционным предложениям и скидкам. Будем рабы если вы найдете товар, который Вам очень понравится!</p>
  
    </body>
    </html>
"""

about_html = """
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>О нас</title>
    </head>
    <body>
        <h1>Информация о нас</h1>
        <ul>
            <li><a href="/">Главная</a></li>
            <li><a href="/about">О насt</a></li>
        </ul>
        <img src="https://st.depositphotos.com/1518767/2414/i/380/depositphotos_24149105-stock-photo-mechanic-reparing-car-while-consulting.jpg" alt="Наша команда" style="width: 600px">
        <p>Мы - сплоченная команда профессионалов, которая сможет предложить Вам первоклассный сервис. Узнайте о нас больше!</p>
       
    </body>
    </html>
"""


def index(request):
    logger.info('Главная страница загружена')
    return HttpResponse(index_html)


def about(request):
    logger.info('Страница "о нас" загружена')
    return HttpResponse(about_html)


# Create your views here.
