import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Google Service Account Credentials
    TYPE: str = os.getenv("type")
    PROJECT_ID: str = os.getenv("project_id")
    PRIVATE_KEY_ID: str = os.getenv("private_key_id")
    PRIVATE_KEY: str = os.getenv("private_key", "").replace('\\n', '\n')
    CLIENT_EMAIL: str = os.getenv("client_email")
    CLIENT_ID: str = os.getenv("client_id")
    AUTH_URI: str = os.getenv("auth_uri")
    TOKEN_URI: str = os.getenv("token_uri")
    AUTH_PROVIDER_CERT_URL: str = os.getenv("auth_provider_x509_cert_url")
    CLIENT_CERT_URL: str = os.getenv("client_x509_cert_url")
    UNIVERSE_DOMAIN: str = os.getenv("universe_domain")
    
    # Document AI Settings
    DOC_AI_PROJECT_ID: str = os.getenv("DOC_AI_PROJECT_ID")
    PROJECT_LOCATION: str = os.getenv("PROJECT_LOCATION")
    FRONT_NATIONAL_ID_API_ENDPOINT: str = os.getenv("FRONT_NATIONAL_ID_API_ENDPOINT")
    FRONT_NATIONAL_ID_PROCESSOR_ID: str = os.getenv("FRONT_NATIONAL_ID_PROCESSOR_ID")
    REAR_NATIONAL_ID_API_ENDPOINT: str = os.getenv("REAR_NATIONAL_ID_API_ENDPOINT")
    REAR_NATIONAL_ID_PROCESSOR_ID: str = os.getenv("REAR_NATIONAL_ID_PROCESSOR_ID")
    
    @classmethod
    def get_credentials_dict(cls) -> dict:
        """Returns the Google credentials as a dictionary"""
        return {
            "type": cls.TYPE,
            "project_id": cls.PROJECT_ID,
            "private_key_id": cls.PRIVATE_KEY_ID,
            "private_key": cls.PRIVATE_KEY,
            "client_email": cls.CLIENT_EMAIL,
            "client_id": cls.CLIENT_ID,
            "auth_uri": cls.AUTH_URI,
            "token_uri": cls.TOKEN_URI,
            "auth_provider_x509_cert_url": cls.AUTH_PROVIDER_CERT_URL,
            "client_x509_cert_url": cls.CLIENT_CERT_URL,
            "universe_domain": cls.UNIVERSE_DOMAIN
        }

settings = Settings()
