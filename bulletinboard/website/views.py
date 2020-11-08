from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from .models import Announcement
from .forms import AnnouncementForm, PersonForm
import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt
import random
import plotly.offline as opy

# Create your views here.

# def add_announcement(request):
#     if request.method == "POST":
#         form = AnnouncementForm(request.POST)
#         if form.is_valid():
#             announcement = form.save(commit=False)
#             announcement.save()
#         else:
#             return render(request, "tasks/add.html", {
#                 "form": form
#             })
#     else:
#         return render(request, "website/index.html", {
#             "announcements": Announcement.objects.all()
#         })


def index(request):
    return render(request, "website/index.html", {
        "anouncements": Announcement.objects.all()
    })


def make_edge(x, y):
    return  go.Scatter(x         = x,
                       y         = y,
                       line      = dict(color = 'black'),
                       mode      = 'lines')

def contact(request):
    #context = {'graph': graph}
    # added code HttpResponseRedirect
    if request.method == "POST":
        person_form = PersonForm(request.POST)
        if person_form.is_valid():
            if Person.objects.filter(name = request.POST.get("name")).exists():
                knownPerson = Person.objects.get(name = request.POST.get("name"))
                knownPerson.delete()
                person = person_form.save()
            else:
                person = person_form.save()
    G = nx.Graph()
    #first add people list as nodes
    all_people = list(Person.objects.all())
    for p in all_people:
        G.add_node(str(p))

    for person in all_people:
        temp = Person.objects.get(name=person)
        friends = list(temp.get_friends())
        name = str(temp)
        print("here is temp: " + name)
        for f in friends:
            print("here is f: " + str(f))
            their_friend = str(f) + ""
            G.add_edge(name, their_friend)

    pos_ = nx.spring_layout(G)

    edge_trace = []
    for edge in G.edges():
        char_1 = edge[0]
        char_2 = edge[1]
        x0, y0 = pos_[char_1]
        x1, y1 = pos_[char_2]
        trace  = make_edge([x0, x1, None], [y0, y1, None])
        edge_trace.append(trace)


    node_trace = go.Scatter(x         = [],
                            y         = [],
                            text      = [],
                            textposition = "top center",
                            textfont_size = 20,
                            mode      = 'markers+text',
                            hoverinfo = 'none',
                            marker    = dict(showscale=False,
                                             color = list(range(len(G.nodes()))),
                                             colorscale='Blackbody',
                                             size = 20,
                                             line  = None))

    for node in G.nodes():
        x, y = pos_[node]
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])
        node_trace['marker']['color'] += tuple(['black'])
        node_trace['text'] += tuple(['<b>' + node + '</b>'])

    layout = go.Layout(
        title='<br>This is our close contacts circle :)</br>',
        font_color="black",
        title_x=0.5,
        titlefont_size=20,
        width=700,
        height=600,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))

    fig = go.Figure(layout = layout)

    for trace in edge_trace:
        fig.add_trace(trace)

    fig.add_trace(node_trace)

    fig.update_layout(showlegend = False)

    graph = fig.to_html(full_html=False, default_height=500, default_width=500)
    context = {'person_form': PersonForm(),'graph': graph }
    return render(request, "website/contact.html", context)

    #simon = Person.objects.get(name= "Simon")
    #print(simon.get_friends())
    #jiaqi = Person.objects.get(name= "Jiaqi")
    #print(jiaqi.get_friends())
