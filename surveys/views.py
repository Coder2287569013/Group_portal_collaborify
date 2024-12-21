from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Survey, Question, Choice, Answer
from .forms import SurveyForm, QuestionForm, ChoiceForm

def survey_list(request):
    surveys = Survey.objects.filter(is_active=True)
    return render(request, 'surveys/survey_list.html', {'surveys': surveys})

@login_required
def create_survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save()
            return redirect('add_question', survey_id=survey.id)
    else:
        form = SurveyForm()
    return render(request, 'surveys/create_survey.html', {'form': form})

@login_required
def add_question(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.survey = survey
            question.save()
            
            if question.question_type in ['single', 'multiple']:
                choices = request.POST.getlist('choices[]')
                for choice_text in choices:
                    if choice_text.strip():
                        Choice.objects.create(
                            question=question,
                            text=choice_text.strip()
                        )
            
            if 'add_another' in request.POST:
                return redirect('add_question', survey_id=survey.id)
            return redirect('survey_list')
    else:
        question_form = QuestionForm()
    
    return render(request, 'surveys/add_question.html', {
        'form': question_form,
        'survey': survey
    })

@login_required
def survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    if request.method == 'POST':
        for question in survey.questions.all():
            if question.question_type == 'text':
                answer_text = request.POST.get(f'question_{question.id}')
                if answer_text:
                    Answer.objects.create(
                        user=request.user,
                        survey=survey,
                        question=question,
                        text_answer=answer_text
                    )
            else:
                choice_ids = request.POST.getlist(f'question_{question.id}')
                if choice_ids:
                    answer = Answer.objects.create(
                        user=request.user,
                        survey=survey,
                        question=question
                    )
                    answer.choice_answer.set(choice_ids)
        
        messages.success(request, 'Спасибо за участие в опросе!')
        return redirect('survey_list')
    
    return render(request, 'surveys/survey_detail.html', {'survey': survey})
