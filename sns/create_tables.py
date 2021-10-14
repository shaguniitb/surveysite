import pandas as pd 
from .models import Comment
from django.http import HttpResponse, JsonResponse
import json
from django.utils import timezone


def create_tables(request):
    df = pd.read_csv("./input.csv")
    for index, row in df.iterrows():
        text = row['comment']
        perspective_score = row['perspective_score']
        toxicity_score = row['avg_rating']
        author = 'tester'
        pub_date = timezone.now()
        print (perspective_score)
        comment, created = Comment.objects.update_or_create(
            text = text,
            defaults = {
                'perspective_score': perspective_score,
                'toxicity_score': toxicity_score,
                'author': author,
                'pub_date': pub_date,
            }
        )

    response = {
        'message': 'Tables saved'
    }
    return HttpResponse(json.dumps(response), content_type='application/json')	