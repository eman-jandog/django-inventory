from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Row, Field
from .models import Profile


class CreateRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        profile_fields = ['department', 'position', 'address', 'phone_number', 'image', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            profile = self.instance.profile
            self.fields['department'] = forms.ChoiceField(
                choices=Profile.DEPARTMENT_CHOICES,
                initial=profile.department if profile else '',
                required=False,
                label='Department'
            )
            self.fields['position'] = forms.CharField(
                max_length=100,
                initial=profile.position if profile else '',
                required=False,
                label='Position'
            )
            self.fields['address'] = forms.CharField(
                max_length=200,
                initial=profile.address if profile else '',
                required=False,
                label='Address'
            )
            self.fields['phone_number'] = forms.CharField(
                max_length=20,
                initial=profile.phone_number if profile else '',
                required=False,
                label='Phone Number'
            )
            self.fields['image'] = forms.ImageField(
                required=False,
                initial=profile.image if profile else None,
                label='Profile Image'
            )
            self.fields['bio'] = forms.CharField(
                widget=forms.Textarea(attrs={'rows': 4}),
                initial=profile.bio if profile else '',
                required=False,
                label='Bio'
            )

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div(
                    Field(
                        'first_name',
                        label_class="block text-sm font-medium text-gray-700 mb-2",
                        css_class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    )
                ),  
                Div(
                    Field(
                        'last_name',
                        label_class="block text-sm font-medium text-gray-700 mb-2",
                        css_class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    )
                ),
                css_class="grid grid-cols-1 md:grid-cols-2 gap-6"
            ),
            Div(
                Div(
                    Field(
                        'username',
                        label_class="block text-sm font-medium text-gray-700 mb-2",
                        css_class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    )
                ),  
                Div(
                    Field(
                        'email',
                        label_class="block text-sm font-medium text-gray-700 mb-2",
                        css_class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    )
                ),
                css_class="grid grid-cols-1 md:grid-cols-2 gap-6"
            ), 
            Div(
                Div(
                    Field(
                        'position',
                        label_class="block text-sm font-medium text-gray-700 mb-2",
                        css_class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    )
                ),  
                Div(
                    Field(
                        'department',
                        label_class="block text-sm font-medium text-gray-700 mb-2",
                        css_class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    )
                ),
                css_class="grid grid-cols-1 md:grid-cols-2 gap-6"
            ),
            Div(
                Div(
                    Field(
                        'address',
                        label_class="block text-sm font-medium text-gray-700 mb-2",
                        css_class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    )
                ),  
                Div(
                    Field(
                        'phone_number',
                        label_class="block text-sm font-medium text-gray-700 mb-2",
                        css_class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    )
                ),
                css_class="grid grid-cols-1 md:grid-cols-2 gap-6"
            ),
            Div(
                Field(
                    'bio',
                    label_class="block text-sm font-medium text-gray-700 mb-2",
                    placeholder="Tell us about yourself...",
                    css_class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                )
            )
        )
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        profile, created = Profile.objects.get_or_create(user=user)
        profile.department = self.cleaned_data.get('department', profile.department)
        profile.position = self.cleaned_data.get('position', profile.position)
        profile.address = self.cleaned_data.get('address', profile.address)
        profile.phone_number = self.cleaned_data.get('phone_number', profile.phone_number)
        profile.image = self.cleaned_data.get('image', profile.image)
        profile.bio = self.cleaned_data.get('bio', profile.bio)
        if commit:
            profile.save()
        return user