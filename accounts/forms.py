from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email',)

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if User.objects.filter(username=username).exists():
            suggestions = []
            i = 1
            while len(suggestions) < 3:
                new_name = f"{username}{i}"
                if not User.objects.filter(username=new_name).exists():
                    suggestions.append(new_name)
                i += 1

            raise forms.ValidationError(
                f"Bu nom band. Tavsiya: {', '.join(suggestions)}"
            )

        return username
