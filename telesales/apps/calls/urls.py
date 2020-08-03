from django.urls import path, include
from .views import (CreateCallView, UpdateDispositionView,
                    GetAllCallsView, GetAllUserCallsView,
                    DeleteCallView,)

urlpatterns = [
    path('add/', CreateCallView.as_view(), name='add_call'),
    path('all/', GetAllCallsView.as_view(), name='get_all_calls'),
    path('user/<str:name>/', GetAllUserCallsView.as_view(), name='get_user_calls'),
    path('update/<int:id>/', UpdateDispositionView.as_view(), name='update_call'),
    path('delete/<int:id>/', DeleteCallView.as_view(), name='delete_call'),
]
