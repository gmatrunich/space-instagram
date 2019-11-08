# Космический Инстаграм
__Автоматическая публикация фотографий от SpaceX и Hubble в Instagram__

Код выполняет три задачи:
1) Скачивает фотографии последнего запуска SpaceX;
2) Скачивает фотографии заданной коллекции Hubble;
3) Обрезает фотографии под формат Instagram и публикует их в заданном Instagram-аккаунте.

Код разделён на 3 раздельных скрипта в разных файлах: `fetch_spacex.py`, `fetch_hubble.py` и `publish_images.py`.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Для работы программы необходимо прописать логин и пароль от Instagram-аккаунта в файле `.env` (`INSTAGRAM_LOGIN` и `INSTAGRAM_PASSWORD`)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
