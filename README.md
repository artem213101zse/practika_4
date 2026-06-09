# Практическая работа №4: CI/CD с Docker и GitHub Actions

Полноценный CI/CD пайплайн: тесты → сборка Docker-образа → публикация в Docker Hub.

## Структура проекта

```
ci_docker_project/
├── app.py
├── requirements.txt
├── Dockerfile
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

## Что делает Workflow

1. **Job `test`** — запускает unit-тесты при каждом push и pull request
2. **Job `build-and-push`** — собирает Docker-образ и отправляет в Docker Hub (только при push в `main`)


## Как запустить локально (для проверки)

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск тестов
pytest -v

# Сборка Docker-образа
docker build -t ci-docker-app .

# Запуск контейнера
docker run -d -p 5000:5000 ci-docker-app
```

Открой http://localhost:5000
