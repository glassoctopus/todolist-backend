from django.contrib import admin
from django.urls import path, include
from tasks.views.auth import register_user, check_user
from rest_framework import routers
from tasks.views.users import UserView
from tasks.todo_view import TodoView
from tasks.views.characters import CharacterView
from tasks.views.skills import SkillView
from tasks.views.archetypes import ArchetypeView
from tasks.views.equipments import EquipmentView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'todos', TodoView, 'todo')
router.register(r'heros', CharacterView, 'hero')
router.register(r'skills', SkillView, 'skill')
router.register(r'archetypes', ArchetypeView, 'archetype')
router.register(r'equipments', EquipmentView, 'equipment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkuser', check_user, name='checkuser'),
    path('register', register_user),
    path('', include(router.urls)),
]
