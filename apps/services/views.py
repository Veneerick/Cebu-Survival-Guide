from django.shortcuts import render

# Sample data only (mirrors the Blazor app).
EMERGENCY = [
    {'id': 'police', 'name': 'Police', 'number': '911', 'icon': 'shield',
     'description': 'Crime, theft, or immediate danger. Stay on the line.'},
    {'id': 'fire', 'name': 'Fire Department', 'number': '911', 'icon': 'flame',
     'description': 'Fires, explosions, and rescue situations.'},
    {'id': 'medical', 'name': 'Ambulance / Medical Emergency', 'number': '911', 'icon': 'medical',
     'description': 'Serious injury or sudden illness needing urgent care.'},
    {'id': 'redcross', 'name': 'Philippine Red Cross', 'number': '143', 'icon': 'cross',
     'description': 'First aid, blood services, and disaster response.'},
]

OTHER = [
    {'name': 'Hospitals', 'description': 'Find nearby hospitals and clinics', 'icon': 'hospital'},
    {'name': 'Government Offices', 'description': 'City Hall and public services', 'icon': 'building'},
    {'name': 'Tourist Assistance', 'description': 'Help for visitors', 'icon': 'compass'},
    {'name': 'Disaster Information', 'description': 'Typhoon and earthquake updates', 'icon': 'storm'},
]


def services(request):
    """Essential Services page: emergency contacts + non-emergency services."""
    return render(request, 'services/services.html', {'emergency': EMERGENCY, 'other': OTHER})
