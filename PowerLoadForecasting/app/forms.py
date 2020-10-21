#from flask import request
from datetime import date
from flask.ext.wtf import Form
from wtforms import SelectField,BooleanField,FloatField
from wtforms_components import DateField,DateRange
from wtforms.validators import DataRequired

class PredictOpts(Form):
    type = SelectField('type', validators=[DataRequired()], choices=[('Max', 'Max'),('Average', 'Average'),('Min', 'Min')])
    start = DateField('start_date',validators=[DateRange(min=date(2007,1,1),max=date(2007,12,31),format="%Y/%m/%d")])
    end = DateField('end_date',validators=[DateRange(min=date(2007,1,1),max=date(2007,12,31),format="%Y/%m/%d")])
    season = BooleanField('season', default=False)
    holiday = BooleanField('holiday', default=False)
    history = BooleanField('history', default=True)
    #start = StringField('start_date', validators=[DataRequired()])
    #type = request.form.get('type')
    #start = request.form.get('start_date')
    #end = request.form.get('end_date')

class Radar_range(Form):
    start = DateField('start_date',validators=[DateRange(min=date(2005,1,1),max=date(2007,12,31),format="%Y/%m/%d")])
    end = DateField('end_date',validators=[DateRange(min=date(2005,1,1),max=date(2007,12,31),format="%Y/%m/%d")])

class ES_para(Form):
    date = DateField('current_date',validators=[DateRange(min=date(2007,1,1),max=date(2007,12,31),format="%Y/%m/%d")])
    sigma = FloatField('current_sigma')
    mu = FloatField('current_mu')
