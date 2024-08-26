from rest_framework.decorators import api_view
from django.http import JsonResponse
from youtube_transcript_api import YouTubeTranscriptApi

@api_view(['POST'])
def orchestrator(request):
    print(request.data)
    #url = 'https://www.youtube.com/watch?v=Kjt_EDgFlkk'
    url = request.data['link']
    code_id = url.rsplit("=")[-1]

    print(code_id)

    d = YouTubeTranscriptApi.get_transcript(code_id)
    return JsonResponse(d, status=200, safe=False)