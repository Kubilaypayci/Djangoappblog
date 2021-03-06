from django import forms

class Register(forms.Form):
	username = forms.CharField(max_length = 20, label = 'Kullanıcı Adı')
	password = forms.CharField(max_length = 20, label = 'Şifre', widget = forms.PasswordInput)
	confirm = forms.CharField(max_length = 20, label = 'Şifreyi Onayla', widget = forms.PasswordInput)
	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		confirm = self.cleaned_data.get('confirm')		
		if (password and username and confirm and password != confirm):
			raise forms.ValidationError('Şifreler aynı değil!')
		values = {
			'username' : username,
			'password' : password,	
		}
		return values
class Login(forms.Form):
	username = forms.CharField(label='Kullanıcı Adı')
	password = forms.CharField(label='Şifre', widget = forms.PasswordInput)