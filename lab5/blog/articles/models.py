from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateField(auto_now_add=True)
	month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня','июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

	def __unicode__ (self):
		return "%s: %s" % (self.author.username, self.title)
	def get_excerpt(self):
		return self.text[:140] + "..." if len(self.text) > 140 else self.text
	def get_text(self):
		return self.text
	def get_date(self):
		d = self.created_date
		return "%d %s %d" % (d.day, self.month_list[d.month-1], d.year)