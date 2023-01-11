## Проект touch_MPTT

Создание базы данных сотрудников, а также структуру организации.<br>
Для реализации использовал иерархическую древовидную структуру.

### Стек технологий

![python version](https://img.shields.io/badge/Python-3.9-yellowgreen)
![python version](https://img.shields.io/badge/Django-4.1.5-yellowgreen)
![python version](https://img.shields.io/badge/djangorestframework-3.14.0-yellowgreen)
![python version](https://img.shields.io/badge/django--mptt-0.14.0-yellowgreen)

### Как запустить проект

Клонировать репозиторий и перейти в репозиторий с файлом manage.py:

```
git clone https://github.com/DamirShamsutdinov/touch_MPTT.git
cd touch_MPTT/companies
```

Перед запуском программы не забываем установить виртуальное окружение и
зависимости

```
WIN: python -m venv venv
MAC: python3 -m venv venv

WIN: source venv/scripts/activate
MAC: source venv/bin/activate

WIN: python -m pip install --upgrade pip
MAC: python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

P.S.:
<br>Celery делать не стал т.к. уже усвоил данный инструмент на другом проекте.
<br>А для меня это лишь учебный проект.

### Пример того что должно получиться

![screenshot](https://github.com/DamirShamsutdinov/touch_MPTT/blob/main/1.jpg)<br><br>
![screenshot](https://github.com/DamirShamsutdinov/touch_MPTT/blob/main/3.jpg)<br><br>
