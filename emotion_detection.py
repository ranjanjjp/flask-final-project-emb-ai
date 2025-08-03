import requests
import json
 
def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # If the API call is successful
    if response.status_code == 200:
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

        # Extract individual emotions
        anger = emotion_scores.get('anger', 0)
        disgust = emotion_scores.get('disgust', 0)
        fear = emotion_scores.get('fear', 0)
        joy = emotion_scores.get('joy', 0)
        sadness = emotion_scores.get('sadness', 0)

        # Find dominant emotion
        emotions = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotions, key=emotions.get)

        # Return the result
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

    else:
        # Handle failure or unexpected response
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }