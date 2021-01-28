from django.db import models
from django.utils.html import format_html


STATUS_CHOICES = [
	('d', 'Draft'),
	('p', 'Published'),
	('w', 'Withdrawn'),
]


class Author(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
   		return self.name

class Article(models.Model):

	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	body = models.TextField()
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)

	def first_word_of_title(self):
		return self.title.split()[0]

	def colored_name(self):
		return format_html(
			'<span style="color: #e04e2f;">{} {}</span>',
			self.title,
			self.status,
		)


	def __str__(self):
		return self.title