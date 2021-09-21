from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import SnippetForm


from .models import Question, Choice

# Get question and display
def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'movies/index.html', context)

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    return render(request, 'movies/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'movies/results.html', { 'question': question })


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'movies/detail.html',{
            'question': question,
            'error_message': "You didnt select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('movies:results', args=(question.id,)))


def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            question = Question(question_text=form.cleaned_data['question'])
            question.save()
            choice1 = Choice(question=question, choice_text=form.cleaned_data['choice1'])
            choice1.save()
            choice2 = Choice(question=question, choice_text=form.cleaned_data['choice2'])
            choice2.save()
            choice3 = Choice(question=question, choice_text=form.cleaned_data['choice3'])
            choice3.save()

    form = SnippetForm()
    return render(request, 'pages/index.html', {'form': form})