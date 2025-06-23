from django.urls import path, include

urlpatterns = [
    path('api/', include('API.all_API.urls'))
]
