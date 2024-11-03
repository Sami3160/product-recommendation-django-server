from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import joblib
import sys
import json
# Create your views here.

def calculate_recommendation(req_data):
    data = pd.DataFrame(req_data)
    weights = {
        'likes': 0.5,
        'time_spent': 0.3,
        'num_visits': 0.2
    }

    # Apply feature engineering
    data['weighted_likes'] = data['liked'] * weights['likes']
    data['weighted_time_spent'] = data['view_time'] * weights['time_spent']
    data['weighted_num_visits'] = data['visit_count'] * weights['num_visits']

    data['interest_score'] = data['weighted_likes'] + data['weighted_time_spent'] + data['weighted_num_visits']
    model = joblib.load('/home/samiii/Documents/ml/HackEraRecommendation/django server tests/myserver/api/model.pkl')
    scaler = joblib.load('/home/samiii/Documents/ml/HackEraRecommendation/django server tests/myserver/api/scaler.pkl')
 
    # Load the scaler and model
    features = ['weighted_likes', 'weighted_time_spent', 'weighted_num_visits']
    X_user = data[features]
    X_user_scaled = scaler.transform(X_user)

    data['predicted_interest_score'] = model.predict(X_user_scaled)

    #sorting the data based on the score
    # print(top_products.to_json(orient='records'))
    top_products = data.sort_values(by='predicted_interest_score', ascending=False).head(10)[['product_id', 'product_name', 'predicted_interest_score']]
    return top_products.to_json(orient='records')



#logging output for debugging
class RecommendView(APIView):
    def get(self, request):
        data=request.data['product_data']
        # print(data)
        res=calculate_recommendation(data)
        return Response(json.loads(res), status=status.HTTP_200_OK)
