from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, permissions
from .models import * 
from .serializers import *
from .forms import *
from django.db.models import Q
import pandas as pd 
import numpy as np
import seaborn as sns
from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
import json
import warnings; warnings.simplefilter('ignore')


md = pd.read_csv('main/movies_metadata.csv')
md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x:[i['name'] for i in x] if isinstance(x, list) else[])
vote_counts = md[md['vote_count'].notnull()]['vote_count'].astype('int')
vote_averages = md[md['vote_average'].notnull()]['vote_average'].astype('int')
md['year'] = pd.to_datetime(md['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
s = md.apply(lambda x: pd.Series(x['genres']), axis=1).stack().reset_index(level=1, drop=True)
s.name = 'genre'
gen_md = md.drop('genres', axis=1).join(s)
def build_chart(genre, no=0, percentile=0.85):
    df = gen_md[gen_md['genre']== genre[0]]
    if no is not 0:
        
        for a in (no-1):
            df.append(gen_md[gen_md['genre'] == genre[a]])
    
    vote_counts = df[df['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = df[df['vote_average'].notnull()]['vote_average'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(percentile)
    
    qualified = df[(df['vote_count'] >= m) & (df['vote_count'].notnull()) & (df['vote_average'].notnull())][['title', 'year', 'vote_count', 'vote_average', 'popularity']]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    qualified['wr'] = qualified.apply(lambda x: (x['vote_count']/(x['vote_count'] + m) * x['vote_average']) + (m/(m + x['vote_count']) * C), axis=1)
    qualified = qualified.sort_values('wr', ascending=True).head(250)
    return qualified



class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerailizers
    permission_class = (permissions.IsAuthenticatedOrReadOnly)


def home(request):
    return JsonResponse("{'page':'home'}", safe=False)


def user_form(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            adventure = form.cleaned_data['adventure']
            horror = form.cleaned_data['horror']
            crime = form.cleaned_data['crime']
            romance = form.cleaned_data['romance']
            family = form.cleaned_data['family']
            fantasy = form.cleaned_data['fantasy']
            comedy = form.cleaned_data['comedy']
            thriller = form.cleaned_data['thriller']
            action = form.cleaned_data['action']
            drama = form.cleaned_data['drama']
            animation = form.cleaned_data['animation']
            x = [("Adventure", adventure), ("Horror", horror), ("Crime", crime), ("Romance", romance), ("Family", family), ("Fantasy", fantasy), ("Comedy", comedy), ("Thriller", thriller), ("Action", action), ("Drama", drama), ("Animation", animation)]
            u = Genre(name=name, adventure=adventure, horror=horror, crime=crime, romance=romance, family=family, fantasy=fantasy, comedy=comedy, thriller=thriller, action=action, drama=drama, animation=animation)
            y = []
            for i in range(len(x)):
                if x[i][1] == True: 
                    y.append(x[i][0])
            u.save()
            a = build_chart(y).head(20)
            out = a['title']
            j_out = json.dump(a['title'])
            print(j_out)

    else:
        form = GenreForm()
    return render(request, 'main/form.html' ,{
        'form':form
    })#JsonResponse("{'page': 'form'}", safe=False)
