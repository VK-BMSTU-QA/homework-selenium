domen = "https://planexa.ru/"

cookie_name = "token"

default_password = "12345678"

authorization_data = {
    "login": "planexa",
    "password": "planexa",
    "wrong_login": "test123124",
    "wrong_password": "12876376943",
}

urls = {
    "base_url": domen + "base"
}

login_errors = {
    "empty_enter": "Логин и пароль должны составлять от 7 до 20 символов",
    "wrong_user": "Пожалуйста, проверьте правильность написания логина и пароля",
}

signup_errors = {
    "empty_enter": "Логин и пароль должны составлять от 7 до 20 символов",
    "already_exist": "Пользователь с таким именем уже зарегистрирован",
    "repeat_pass": "Введенные пароли не совпадают",
}

create_desc_errors = {
    "invalid_title": "Длина названия должна быть от 1 до 30 символов",
}
