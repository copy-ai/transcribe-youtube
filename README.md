# Run the App Locally

- cd copyai
- pip install -r requirements.txt
- edit copyai/settings.py
  - add `localhost` to `ALLOWED_HOSTS`
  - set `DEBUG = True`
- python3 manage.py runserver 0.0.0.0:5000 (or any port)

# Use Postman / Insomnia to Test

Set content type and send a YT short-code or a full YT URL as the payload

```
POST http://localhost:5000/text
Content-Type: application/json

{
	"link": "Kjt_EDgFlkk"
}
```

# Restart Heroku

`heroku restart -a copy-ai-yt-transcriber`

# Tail Heroku Logs

`heroku logs -t -a copy-ai-yt-transcriber`
