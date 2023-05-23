from .models import Article
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

def archive(request):
	return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
	try:
		post = Article.objects.get(id=article_id)
		return render(request, 'article.html', {"post": post})
	except Article.DoesNotExist:
		raise Http404

def create_post(request):
	if request.user.is_authenticated:
		if request.method == "POST": # обработать данные формы, если метод POST
			form = {
				'text': request.POST["text"], 'title': request.POST["title"]
			} # в словаре form будет храниться информация, введенная пользователем
			if form["text"] and form["title"]: # если поля заполнены без ошибок
				if Article.objects.filter(title = form["title"]):
					return HttpResponse(u'Error! Already exists!', content_type="text/plain")
				else:
					article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
					return redirect('get_article', article_id=article.id) # перейти на страницу поста
			else: # если введенные данные некорректны
				form['errors'] = u"Не все поля заполнены"
				return render(request, 'create_post.html', {'form': form})
		else: # просто вернуть страницу с формой, если метод GET
			return render(request, 'create_post.html', {})
	else:
		raise Http404

def register_user(request):
	if request.method == "POST":
		form = {
			'username': request.POST["username"],
			'email': request.POST["email"],
			'password': request.POST["password"]
		}
		if form["username"] and form["email"] and form["password"]: # если поля заполнены без ошибок
			try:
				User.objects.get(username=form["username"])
				form['errors'] = "Пользователь с таким именем уже есть"
				return render(request, 'register.html', {'form': form})
			except User.DoesNotExist:
				User.objects.create_user(form["username"], form["email"], form["password"])
				return redirect('archive')
		else:
			form['errors'] = "Не заполнены поля ввода"
			return render(request, 'register.html', {'form': form})
	else: # просто вернуть страницу с формой, если метод GET
		return render(request, 'register.html', {})

def auth_user(request):
	if request.method == "POST":
		form = {
			'username': request.POST["username"],
			'password': request.POST["password"]
		}
		if form["username"] and form["password"]: # если поля заполнены без ошибок
			try:
				User.objects.get(username=form["username"])
				user = authenticate(username=form["username"], password=form["password"])
				if user:
					login(request, user)
					return redirect('archive')
				else:
					form['errors'] = 'Такого аккаунта не существует'
					return render(request, 'auth.html', {'form': form})
			except User.DoesNotExist:
				form['errors'] = "Данные авторизации неверны"
				return render(request, 'auth.html', {'form': form})
		else:
			form['errors'] = "Не заполнены поля ввода"
			return render(request, 'auth.html', {'form': form})
	else: # просто вернуть страницу с формой, если метод GET
		return render(request, 'auth.html', {})
		
def exit_user(request):
	logout(request)
	return redirect('/')