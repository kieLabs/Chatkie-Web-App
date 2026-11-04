# ChatKie Firebase configuration — paste locations

There are TWO different Firebase configurations. Do not mix them.

## A. Browser / Firebase Web App config (public)

File: `frontend/public/firebase-config.js`

Paste these values from Firebase Console → Project settings → General → Your apps → Web app config:
- `apiKey`
- `authDomain`
- `databaseURL` (Realtime Database URL; copy the exact URL shown in the console)
- `projectId`
- `storageBucket`
- `messagingSenderId`
- `appId`

Optional `CHATKIE_RECAPTCHA_SITE_KEY`: paste the reCAPTCHA v3 **site key** only. Leave empty if not configured. The site key is public; the reCAPTCHA secret key is not.

This config is sent to browsers, so it is not a place for passwords, private keys, or service-account JSON. Firebase Web API keys are identifiers, not authorization by themselves. Enforce access with Firebase Authentication, Realtime Database/Storage Security Rules, authorized domains and App Check.

## B. Firebase Admin / backend credentials (private)

File template: `backend/.env.example`

1. Copy it to `backend/.env` on your local machine/backend host.
2. In Firebase Console → Project settings → Service accounts, generate a service-account private key (JSON).
3. Copy `project_id` to `FIREBASE_PROJECT_ID`, `client_email` to `FIREBASE_CLIENT_EMAIL`, and `private_key` to `FIREBASE_PRIVATE_KEY`. Keep the private key line breaks as `\n` inside the quoted environment value if your host requires one-line values.
4. Set `FIREBASE_DATABASE_URL` and `FIREBASE_STORAGE_BUCKET` to the exact values for this project.
5. Set `CORS_ORIGINS` to the exact deployed frontend and Blogger origins. Avoid wildcard `*` in production.
6. Keep `backend/.env` out of Git. `.gitignore` excludes it. Configure the same variables in your backend hosting provider's environment-variable/secrets panel.

`backend/app/firebase_admin.py` contains Firebase Admin initialization and ID-token verification helpers. It is a helper module; the current FastAPI app does not yet use it to protect all routes or migrate the legacy Firebase matchmaking/room/WebRTC logic. Do not treat this as a completed backend migration.

## Never paste these into frontend/GitHub

- Firebase service-account JSON file
- `private_key` / `FIREBASE_PRIVATE_KEY`
- reCAPTCHA secret key
- TURN server credential/secret
- Any payment, email, AI or other private server API secret

If a private credential was ever committed or exposed, revoke/rotate it in its provider console. Deleting the file alone does not remove it from Git history.
