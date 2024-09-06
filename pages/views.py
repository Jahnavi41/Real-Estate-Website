from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP (Seller of the month)
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)

@staff_member_required
def special1(request):
    # Logic for your special page
    context = {
        'message': 'Welcome to the special admin page!'
    }
    return render(request, 'pages/special_page.html', context)

from realtors.form import RealtorForm
from django.shortcuts import redirect
@staff_member_required
def special(request):
    if request.method == 'POST':
        form = RealtorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect after successful form submission
        else:
            print(form.errors)  # Print form errors to the console
    else:
        form = RealtorForm()
    return render(request, 'pages/special_page.html', {'form': form})

@staff_member_required
def approval(request):
    pending_listings = Listing.objects.filter(status='pending')
    approved_listings = Listing.objects.filter(status='approved')
    rejected_listings = Listing.objects.filter(status='rejected')

    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        action = request.POST.get('action')
        listing = get_object_or_404(Listing, id=listing_id)
        
        if action == 'approve':
            listing.status = 'approved'
        elif action == 'reject':
            listing.status = 'rejected'
        
        listing.save()
        #return redirect('pages/approval_status.html')

    context = {
        'pending_listings': pending_listings,
        'approved_listings': approved_listings,
        'rejected_listings': rejected_listings,
    }
    return render(request, 'pages/approval_status.html', context)