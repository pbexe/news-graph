from django.apps import AppConfig
import nltk
class MyAppConfig(AppConfig):
	name = 'news'
	verbose_name = "News-Graph"
	def ready(self):
		print("Checking nltk")
		nltk.download("book")
		("NLTK initiated")