#views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from .models import User, Comment, Contact
from django.contrib.auth import logout as auth_logout



# Registration view
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')  # New field for confirming password

        # Check if the passwords match
        if password != password_confirm:
            messages.error(request, 'Passwords do not match')  # Add error message if passwords don't match
            return render(request, 'register.html')

        # Check if the email already exists
        user = User.objects.filter(email=email)
        if user.exists():
            messages.error(request, 'Email already exists')  # Add error message if email exists
            return render(request, 'register.html')

        # Create and save the new user
        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        #messages.success(request, 'Registration successful! Please log in.')  # Success message
        return redirect('login')

    return render(request, 'register.html')



def login_view(request):
    messages.get_messages(request).used = True

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Attempt to fetch the user by email using filter (no exception handling)
        user = User.objects.filter(email=email).first()
        # `first()` will return the first match or None


        if user and user.password == password:  # If user exists and the password matches
            # Store the user ID in session to track the logged-in user
            request.session['user_id'] = user.id
            messages.success(request, f'Welcome, {user.first_name}!')
            return redirect('index')  # Redirect to the index page after successful login
        else:
            messages.error(request, 'Invalid email or password')  # Error message for incorrect login

    return render(request, 'login.html')

'''def logout_view(request):
    # Clear any previous messages
    messages.get_messages(request).used = True

    # Log the user out
    auth_logout(request)

    # Redirect to login page after logging out
    return redirect('home')'''

def logout_view(request):
    # Clear the session (log out the user)
    request.session.flush()  # This will remove the user from the session
    return redirect('home')  # Redirect to the homepage after logout


'''def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user exists with the given email and password
        user = User.objects.filter(email=email, password=password)
        if user.exists():
            return redirect('index')  # Redirect to the index page if login is successful
        else:
            messages.error(request, 'Invalid email or password')  # Add error message
            return redirect('login')  # Redirect back to login if credentials are invalid

    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # This will end the user's session
    return redirect('home')  # Redirect to the home page or login page after logout'''






def comment(request):
    if request.method == 'POST':
        # Retrieve the form data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Check if all required fields are filled
        if not name or not email or not message:
            messages.error(request, "All fields are required!")
            return redirect('blog')  # Redirect back to the blog page if fields are missing

        # Save the comment to the database if all fields are present
        comment = Comment(name=name, email=email, message=message)
        comment.save()

        # Show a success message
        messages.success(request, "Your comment has been posted successfully!")

        # Redirect back to the blog page after saving the comment
        return redirect('blog')

    # If the request is not a POST, just render the blog page
    return render(request, 'blog.html')

    # Check if email already exists in the database (unique constraint)
''' if Comment.objects.filter(email=email).exists():
            messages.error(request, "A comment with this email already exists.")
            return redirect('blog')'''


def saveEnquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name = name, email= email, subject = subject, message = message)
        contact.save()
        return redirect('contact')
    return render(request,'contact.html')


'''def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid credentials, please try again.")
            return redirect('login')

        # Check if password is correct
        if user.check_password(password):
            # Password is correct, log the user in
            request.session['user_id'] = user.id
            messages.success(request, "Login successful!")
            return redirect('home')  # Redirect to home or dashboard
        else:
            messages.error(request, "Invalid credentials, please try again.")
            return redirect('login')

    return render(request, 'login.html')
'''

def index(request):
        user_id = request.session.get('user_id')  # Retrieve the user ID from the session
        user = None
        if user_id:
            user = User.objects.get(id=user_id)  # Retrieve the user object from the database
        return render(request, 'index.html', {'user': user})


def course(request):
    return render(request,'course.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')
def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,'home.html')



#def register(request):
 #   return render(request,'register.html')

#def login(request):
 #   return render(request,'login.html')

