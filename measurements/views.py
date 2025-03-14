from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import os

@csrf_exempt
def upload_eeg(request):
    if request.method == 'POST' and request.FILES.get('eeg_file'):
        eeg_file = request.FILES['eeg_file']
        file_path = os.path.join('uploads', eeg_file.name)
        
        # Guardar el archivo en el servidor
        saved_path = default_storage.save(file_path, eeg_file)
        
        # Simulación del procesamiento del EEG (esto se debe reemplazar con análisis real)
        result = {
            "file": eeg_file.name,
            "status": "Processed Successfully",
            "diagnosis": "No abnormal activity detected"
        }
        
        return JsonResponse(result)

    return JsonResponse({"error": "Invalid request"}, status=400)
