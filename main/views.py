from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, permissions
from .models import * 
from .serializers import *
from .forms import * 
from django.db.models import Q
from django.contrib.auth import authenticate, get_user_model, login, logout
from  django.contrib.auth.models import User, auth
from hashlib import sha256
# machine learning model 1
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


def send_mail(bod, email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('madrixgaming2001@gmail.com', 'lpdzdfdsrgmaocou')

    subject = 'Amazon Price Tracker from Madrix'
    body = bod
    msg = "Recommandations from TWTCS"
    server.sendmail(
        'madrixgaming2001@gmail.com',
        email,
        msg,
    )
    print("#############")
    server.quit

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
## end of model

links_small = pd.read_csv('main/links_small.csv')
links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')
md = md.drop([19730, 29503, 35587]) 
md['id'] = md['id'].astype('int')
smd = md[md['id'].isin(links_small)]
smd['tagline'] = smd['tagline'].fillna('')
smd['description'] = smd['overview'] + smd['tagline']
smd['description'] = smd['description'].fillna('')
tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(smd['description'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
smd = smd.reset_index()
titles = smd['title']
indices = pd.Series(smd.index, index=smd['title'])


def get_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    #sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]


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
            a = build_chart(y).head(10)
            col_title = list(a.title)
            json_title = json.dumps(col_title)
            print(json_title)
            #send_mail(col_title, email)
            print(y)
            return JsonResponse(col_title, safe=False)
    else:
        form = GenreForm()
    return JsonResponse("{'message: genre'}", safe=False)


def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            print(search)
            u = Search(search=search)
            u.save()
            a = get_recommendations(search)
            col_title = list(a)
            json_title = json.dumps(col_title)
            json_title = json.loads(json_title)
            print(json_title)
            #send_mail(col_title, email)
            return JsonResponse(json_title, safe=False)
    else:
        form = SearchForm()
    return JsonResponse("{'message': 'search'}", safe=False)
