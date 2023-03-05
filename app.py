
from flask import Flask, render_template
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    number = datetime.datetime.now().second
    t = np.linspace(0, 2*np.pi, 100)
    x = np.sin(t)
    y = np.sin(number*2*t)
    
    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines'), row=1, col=1)
    fig.update_layout(title='Plot '+str(number), showlegend=False)
    
    graph_html = fig.to_html(full_html=True)
    
    return render_template('index.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)



