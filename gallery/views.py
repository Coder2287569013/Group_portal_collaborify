from django.shortcuts import render
from .models import Photo
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .forms import PhotoForms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixin import UserIsOwnerMixin


class PhotoCreatViews(LoginRequiredMixin,CreateView):
    model = Photo
    form_class = PhotoForms
    success_url = reverse_lazy('gallery-list')

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)
    

class PhotoListViews(ListView):
    model = Photo
    context_object_name = 'photos'
    paginate_by = 20


class PhotoDeleteViews(UserIsOwnerMixin,LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('gallery-list')
    