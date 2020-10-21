#!flask/bin/python
from app import app
import warnings

warnings.filterwarnings("ignore")
app.run(debug = True)