from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        # Get the selected choice from the request
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # If no choice is selected or the choice does not exist, show an error message
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        # Increment the vote count for the selected choice
        selected_choice.votes += 1
        selected_choice.save()

        # Redirect to the results page
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # Display the 5 most recent questions
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # Get the question by its ID or return a 404 if not found
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    # Get the question by its ID or return a 404 if not found
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})