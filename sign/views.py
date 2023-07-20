from django.shortcuts import render
from django.views.generic import UpdateView
from .forms import UpdateProfile, BaseRegisterForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

class Account(LoginRequiredMixin, TemplateView):
    template_name = 'sign/account.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context

@login_required
def add_authors(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return HttpResponseRedirect("/sign/account/")


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    template_name = 'sign/register.html'
    success_url = '/'

    def form_valid(self, form):
      form.save()
      user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
      login(self.request, user)
      return HttpResponseRedirect("/sign/account/")


class Update_profile(LoginRequiredMixin, UpdateView):
  model = User
  form_class = UpdateProfile
  success_url = '/'

  def setup(self, request, *args, **kwargs):
    self.user_id = request.user.pk
    return super().setup(request, *args, **kwargs)

  def get_object(self, queryset=None):
    if not queryset:
      queryset = self.get_queryset()
    return get_object_or_404(queryset, pk=self.user_id)