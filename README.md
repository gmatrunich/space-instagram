# Космические Инстаграм и Imgur
__Автоматическая публикация фотографий от SpaceX, Hubble и NASA в Instagram и Imgur__

Код выполняет пять задач:
1) Скачивает фотографии последнего запуска SpaceX;
2) Скачивает фотографии заданной коллекции Hubble;
3) Скачивает "фотографию дня" с сайта NASA за заданное количество дней; 
4) Обрезает фотографии под формат Instagram и публикует их в заданном Instagram-аккаунте;
5) Публикует фотографии в исходном виде в заданном Imgur-аккаунте.

Код разделён на 5 раздельных скрипта в разных файлах: `fetch_spacex.py`, `fetch_hubble.py`, `fetch_nasa.py`, `instagram_publish_images.py` и `imgur_publish_images.py`.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Для работы программы необходимо прописать логин и пароль от Instagram-аккаунта в файле `.env` (`INSTAGRAM_LOGIN` и `INSTAGRAM_PASSWORD`), `IMGUR_CLIENT_ID`, `IMGUR_CLIENT_SECRET`, `IMGUR_ACCESS_TOKEN`, `IMGUR_REFRESH_TOKEN` от Imgur-аккаунта и `NASA_API_KEY` от NASA-аккаунта.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
