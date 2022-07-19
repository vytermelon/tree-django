from django import forms

class CreateBook(forms.Form):
    book_name = forms.CharField(label='Book name', max_length=100)
    node_content = forms.CharField(label='Node 1:', max_length=2500,widget=forms.Textarea(attrs={
               'rows': 5,
               'size': 80,
               'style': 'height: 10em;'
            }))

class CreateNode(forms.Form):
    branch_content = forms.CharField(label='Branch Name', max_length=100)
    node_content = forms.CharField(label='Node Content', max_length=2500,widget=forms.Textarea(attrs={
               'rows': 5,
               'size': 80,
               'style': 'height: 10em;'
            }))



