from django.urls import path
from Chittoor import views

urlpatterns = [
	path('',views.home,name="homepage"),
	path('about/',views.about,name="aboutpage"),
	path('ct/',views.contact,name="cnt"),
	path('signup/',views.signup,name='register'),
]