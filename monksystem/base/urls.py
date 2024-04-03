from django.urls import path
from . import views 



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    
    path('accounts/login/', views.loginPage, name='login'),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('register/', views.registerPage, name = "register"),

    path('viewFile/', views.viewFile, name='viewFile'),    
    path('uploadFile/', views.uploadFile, name='uploadFile'),

    path('file/<int:file_id>/', views.file, name='file'),    
    path('claim/<int:file_id>/', views.claimFile, name='claimFile'),
    path('import/', views.importFiles, name='importFiles'),

    path('doctor/<str:pk>', views.doctor, name="doctor"),
    path('viewDoctor/', views.viewDoctor, name = "viewDoctor"),
    path('addDoctor/', views.addDoctor, name = "addDoctor"),

    path('subject/<str:pk>', views.subject, name="subject"),
    path('viewSubject/', views.viewSubject, name = "viewSubject"),
    path('addSubject/', views.addSubject, name = "addSubject"),

    path('project/<str:pk>', views.project, name="project"),
    path('viewProject/', views.viewProject, name = "viewProject"),
    path('addProject/', views.addProject, name = "addProject"),

    path('viewVitals/', views.viewVitals, name = "viewVitals"),
    #path('addVitals/', views.addVitals, name = "addVitals"),
    
]