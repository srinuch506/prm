from itsdangerous import URLSafeTimedSerializer
from key import secret_key
def token(email,salt):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.dumps(email,salt=salt)
 