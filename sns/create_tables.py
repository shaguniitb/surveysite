import pandas as pd 
from .models import Comment
from django.http import HttpResponse, JsonResponse
import json
from django.utils import timezone

def fill_tables_from_csv(filename):
    df = pd.read_csv(filename)
    df = df.sample(frac=1)
    for index, row in df.iterrows():
        text = row['comment']
        toxicity_score = row['avg_toxic_score']
        author = row['author']
        author_name = row['author_name']
        pub_date = row['pub_date']
        num_likes = row['num_likes']
        num_comments = row['num_comments']
        num_retweets = row['num_retweets']
        comment, created = Comment.objects.update_or_create(
            text = text,
            author_name = author_name,
            num_likes = num_likes,
            num_comments = num_comments,
            num_retweets = num_retweets,
            pub_date = pub_date,
            toxicity_score = toxicity_score,
            defaults = {
                'author': author,
                'text': text,
            }
        )    


def create_tables(request):
    fill_tables_from_csv("./main_comments.csv")
    fill_tables_from_csv("./nontoxic_comments.csv")

    response = {
        'message': 'Tables saved'
    }
    return HttpResponse(json.dumps(response), content_type='application/json')	