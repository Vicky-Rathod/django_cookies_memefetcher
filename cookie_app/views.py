from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from users.models import User
# Create your views here.
def get_memes():
    url = "https://api.imgflip.com/get_memes"
    r = requests.get(url)
    memes = r.json()
    return [memes['data']['memes'][i] for i in range(5)]


@method_decorator(login_required, name='dispatch')
class GetMemes(TemplateView):
    template_name = 'memes/memes.html'
    def render_to_response(self, context, **response_kwargs):
        response = super(GetMemes, self).render_to_response(context, **response_kwargs)
        response.set_cookie("name","user.first_name")
        return response
    def get_context_data(self, *args, **kwargs):
        try:
            user = User.objects.get(id = self.request.user.id)
            print(user.first_name)
        except:
            user = None
        context = {
            'droplets' : get_memes(),
            'user':user,
        }
        return context