from django.shortcuts import render

# Sample data only (mirrors the Blazor app).
TIPS = [
    ('Transport', 'Carry small bills', 'Jeepney drivers rarely have change for large notes. Keep coins and small bills ready.'),
    ('Transport', "Say 'para' to get off", "Call out 'para' or tap the roof or rail when you want the driver to stop."),
    ('Transport', 'Ask for the meter', 'In a taxi, ask the driver to use the meter before you ride.'),
    ('Safety', 'Guard your phone and wallet', 'Keep valuables in front pockets or a zipped bag in crowded areas and on jeepneys.'),
    ('Safety', 'Save emergency numbers offline', 'Store 911 and the Red Cross number in your phone before you need them.'),
    ('Safety', 'Share your trip', 'Tell someone your route when you travel at night or to unfamiliar areas.'),
    ('Weather', 'Check typhoon advisories', 'Follow official weather bulletins before long trips during typhoon season.'),
    ('Weather', 'Know your evacuation spot', 'Ask your hotel or host where the nearest evacuation center is.'),
    ('Weather', 'Expect flooded streets', 'Heavy rain can flood low areas quickly. Allow extra travel time.'),
]
BADGE = {'Transport': 'blu', 'Safety': 'grn', 'Weather': 'amb'}


def tips(request):
    """Survival Tips page with category filter chips."""
    categories = ['All'] + list(dict.fromkeys(t[0] for t in TIPS))
    current = request.GET.get('category', 'All')
    if current not in categories:
        current = 'All'
    items = [{'category': c, 'title': t, 'body': b, 'badge': BADGE.get(c, 'amb')}
             for c, t, b in TIPS if current == 'All' or c == current]
    return render(request, 'tips/tips.html', {'categories': categories, 'current': current, 'tips': items})
