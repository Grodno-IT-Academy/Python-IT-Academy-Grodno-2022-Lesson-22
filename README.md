# Планы:(может за день не успеем но вообще закончим к концу курса)
- Перейти на постгрес
- Добавить к нашему проекту докер-компоуз для девелопмента с отдельной базой!
- Добавить удаленную файловую систему
- Создать докер для запуска проекта на wsgi
- Запустить на сервере
- Обсудить поддержку и развитие приложения после запуска!

# Теперь для запуска проекта на компьютере достаточто лишь 

```shell
docker compose up
docker compose -f docker-compose-deploy.yml up --build
```
Чтобы отдавать команды нашей среде мы делае следующее:

```shell
docker compose exec app python manage.py migrate
```