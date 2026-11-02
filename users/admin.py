from django.contrib import admin
from users.models import User

# -28- Регистрируем кастомного пользователя в админке,используем базовый ModelAdmin вместо UserAdmin
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    # -28- Выводим список пользователей по email и статусам
    list_display = ('email', 'is_staff', 'is_active')
    # -28- Поля, которые можно будет редактировать внутри карточки пользователя (включая группы)
    fields = ('email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
    # -28- Настраиваем горизонтальный фильтр для удобного выбора групп
    filter_horizontal = ('groups', 'user_permissions')


# ------28работает корректировка-----
#
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from users.models import User  # -28- Импортируем кастомную модель из приложения users
#
# # -28- Регистрируем кастомного пользователя в админке, используя стандартный или расширенный класс управления
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     # -28- Настройка отображения списка пользователей (подставьте поля, если авторизация по email)
#     list_display = ('email', 'is_staff', 'is_active')
#     ordering = ('email',)