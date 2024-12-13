from django.contrib import admin
from .models import Question, UserQuizSession, UserAnswer


# Registering the Question model to appear in the admin interface
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer')
    search_fields = ('text',)  # Allows searching by question text
    list_filter = ('correct_answer',)  # Add filter by correct answer

admin.site.register(Question, QuestionAdmin)

# Registering the UserQuizSession model to appear in the admin interface
class UserQuizSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'score', 'total_questions', 'correct_answers', 'incorrect_answers')
    search_fields = ('id',)
    list_filter = ('score',)

admin.site.register(UserQuizSession, UserQuizSessionAdmin)

# Registering the UserAnswer model to appear in the admin interface
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('session', 'question', 'selected_answer', 'is_correct')
    search_fields = ('session__id', 'question__text',)  # Search by session ID or question text
    list_filter = ('is_correct',)

admin.site.register(UserAnswer, UserAnswerAdmin)


