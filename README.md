# Youzertube_api

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.
The server fetches latest videos async after every 8 minutes and saves it to the database.


## Setup Guide
- Clone the project
- As this project is based on Django, your system need to have proper python setup, refer [this](https://www.python.org/downloads/)
- Go the project through the terminal and install all dependencies by using typing `pip install -r requirements.txt` in the terminal
- Inside the `setting.py` file, fill the variable `GOOGLE_API_KEYS` with all the API Keys available,the list should be filled as `['API_KEY_1','API_KEY_2',...]`
- For getting an API key follow [this](https://developers.google.com/youtube/v3/getting-started)
- Run the server using `python mange.py runserver`

