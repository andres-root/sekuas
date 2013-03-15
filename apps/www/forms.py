from django import forms

class newPostForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput())
	content = forms.CharField(widget=forms.TextInput())

	def clean(self):
		return self.cleaned_data
