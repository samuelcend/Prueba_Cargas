from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views  # ← Esto es necesario para acceder a measurement_list y measurement_create
from measurements.views import upload_eeg

urlpatterns = [
    path('measurements/', views.measurement_list),
    path('measurementcreate/', csrf_exempt(views.measurement_create), name='measurementCreate'),

    # ✅ Nuevo endpoint para la carga de EEG
    path('upload-eeg/', upload_eeg, name='upload-eeg'),
]
