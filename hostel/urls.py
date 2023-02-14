from django.urls import path
from . import views

app_name="hostel"

urlpatterns = [
     path('index/', views.index, name="index"),
     path('signup',views.signup),
     path('otp',views.otp,name='otp'),
     path('contact_us',views.contact_us,name="contact_us"),
     path('hostel_login',views.hostel_login,name='hostel_login'),
     path('hostel_home',views.hostel_home,name='hostel_home'),
     path('profile', views.profile, name='profile'),
     path('hostel', views.hostel, name='hostel'),
     path('info', views.info, name='info'),
     path('images', views.images, name='images'),
     path('Facilities', views.Facilities, name='Facilities'),
     path('FoodMenu', views.Food_Menu, name='FoodMenu'),
     path('logout', views.logout, name='logout'),
     path('department', views.department, name='department'),
     path('fee_structure', views.fee_structure, name='fee_structure'),
     path('other_activity', views.other_activity, name='other_activity'),
     path('Aboutus', views.Aboutus, name='Aboutus'),
     path('OURFOUNDERS', views.OURFOUNDERS, name='OURFOUNDERS'),
     path('OURAIM', views.OURAIM, name='OURAIM'),
     path('PRESIDENTSMESSAGE', views.PRESIDENTSMESSAGE, name='PRESIDENTMESSAGE'),
     path('GURUKULMANAGEMENTCOMMITTIEE', views.GURUKULMANAGEMENTCOMMITTIEE, name='GURUKULMANAGEMENTCOMMITTIEE'),
     path('COREVALUESOFGURUKUL', views.COREVALUESOFGURUKUL, name='COREVALUESOFGURUKUL'),
     path('student_guidlines', views.student_guidlines, name='student_guidlines'),
     path('Yoga', views.yoga, name='yoga'),
     path('Picnic', views.picnic, name='picnic'),
     path('Arts', views.arts, name='Arts'),
     path('Games', views.games, name='Arts'),
     path('change_password', views.change_password, name='change_password'),
     path('Feedback', views.Feedback, name='Feedback'),
     path('hostel_booking', views.hostel_booking, name='hostel_booking'),
     path('select_room', views.select_room, name='select_room'),
     path('footer', views.footer, name='footer'),
     path('bookingform', views.bookingform, name='bookingform')
     
]

