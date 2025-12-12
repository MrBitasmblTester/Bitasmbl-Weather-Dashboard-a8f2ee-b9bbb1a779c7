import os
class Settings:
    weather_api_key: str = os.getenv('WEATHER_API_KEY','')
settings = Settings()
