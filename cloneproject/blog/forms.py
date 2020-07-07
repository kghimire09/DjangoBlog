from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('author','title','text')
#formatting the specific widgets
        widgets = {
        #title is connected to the textinputclass which is our class.
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            #text is connected to three css classes.
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

# the comment form. much similar to the post form
class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')

        widgets = {

            'author':forms.TextInput(attrs={"class":'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
