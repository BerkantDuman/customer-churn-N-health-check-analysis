from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    path('api/people', views.PersonView.as_view({"get": "list_all"})),
    path('api/people/<int:id>',
         views.PersonView.as_view({"get": "get_by_id"})),
    path('api/people/login', views.PersonView.as_view({"post": "login"})),
    path('api/values', views.ValueView.as_view({"get": "list_all"})),
    path('api/values/<int:id>', views.ValueView.as_view({"get": "get_by_id"})),
    path('api/values/person/<int:person_id>',
         views.ValueView.as_view({"get": "get_by_person"})),
]
