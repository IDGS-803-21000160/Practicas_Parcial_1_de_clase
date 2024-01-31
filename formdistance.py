from wtforms import Form
from wtforms  import StringField,IntegerField,EmailField,FloatField

class DistanceForm(Form):
    valorx1=FloatField('valorx1')
    valorx2=FloatField('valorx2')
    valory1=FloatField('valory1')
    valory2=FloatField('valory2')
    