from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Band


@login_required
def index(request):
    events=Event.objects.filter(creator=request.user)
    return render(request, 'events/index.html', {'events': events})
@login_required
def ask_for_event(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        date_time=request.POST.get('date_time')
        is_outdoor=request.POST.get('is_outdoor')=='on'
        poster=request.FILES.get('poster')
        bands_input=request.POST.get('bends','')

        event=Event.objects.create(
            name=name,
            date_time=date_time,
            is_outdoor=is_outdoor,
            poster=poster,
            creator=request.user,
        )

        band_names=[b.strip() for b in bands_input.split(',') if b.strip()]
        for band_name in band_names:
            band=Band.objects.filter(name__iexact=band_name).first()
            if band:
                event.bands.add(band)

        return redirect('index')

    return render(request, 'events/ask_for_event.html')





