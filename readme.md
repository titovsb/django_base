## Список внесенных изменений
#### 18.01.2022 (commit Lesson06)
- authapp/templates: userlist.html, regupdate.html, verification.html
- authapp.forms: DebiUserCreationForm.save()
- authapp.models: поле email переписали уникальным. добавлен activation_key, expiration_date
- authapp.urls: задействован re_path
- authapp.views: registration(), userlist(), send_veriry_mail() + verify()
- Добавлено подтверждение регистрации по коду активации
- Подключен filebase backend для send_mail()
#### 09.02.2022
- создано приложение adminapp
- в adminapp добавлены кнопки деактивировать и удалить
- в authapp созданы модели user и profile
