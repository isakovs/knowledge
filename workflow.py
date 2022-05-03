"""Создать Workflow:"""
# создать директорию .github/workflows с шаблоном main.yml (workflow файл).
# Можно создать на GitHub.
# Любой workflow должен содержать, как минимум три ключа:
# name — имя;
# on — ивент, событие-триггер, после которого сработает workflow;
# jobs — список действий, которые выполняются после срабатывания события on.

"""Определить последовательность выполнения задач"""
# .github/workflows/main.yml

# Тут ваши задачи тестирования и сборки образа
# ...
# Сразу после них добавьте новую задачу: деплой приложения
build_and_push_to_docker_hub:
    name: Push Docker image to Docker Hub
    runs-on: ubuntu-latest
    needs: tests
    steps:
      - name: Check out the repo
        # Проверка доступности репозитория Docker Hub для workflow
        uses: actions/checkout@v2 
      - name: Set up Docker Buildx
        # Вызов сборщика контейнеров docker
        uses: docker/setup-buildx-action@v1 
      - name: Login to Docker 
        # Запуск скрипта авторизации на Docker Hub
        uses: docker/login-action@v1 
        with:
          username: <ваш_username_dockerhub> 
          password: <ваш_пароль_dockerhub>
      - name: Push to Docker Hub
        # Пуш образа в Docker Hub 
        uses: docker/build-push-action@v2 
        with:
          push: true
          tags: ваш-логин-на-docker-hub/ваш-репозиторий-на-docker-hub:latest


"""Хранить секретные переменные на GitHub"""
# в настройках репозитория раздлел sexrets.
# Создаем и обращаемся по шаблону:
${{ secrets.<ИМЯ_СЕКРЕТА> }} 