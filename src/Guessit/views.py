#rendering
from django.shortcuts import render,render_to_response
#http
from django.http import HttpResponseRedirect,HttpResponse
#Template related import files
from django.template import RequestContext
#models
from Guessit.models import Songdata
#form
from Guessit.form import Song_form

question_id = 1
# Create your views here.

def home(request):
    return render_to_response('home.html')

def display_question(request):
    global question_id
    context = RequestContext(request)
    try:
        #quesno_id = {'id':question_id}
        song_data = Songdata.objects.get(song_id=question_id)
        total_ques = Songdata.objects.all().count()
    except Songdata.DoesNotExist:
        pass   #Come back here later
       
    if request.method == 'POST':
        form = Song_form(request.POST)
        if form.is_valid():
            user_answer = form.cleaned_data['answer']
            if song_data.song_name.strip() == user_answer.strip():
                if int(question_id) < int(total_ques):
                    question_id = question_id+1
                    print question_id
                    song_data = Songdata.objects.get(song_id=question_id)
                    print song_data.lyrics
                    form = Song_form()
                    return render_to_response('display_question.html', {'form':form,'song_data':song_data,'quesno_id':question_id,'total_ques':total_ques},context)
                    #return HttpResponseRedirect("/SongQuiz/question/%s/" % (int(question_id)+1))
                else:
                    return render_to_response('results.html')
            else:
                return HttpResponse("Your answer is wrong")
        else:
            print form.errors
    else:
        form = Song_form()
    return render_to_response('display_question.html',{'form':form,'song_data':song_data,'quesno_id':question_id,'total_ques':total_ques},context)
