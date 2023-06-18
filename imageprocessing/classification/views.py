from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import PredictionForm
from. models import Prediction

def predict(request: HttpRequest):
    context = dict()
    context["form"] = PredictionForm

    # if request.method == "POST":
    #     form_data = PredictionForm(data=request.POST, files=request.FILES)
    #     if form_data.is_valid():
    #         flight: Flight = form_data.save(commit=False)
    #         flight.user = request.user
    #         flight.picture = form_data.cleaned_data["picture"]
    #         flight.save()
    #         return redirect("flights")
    # context["flights"] = Flight.objects.all()
    return render(request, "prediction.html", context=context)