# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import *
from pyecharts import Line

Remote_host = "https://pyecharts.github.io/assets/js"

# Create your views here.
def index(request):
    agent_list = agent_score.objects.all()
    context = {'list': agent_list}
    return render(request, 'agent_score/index.html', context)

def show(request, id):
    score_list = agent_score.objects.get(pk=id)
    data = {
            'observe':eval(score_list.observe_score),
            'evaluate':eval(score_list.evaluate_score),
            'predict':eval(score_list.predict_score)

    }
    columns = {
                'observe': [str(i) for i in range(len(data['observe']))],
                'evaluate': [str(i) for i in range(len(data['evaluate']))],
                #'predict': [str(i) for i in range(len(data['observe']), (len(data['observe'])+len(data['predict'])))]
    }

    line = Line("Line Chart", "Agent_Score", width=2000, height=800)
    line.add('Observe', columns['observe'], data['observe'], mark_line=['average'])
    line.add('Evaluate', columns['evaluate'], data['evaluate'], mark_line=['average'])
    #line.add('Predict', columns['predict'], data['predict'])


    context = dict(
        myechart=line.render_embed(),
        host=Remote_host,
        script_list=line.get_js_dependencies()
    )
    return render(request, 'agent_score/show.html', context)

