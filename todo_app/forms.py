from django import forms
from .models import TaskToDo



class TaskToDoForm(forms.ModelForm):
    
 
    class Meta:

        model = TaskToDo
        fields = ('featured_image','name','task','priority')

    