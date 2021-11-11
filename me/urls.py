from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("skills/", views.skills, name="skills"),
    path("education/", views.education, name="education"),
    path("project/", views.project, name="project"),
]
