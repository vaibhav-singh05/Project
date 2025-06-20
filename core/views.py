from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.http import FileResponse
from django.conf import settings
from django.shortcuts import render
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
import pandas as pd
import os
import uuid
from rest_framework import status
from .models import Hotel

# ✅ Render Google login HTML with client ID from settings
def google_login_page(request):
    return render(request, 'google_login.html', {
        'google_client_id': settings.GOOGLE_CLIENT_ID
    })


# ✅ Google Login endpoint with real token validation
class GoogleLoginView(APIView):
    def post(self, request):
        token = request.data.get("id_token")
        if not token:
            return Response({"error": "ID token is required"}, status=400)

        try:
            idinfo = id_token.verify_oauth2_token(token, google_requests.Request(), settings.GOOGLE_CLIENT_ID)
            return Response({
                "message": "Login successful",
                "email": idinfo.get("email"),
                "name": idinfo.get("name"),
            })
        except ValueError:
            return Response({"error": "Invalid ID token"}, status=401)


# ✅ CSV to Excel conversion API
class CsvToExcelView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        csv_file = request.FILES.get('file')

        if not csv_file or not csv_file.name.endswith('.csv'):
            return Response({'error': 'Only CSV files allowed'}, status=400)

        try:
            df = pd.read_csv(csv_file)
        except Exception as e:
            return Response({'error': f'Failed to read CSV: {str(e)}'}, status=400)

        filename = f"converted_{uuid.uuid4().hex}.xlsx"
        excel_path = os.path.join(settings.MEDIA_ROOT, filename)

        try:
            df.to_excel(excel_path, index=False)
        except Exception as e:
            return Response({'error': f'Failed to convert to Excel: {str(e)}'}, status=500)

        return Response({'filename': filename})



def dashboard(request):
    return render(request, 'dashboard.html')


class HotelListAPIView(APIView):
    def get(self, request):
        city = request.GET.get('city', '').lower()
        if not city:
            return Response({"error": "City parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        hotels = Hotel.objects.filter(city__iexact=city)

        data = [
            {"name": h.name, "address": h.address, "price": h.price}
            for h in hotels
        ]

        return Response({"hotels": data})
    
def hotel_page(request):
    return render(request, 'hotels.html')