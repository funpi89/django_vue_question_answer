from django_registration.forms import RegistrationForm
from users.models import CustomerUser

class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomerUser