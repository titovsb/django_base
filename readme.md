## Список внесенных изменений
#### 13.02.2022 DJANGO2 - lesson3
1. +Создать выпадающее меню для ссылки на личный кабинет пользователя в меню.
2. Создать приложение для работы с заказами пользователя.
3. Создать контроллеры CRUD для заказа на базе Django CBV.
4. Реализовать обновление статуса заказа при совершении покупки.
5. Обновить контроллеры проекта – перевести на Django CBV.
6. *Организовать работу со статусом заказов в админке (имитация обработки заказа в магазине).

#### 12.02.2022
- выполнены полностью задания стартового курса DJANGO
#### 09.02.2022
- создано приложение adminapp
- в adminapp добавлены кнопки деактивировать и удалить
- в authapp созданы модели user и profile
#### 18.01.2022 (commit Lesson06)
- authapp/templates: userlist.html, regupdate.html, verification.html
- authapp.forms: DebiUserCreationForm.save()
- authapp.models: поле email переписали уникальным. добавлен activation_key, expiration_date
- authapp.urls: задействован re_path
- authapp.views: registration(), userlist(), send_veriry_mail() + verify()
- Добавлено подтверждение регистрации по коду активации
- Подключен filebase backend для send_mail()
