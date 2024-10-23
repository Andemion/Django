from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Band, Listing
from listings.forms.forms import ContactUsForm, BandForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html.twig', {'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html.twig', {'band': band})


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request, 'listings/band_create.html.twig', {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)  # on pré-remplir le formulaire avec un groupe existant
    return render(request,
                  'listings/band_update.html.twig',
                  {'form': form})


def listing(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.htm.twig', {'listings': listings})


def about(request):
    return render(request, 'listings/about.html.twig')


def contact(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
        return redirect('email-sent')
    else:
        form = ContactUsForm()  # ajout d’un nouveau formulaire ici

    return render(request, 'listings/contact.html.twig', {'form': form})
