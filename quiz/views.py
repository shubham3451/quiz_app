from django.shortcuts import render, redirect
import random
from .models import Question, UserQuizSession, UserAnswer

# Create your views here.

def start_quiz(request):
    # Create a new quiz session
    session = UserQuizSession.objects.create(score=0, total_questions=0, correct_answers=0, incorrect_answers=0)
    request.session['quiz_session_id'] = session.id
    return redirect('quiz:question')

def get_random_question():
    # Get a random question from the database
    return random.choice(Question.objects.all())

def question(request):
    # Get the session ID from the request
    session_id = request.session.get('quiz_session_id')
    
    if not session_id:
        return redirect('quiz:start_quiz')

    session = UserQuizSession.objects.get(id=session_id)
    
    # Handle GET request: Fetch and display a random question
    if request.method == 'GET':
        # Retrieve a random question at the start of the request (only once)
        question = get_random_question()
        
        # Store the question ID in the session for consistency
        request.session['current_question_id'] = question.id


        return render(request, 'question.html', {'question': question})

    # Handle POST request: Check the user's answer
    if request.method == 'POST':
        # Retrieve the question ID from the session
        question_id = request.session.get('current_question_id')
        
        # If no question ID in the session, redirect to start quiz
        if not question_id:
            return redirect('quiz:start_quiz')
        
        # Fetch the correct question using the ID stored in the session
        question = Question.objects.get(id=question_id)

        selected_answer = request.POST.get('answer').upper()

        correct_answer = question.correct_answer.upper()


        # Check if the selected answer is correct
        is_correct = selected_answer == correct_answer
        

        # Save the user's answer and update the session
        UserAnswer.objects.create(
            session=session,
            question=question,  
            selected_answer=selected_answer,
            is_correct=is_correct
        )

        if is_correct:
            session.correct_answers += 1
            session.score += 1
        else:
            session.incorrect_answers += 1
        session.total_questions += 1 
        session.save()

        # Redirect to next question or show results
        if session.total_questions >= 5:
            return redirect('quiz:results')
        return redirect('quiz:question')
    return render(request, 'question.html', {'question': question})

def results(request):
    session_id = request.session.get('quiz_session_id')
    if not session_id:
        return redirect('quiz:start_quiz')

    session = UserQuizSession.objects.get(id=session_id)
    return render(request, 'results.html', {'session': session})



