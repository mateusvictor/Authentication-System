from django.urls import path, include
from .views import StudentSignUpView, TeacherSignUpView, home, signup


urlpatterns = [
	path('', home, name='home'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/signup/', signup, name='signup'),
	path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
	path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
]
