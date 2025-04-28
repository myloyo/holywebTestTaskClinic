from rest_framework import serializers
from .models import Doctor, Appointment
from datetime import time as dtime

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, data):
        appointment_time = data['time']
        if not dtime(9, 0) <= appointment_time <= dtime(17, 0):
            raise serializers.ValidationError("Время приёма вне рабочего времени (9:00–18:00).")

        doctor = data['doctor']
        date = data['date']

        existing = Appointment.objects.filter(doctor=doctor, date=date, time=appointment_time)
        if existing.exists():
            raise serializers.ValidationError("У врача уже есть запись на это время.")

        return data
