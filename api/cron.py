import os
from apiclient.discovery import build
import apiclient
from .models import *
from youtube_fetch_api import settings
from datetime import datetime, timedelta


def do():
    apiKeys = settings.GOOGLE_API_KEYS
    time_now = datetime.now()
    last_request_time = time_now - timedelta(minutes=8) # run after 8 minutes 
    valid = False # checking of valid api keys

    for apiKey in apiKeys:
        try:
            youtube = build("youtube", "v3", developerKey=apiKey)
            req = youtube.search().list(q="music", part="snippet", order="date", maxResults=30,
                                        publishedAfter=(last_request_time.replace(microsecond=0).isoformat()+'Z'))
            res = req.execute()
            valid = True
        except apiclient.errors.HttpError as err:
            code = err.resp.status
            if not(code == 400 or code == 403):
                break

        if valid:
            break

    if valid: # if valid api creating an object in database.

        for item in res['items']:
            video_id = item['id']['videoId']
            publishedDateTime = item['snippet']['publishedAt']
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnailsUrls = item['snippet']['thumbnails']['default']['url']
            channel_id = item['snippet']['channelId']
            channel_title = item['snippet']['channelTitle']
            Videos.objects.create(
                video_id=video_id,
                title=title,
                description=description,
                channel_id=channel_id,
                channel_title=channel_title,
                publishedDateTime=publishedDateTime,
                thumbnailsUrls=thumbnailsUrls,
            )
