from django import forms

class VideoForm(forms.Form):
    video_url = forms.URLField(label='Ссылка на видео', required=True)
