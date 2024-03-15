# Import necessary modules

# from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reminders
import json

# Endpoint to handle saving reminders
@csrf_exempt
def reminder_save(request):
    if request.method == 'POST':
        # Parse JSON data from request body
        data = json.loads(request.body)

        # Extract necessary fields from JSON data
        date = data.get('date')
        time = data.get('time')
        message = data.get('message')

        # Check if all required fields are present
        if date and time and message:
            # Create and save reminder object
            remainder = Reminders(date=date, time=time, message=message)
            remainder.save()

            # Return success response
            return JsonResponse({'status': 'Reminder saved successfully.'})
        else:
            # Return error response if any required field is missing
            return JsonResponse({'error': 'Missing required fields.'}, status=400)
    else:
        # Return error response for unsupported HTTP methods
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
