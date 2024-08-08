class Config:
    def get_token():
        import os
        from dotenv import load_dotenv

        load_dotenv()

        TOKEN = os.getenv("token_bot")
        return TOKEN