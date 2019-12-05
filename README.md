# Космические Инстаграм и Imgur
__Автоматическая публикация фотографий от SpaceX и Hubble в Instagram и Imgur__

Код выполняет четыре задачи:
1) Скачивает фотографии последнего запуска SpaceX;
2) Скачивает фотографии заданной коллекции Hubble;
3) Обрезает фотографии под формат Instagram и публикует их в заданном Instagram-аккаунте;
4) Публикует фотографии в исходном виде в заданном Imgur-аккаунте.

Код разделён на 4 раздельных скрипта в разных файлах: `fetch_spacex.py`, `fetch_hubble.py`, `instagram_publish_images.py` и `imgur_publish_images.py`.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Для работы программы необходимо прописать логин и пароль от Instagram-аккаунта в файле `.env` (`INSTAGRAM_LOGIN` и `INSTAGRAM_PASSWORD`) и `IMGUR_CLIENT_ID`, `IMGUR_CLIENT_SECRET`, `IMGUR_ACCESS_TOKEN`, `IMGUR_REFRESH_TOKEN` от Imgur-аккаунта

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
