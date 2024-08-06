from django.urls import path
from todo_app import views


urlpatterns = [
    
    #CRUD - read in main home view - main folder urls
    
    # add - create
    path('addTask/',views.addTask,name='addTask'),
    
    # edit-update
    path('editTask/<int:pk>/',views.editTask,name='editTask'),
    
    # delete
    path('deleteTask/<int:pk>/',views.deleteTask,name='deleteTask'),
    
    # In progress to complete and vice versa
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),
    
]
