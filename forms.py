from django import forms

#TOPIC_CHOICES = (
#    ('general', 'General enquiry'),
#    ('bug', 'Bug report'),
#    ('suggestion', 'Suggestion'),
#)

class PingForm(forms.Form):
#    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    pingback = forms.CharField()
#    sender = forms.EmailField(required=False)

