from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1,null=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return self.text

class UserQuizSession(models.Model):
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Session {self.id} - Score: {self.score}"
    
class UserAnswer(models.Model):
    session = models.ForeignKey(UserQuizSession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,null =True, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    is_correct = models.BooleanField()

    def __str__(self):
        return f"Answer for Question {self.question.id}"



