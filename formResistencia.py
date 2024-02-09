from wtforms import Form
from wtforms  import StringField,IntegerField,EmailField,FloatField,SelectField,RadioField

class ResistenciaForm(Form):
    colores1 = SelectField('Selecciona un color', choices=[(0, 'Negro'), (1, 'Cafe'), (2, 'Rojo'),(3, 'Naranja'),(4, 'Amarillo'),(5, 'Verde'),(6, 'Azul'),(7, 'Violeta'),(8, 'Gris'),(9, 'Blanco')])
    colores2 = SelectField('Selecciona un color', choices=[(0, 'Negro'), (1, 'Cafe'), (2, 'Rojo'),(3, 'Naranja'),(4, 'Amarillo'),(5, 'Verde'),(6, 'Azul'),(7, 'Violeta'),(8, 'Gris'),(9, 'Blanco')])
    colores3 = SelectField('Selecciona un color', choices=[(1, 'Negro'), (10, 'Cafe'), (100, 'Rojo'),(1000, 'Naranja'),(10000, 'Amarillo'),(100000, 'Verde'),(1000000, 'Azul'),(10000000, 'Violeta'),(100000000, 'Gris'),(1000000000, 'Blanco')])
    
    options=RadioField('',choices=[(5,'Dorado'),(10,'Plata')]);
    
    