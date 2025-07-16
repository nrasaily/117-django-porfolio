from django.shortcuts import render

# Create your views here.

# about me page
def about_me_view(request):
  return render(request, 'pages/about_me.html')

# experience page
def experience(request):
  return render(request, 'pages/experience.html')

