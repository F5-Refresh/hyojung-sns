from django.urls import path

from .views import SignInAPIView, SignOutAPIView, SignUpAPIView

urlpatterns = [
    path('signup', SignUpAPIView.as_view()),
    path('signin', SignInAPIView.as_view()),
    path('signout', SignOutAPIView.as_view()),
]
