# airlines/views.py
from rest_framework import viewsets
from .models import Airplane
from .serializers import AirplaneSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse

class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    @action(detail=False, methods=['GET'], url_path='fuel_consumption')
    def fuel_consumption(self, request):
        airplanes = Airplane.objects.all()

        if not airplanes:
            # Handle the case when the list is empty
            return Response({"detail": "No airplanes available."}, status=400)

        # Calculate total fuel consumption per minute for all airplanes
        total_fuel_consumption = sum(plane.fuel_consumption_per_minute() for plane in airplanes)

        # Calculate the maximum minutes each airplane can fly
        max_minutes_to_fly = min((plane.fuel_tank_capacity() / plane.fuel_consumption_per_minute()) for plane in airplanes)

        result = {
            'total_fuel_consumption_per_minute': total_fuel_consumption,
            'max_minutes_to_fly': max_minutes_to_fly
        }

        return JsonResponse(result)
