from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.forms import ModelForm

from userauth import models


class UserInfoCreateForm(ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ('about', 'user_pic',)

    def clean_user_pic(self):
        user_pic = self.cleaned_data['user_pic']

        try:
            w, h = get_image_dimensions(user_pic)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = user_pic.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(user_pic) > (20 * 1024):
                raise ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return user_pic

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

