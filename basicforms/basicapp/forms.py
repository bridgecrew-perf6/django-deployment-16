from django import forms
from django.core import validators


# nahve dorost kardan validation haye dasti, khodeman tayin konim
# nokte : baraye bekar giri in mahdoodiyat dar parametri:
# dar dakhele parantez parametre morede nzr validators=[func_name] ghrar midahim.

def chek_name(value):
    if value[0].lower() == 'z':
        raise forms.ValidationError("you can't use z for start name")


class FormName(forms.Form):
    name = forms.CharField(validators=[chek_name])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)

    # khate payin dar vaghe dar form namayesh dade nemishavad ama dar inspect page vojod darad ke
    # baraye gir andakhtane robat ha bekar gerefte mishavad ;)
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_mail = all_clean_data['verify_email']
        if email != v_mail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH")

    # bejaye tabe zir line 23 ra gharra dadim va az yeki az builtin haye python estefade kardim
    # def clean_bot(self):
    #     bot = self.cleaned_data['bot_catcher']
    #     if bot:
    #         raise forms.ValidationError('GOTCHA BOT !')
    #     return bot




