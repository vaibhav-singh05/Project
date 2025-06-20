from django.urls import path
from .views import GoogleLoginView, CsvToExcelView, google_login_page, dashboard, HotelListAPIView, hotel_page

urlpatterns = [
    # API Endpoints
    path('google-login/', GoogleLoginView.as_view(), name='google-login'),
    path('csv-to-excel/', CsvToExcelView.as_view(), name='csv-to-excel'),

    # Frontend Page
    path('google-login-page/', google_login_page, name='google-login-page'),
    path('dashboard/', dashboard, name='dashboard'),
    path('hotels/', HotelListAPIView.as_view(), name='hotels'),
    path('hotels-page/', hotel_page, name='hotels-page'),
]