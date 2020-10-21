from flask import *
from app import app
from datetime import date
from .forms import *
from .models import PredictList
from .algorithm import svm
from .algorithm import multilinear
from .algorithm import Algorithm_test
from .function import Weather
from .function import SimilarDays
from werkzeug.datastructures import MultiDict

# index view function suppressed for brevity

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@app.route('/index.html', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/dashboard.html', methods = ['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/SVM', methods = ['GET', 'POST'])
@app.route('/SVM.html', methods = ['GET', 'POST'])
def SVM():
    form = PredictOpts()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print(form.type.data)
        print(form.start.data)
        print(form.end.data.strftime('%Y/%m/%d'))
        print(form.season.data)
        print(form.holiday.data)
        print(form.history.data)
        if form.history.data:
            i = 1
        else:
            i = 0
        if form.season.data:
            i = i + 2
        if form.holiday.data:
            i = i + 4
        result = Algorithm_test.Predict_Main(str(form.start.data), str(form.end.data), i, str(form.type.data))
        return render_template('SVM.html',results = result,form = form)
    result = Algorithm_test.Predict_Main()
    return render_template('SVM.html',results = result,form = form)

@app.route('/linear', methods = ['GET', 'POST'])
@app.route('/MultiLinear', methods = ['GET', 'POST'])
@app.route('/linear.html', methods = ['GET', 'POST'])
@app.route('/MultiLinear.html', methods = ['GET', 'POST'])
def MultiLinear():
    form = PredictOpts()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        if form.history.data:
            i = 1
        else:
            i = 0
        if form.season.data:
            i = i + 2
        if form.holiday.data:
            i = i + 4
        result = multilinear.Predict_Main(str(form.start.data), str(form.end.data), i, str(form.type.data))
        return render_template('MultiLinear.html',results = result,form = form)
    result = multilinear.Predict_Main()
    return render_template('MultiLinear.html',results = result,form = form)

@app.route('/Radar', methods = ['GET', 'POST'])
@app.route('/Radar.html', methods = ['GET', 'POST'])
def Radar():
    form = Radar_range()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print(form.start.data)
        print(form.end.data.strftime('%Y/%m/%d'))
        result = Weather.Weather_Main(str(form.start.data), str(form.end.data))
        return render_template('Radar.html',results = result,form = form)
    result = Weather.Weather_Main()
    return render_template('Radar.html',results = result,form = form)

@app.route('/EffectScatter', methods = ['GET', 'POST'])
@app.route('/EffectScatter.html', methods = ['GET', 'POST'])
def EffectScatter():
    form = ES_para()
    if form.validate_on_submit():
        print(form.sigma.data)
        print(form.mu.data)
        result = SimilarDays.Similar_Search(str(form.date.data),form.mu.data,form.sigma.data)
        return render_template('EffectScatter.html',results = result,form = form)
    result = SimilarDays.Similar_Search()
    return render_template('EffectScatter.html',results = result,form = form)

@app.route('/test.html', methods = ['GET', 'POST'])
def test():
    result = SimilarDays.Similar_Search()
    return render_template('test.html',results = result)