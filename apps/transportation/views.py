from django.http import Http404
from django.shortcuts import render

# Sample data only (mirrors the Blazor app). Replace with database models later.
ROUTES = [
    {'code': '04L', 'start': 'Lahug', 'end': 'Colon', 'via': 'Mango Avenue', 'color': '#1C90F7',
     'path': 'M470 90 L400 140 L330 190 L270 240 L200 290',
     'stops': ['Lahug', 'JY Square', 'Mango Avenue', 'Fuente Osmeña', 'Colon']},
    {'code': '17B', 'start': 'Ayala Center', 'end': 'Carbon Market', 'via': 'Osmeña Blvd', 'color': '#D61ADC',
     'path': 'M470 90 L520 190 L470 260 L350 320 L270 330',
     'stops': ['Ayala Center', 'Cebu Business Park', 'Osmeña Blvd', 'Carbon Market']},
    {'code': '01K', 'start': 'Talamban', 'end': 'SM City', 'via': 'Escario Street', 'color': '#A6D619',
     'path': 'M120 350 L200 290 L330 250 L400 210 L560 160',
     'stops': ['Talamban', 'Gorordo Avenue', 'Escario Street', 'SM City']},
]

LANDMARKS = [
    {'name': 'Lahug', 'x': 470, 'y': 90}, {'name': 'Colon', 'x': 200, 'y': 290},
    {'name': 'IT Park', 'x': 520, 'y': 190}, {'name': 'Carbon', 'x': 270, 'y': 330},
    {'name': 'Ayala', 'x': 400, 'y': 210},
]

TRANSPORT_TYPES = [
    {'name': 'Jeepney', 'description': 'Cheapest option. Flag down, pay the driver.', 'icon': 'jeep', 'tile': 'mag'},
    {'name': 'Bus', 'description': 'Best for longer city-to-city trips.', 'icon': 'bus', 'tile': 'grn'},
    {'name': 'Taxi', 'description': 'Metered. Ask the driver to use the meter.', 'icon': 'taxi', 'tile': 'amb'},
    {'name': 'Modern Jeepney', 'description': 'Air-conditioned, fixed stops.', 'icon': 'modern', 'tile': 'blu'},
]


def _find(code):
    return next((r for r in ROUTES if r['code'].lower() == str(code).lower()), None)


def transportation(request):
    """Transportation page: route search, map, route info card, ways to get around."""
    query = request.GET.get('q', '').strip()
    routes = ROUTES
    if query:
        q = query.lower()
        routes = [r for r in ROUTES if any(q in r[k].lower() for k in ('code', 'start', 'end', 'via'))]
    selected = _find(request.GET.get('route', '')) or (routes[0] if routes else None)
    return render(request, 'transportation/transportation.html', {
        'query': query, 'routes': routes, 'all_routes': ROUTES, 'selected': selected,
        'landmarks': LANDMARKS, 'transport_types': TRANSPORT_TYPES,
    })


def route_detail(request, code):
    route = _find(code)
    if route is None:
        raise Http404('Route not found')
    stops = [{'n': i + 1, 'name': s, 'first': i == 0, 'last': i == len(route['stops']) - 1}
             for i, s in enumerate(route['stops'])]
    return render(request, 'transportation/route_detail.html', {'route': route, 'stops': stops})
