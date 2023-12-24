from datetime import datetime

import pytz as pytz
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, FloatField


class ProductoForm(FlaskForm):
    tipo_producto = StringField('')
    precio = FloatField('')
    submit = SubmitField('Agregar')


class MyForm(FlaskForm):
    fecha_hora = DateTimeField('Fecha y Hora', default=datetime.now())
