Учебный проект API на DRF.

Установка nodejs:
1. Либо через менеджер приложений ubuntu software
2. Либо скачать архив с сайта и установить:
2.1 Разархивировать таром
2.2 sudo cp -r названиеархива/{bin,include,lib,share} /usr/

Создание проекта на react:
1. В корне проекта DJango написать ``npx create-react-app frontend`` (в папке с ``manage.py``)
2. Дальше все команды для реакта писать в папке frontend
3. Запуск тестового сервера реакта: npm run start

    #чтобы галочка ставилась, надо в сериалайзере прописать
    #active = serializers.BooleanField(initial=True)
    #чтобы сделать только для чтения 
    #active = serializers.BooleanField(read_only=True)
