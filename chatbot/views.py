from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Chat
from .forms import UserRegistrationForm

from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('chat')
    else:
        form = UserRegistrationForm()
    return render(request, 'chatbot/register.html', {'form': form})


def chat(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        # Here you would call your chatbot logic to get the answer
        answer = "This is a placeholder answer."  # Replace with chatbot logic
        chat_entry = Chat(user=request.user, question=question, answer=answer)
        chat_entry.save()
        return render(request, 'chatbot/chat.html', {'question': question, 'answer': answer})
    return render(request, 'chatbot/index.html')


def chat_history(request):
    chats = Chat.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'chatbot/chat_history.html', {'chats': chats})




# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat')  # Redirect to the chat page after login
    else:
        form = AuthenticationForm()
    return render(request, 'chatbot/login.html', {'form': form})



# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout