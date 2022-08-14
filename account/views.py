from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from .forms import ProfileForm
from .mixins import (
	FieldsMixin, 
	FormValidMixin, 
	AuthorAccessMixin,
	AuthorsAccessMixin,
	SuperUserAccessMixin
	)
from django.urls import reverse_lazy
from django.views.generic import (
	ListView, 
	CreateView, 
	UpdateView,
	DeleteView
	)
from blog.models import Article
from .models import User

class ArticleList(AuthorsAccessMixin, ListView):
	template_name = 'registration/home.html'

	def get_queryset(self):
		if self.request.user.is_superuser:
			return Article.objects.all()
		else:
			return Article.objects.filter(author=self.request.user)


class ArticleCreate(AuthorsAccessMixin, FormValidMixin, FieldsMixin, CreateView):
	model = Article
	template_name = 'registration/article-create-update.html'


class ArticleUpdate(AuthorAccessMixin,FormValidMixin, FieldsMixin, UpdateView):
	model = Article
	template_name = 'registration/article-create-update.html'


class ArticleDelete(SuperUserAccessMixin,DeleteView):
	model = Article
	success_url = reverse_lazy('account:home')
	template_name = 'registration/article_confirm_delete.html'

class Profile(LoginRequiredMixin, UpdateView):
	model = User
	success_url = reverse_lazy('account:profile')
	template_name = 'registration/profile.html'
	form_class = ProfileForm

	def get_object(self):
		return User.objects.get(pk= self.request.user.pk)

class Login(LoginView):
	def get_success_url(self) -> str:
		user = self.request.user

		if user.is_superuser or user.is_author:
			return reverse_lazy('account:home')
		else:
			return reverse_lazy('account:profile')

from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


class Register(CreateView):
	form_class= SignupForm
	template_name = 'registration/register.html'
	
	def form_valid(self, form):
		user = form.save(commit=False)
		user.is_active = False
		user.save()
		current_site = get_current_site(self.request)
		mail_subject = 'فعال سازی اکانت'
		message = render_to_string('registration/activate_account.html', {
			'user': user,
			'domain': current_site.domain,
			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
			'token': account_activation_token.make_token(user),
		})
		to_email = form.cleaned_data.get('email')
		email = EmailMessage(
					mail_subject, message, to=[to_email]
		)
		email.send()
		context = {
			"message": "لینک فعال سازی به ایمیل شما ارسال شد.",
			"url": "/login",
			"button_name": "ورود"
		}
		return render(self.request, "registration/activation_status.html", context)

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		context = {
			"message": "اکانت شما با موفقیت فعال شد.",
			"url": "/login",
			"button_name": "ورود"
		}
	else:
		context = {
			"message": "لینک فعال سازی منقضی شده است.",
			"url": "/registration",
			"button_name": "تلاش مجدد"
		}
	
	return render(request, "registration/activation_status.html", context)
	