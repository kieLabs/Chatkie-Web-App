"""Optional Firebase Admin SDK bootstrap and ID-token verification helpers.

Set the FIREBASE_* variables in backend/.env. Never copy these values into the frontend.
"""
import os
import firebase_admin
from firebase_admin import auth, credentials


def get_firebase_app():
    if firebase_admin._apps:
        return firebase_admin.get_app()

    project_id = os.getenv("FIREBASE_PROJECT_ID", "").strip()
    client_email = os.getenv("FIREBASE_CLIENT_EMAIL", "").strip()
    private_key = os.getenv("FIREBASE_PRIVATE_KEY", "").replace("\\n", "\n").strip()

    if not (project_id and client_email and private_key):
        raise RuntimeError("Firebase Admin is not configured. Set FIREBASE_PROJECT_ID, FIREBASE_CLIENT_EMAIL and FIREBASE_PRIVATE_KEY in backend/.env")

    credential = credentials.Certificate({
        "type": "service_account",
        "project_id": project_id,
        "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID", ""),
        "private_key": private_key,
        "client_email": client_email,
        "client_id": os.getenv("FIREBASE_CLIENT_ID", ""),
        "token_uri": "https://oauth2.googleapis.com/token",
    })
    options = {}
    database_url = os.getenv("FIREBASE_DATABASE_URL", "").strip()
    storage_bucket = os.getenv("FIREBASE_STORAGE_BUCKET", "").strip()
    if database_url:
        options["databaseURL"] = database_url
    if storage_bucket:
        options["storageBucket"] = storage_bucket
    return firebase_admin.initialize_app(credential, options or None)


def verify_firebase_id_token(id_token: str):
    """Verify a Firebase Auth ID token and return its decoded claims."""
    get_firebase_app()
    return auth.verify_id_token(id_token, check_revoked=True)
