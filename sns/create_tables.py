import pandas as pd 
from .models import Comment
from django.http import HttpResponse, JsonResponse
import json
from django.utils import timezone

def fill_tables_from_csv(filename):
    df = pd.read_csv(filename)
    for index, row in df.iterrows():
        text = row['comment']
        perspective_score = row['perspective_score']
        toxicity_score = row['avg_toxic_score']
        author = row['author']
        pub_date = timezone.now()
        comment, created = Comment.objects.update_or_create(
            text = text,
            defaults = {
                'perspective_score': perspective_score,
                'toxicity_score': toxicity_score,
                'author': author,
                'pub_date': pub_date,
            }
        )    


def create_tables(request):
    fill_tables_from_csv("./main_comments.csv")
    fill_tables_from_csv("./nontoxic_comments.csv")

    response = {
        'message': 'Tables saved'
    }
    return HttpResponse(json.dumps(response), content_type='application/json')	