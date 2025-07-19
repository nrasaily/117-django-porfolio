from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

# about me page
def about_me_view(request):
  return render(request, 'pages/about_me.html')

# experience page
def experience(request):
  return render(request, 'pages/experience.html')

# Contact page
#def contact(request):
# return render(request, 'pages/contact.html')

def contact_view(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      message = form.cleaned_data['message']

      message_body = (
        f"You have a new email from your portfolio page \n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Message: {message}"

      )

      try:
        send_mail(
          "Email from portfolio page", #subject
          message_body, #message body
          email, # From email
          ['nareshsathi79@gmail.com'] # To email
        )
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form })
      except Exception as e:
        print(e)
        return render(request, 'pages/contact.html', {'form': form, 'error': str(e)})
  else:
    form = ContactForm()
    
  return render(request, 'pages/contact.html', {'form': form})