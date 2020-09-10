# Github API Task

Программа выводит  30 наиболее часто встречающихся слов в сообщениях к последним 100 коммитам в проекте Kotlin,
ветка master.

Замечания: 
- Слова в сообщениях разделены по знакам пунктуации и пробелам
- Весь текст приведен в нижний регистр
- Словами считаются только последовательности букв
- Чтобы удалить стоп-слова из выдачи, установите remove_stopwords в True
# Запуск
Требования для запуска: Python 3.8

```
0. Activate your virtual python environment (recommended) / use global interpreter
1. $ pip install -r requirements.txt
2. $ python main.py
```

Если возникли проблемы с библиотекой nltk, замените шаг 2:
```
2. $ python nltk_free_version.py
```