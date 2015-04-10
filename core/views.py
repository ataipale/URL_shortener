from django.shortcuts import render
from django.views.generic import TemplateView, FormView, RedirectView
from . import forms 
import string
import random
from . import models
from django.shortcuts import redirect
# Create your views here.

def id_generator(size=6, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

class ShortLinkRedirectView(RedirectView):

	def get(self, request, *args, **kwargs):
		unique_id = kwargs.pop('unique_id')
		link = models.Link.objects.get(unique_ID = unique_id)

		return redirect(link.larger_link)


class SuccessView(TemplateView):
	template_name = 'core/success.html'

	# overriding methods
	def get_context_data(self, **kwargs):
		return {
			'unique_id': kwargs.pop('unique_id'),
		}

class IndexView(FormView):
	template_name = 'core/index.html'

# inheriting from our forms.py file
	form_class = forms.URLInputForm

	def form_valid(self, form):
		unique_id = id_generator(size = 10)
		long_url = form.cleaned_data['long_url']

		new_link = models.Link(larger_link = long_url, unique_ID = unique_id)

		new_link.save()

		return redirect('/success/' + unique_id)

	





