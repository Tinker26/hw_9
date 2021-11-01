from django.forms import ModelForm
from shop.models import Krasofkalar

class CreateKrasofkaForm(ModelForm):
    
    class Meta:
        fields = ('name','old_price','image','price','category')
        model = Krasofkalar

