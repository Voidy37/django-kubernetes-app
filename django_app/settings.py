import os
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.postgresql',
 'NAME': os.getenv('DB_NAME', 'myapp'),
 'USER': os.getenv('DB_USER', 'postgres'),
 'PASSWORD': os.getenv('DB_PASSWORD', ''),
 'HOST': os.getenv('DB_HOST', 'localhost'),
 'PORT': os.getenv('DB_PORT', '5432'),
 }
}
# Для демонстрации балансировки - выводим hostname pod'а
import socket
def get_hostname():
 return socket.gethostname()
# Добавить в контекст шаблонов или создать middleware
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                # Добавляем наш кастомный контекст-процессор
                'django_app.settings.pod_info_context',
            ],
        },
    },
]

# Дополнительные настройки
ALLOWED_HOSTS = ['*']
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
