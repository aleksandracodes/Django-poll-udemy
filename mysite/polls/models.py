from django.db import models
from django.utils import timezone
import datetime


# Create a new table in our db which will hold our questions
# and each of a question will have a text & publish date
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date_published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return (now - datetime.timedelta(days=1) <= self.pub_date <= now)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text