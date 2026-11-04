# Chatkie — Next.js + Python migration package

This package is a **compatibility-first migration** of the supplied Blogger Chatkie template. The existing Chatkie interface and browser-side features are preserved in `frontend/public/legacy.html`, served inside a Next.js application. A separate FastAPI service is included as the starting point for moving server responsibilities in controlled stages.

## Important status and limitations

- The supplied document contains Blogger XML/HTML and a large browser-side JavaScript application, not a source repository with separated modules.
- Firebase configuration in the supplied file is placeholder text (`YOUR_ACTUAL_API_KEY`, etc.). Add your Firebase Web App values in `frontend/public/firebase-config.js`. Keep Firebase Admin service-account credentials in `backend/.env` only. Firebase web config is public client configuration; protect data with Firebase Security Rules and App Check. See `FIREBASE-SETUP.md` for the exact paste locations.
- Existing browser-side Firebase Realtime Database, Firebase Auth, and direct WebRTC flows are preserved for compatibility. They have **not** yet been rewritten into Python endpoints. The FastAPI service currently provides health endpoints and a WebSocket connectivity test only.
- Real stranger video calls across restrictive networks may require a properly configured TURN server. Browser camera/microphone access requires HTTPS (except localhost).
- This package does not claim production readiness. Test authentication, database rules, room access, reporting/blocking, account deletion, camera permissions, and WebRTC on staging before public launch.

## Run locally

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Open http://localhost:3000. The Next.js page loads `/legacy.html` in a full-screen iframe.

### Python backend (separate terminal)
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Health check: http://localhost:8000/health

## GitHub deployment

1. Create a GitHub repository named `chatkie`.
2. Upload the contents of this ZIP (the `frontend`, `backend`, `blogger`, README and .gitignore folders/files) to the repository root.
3. Deploy `frontend` to a Next.js-capable host. Because `output: export` is enabled, it can also be built as static files (`cd frontend && npm install && npm run build`); publish the generated `frontend/out` directory to static hosting or GitHub Pages.
4. Deploy `backend` separately to a Python ASGI host if/when you start using its API. GitHub Pages cannot run Python/FastAPI.
5. Set the actual Firebase web config in `frontend/public/firebase-config.js`; set private Admin credentials in backend host environment variables (local template: `backend/.env.example` copied to `.env`). Verify Firebase authorized domains, Security Rules and App Check, then redeploy.
6. Replace `YOUR-CHATKIE-FRONTEND-DOMAIN` in `blogger/chatkie-iframe.html` with the deployed frontend URL and paste that snippet into Blogger HTML.

## Next migration stage

The next engineering stage is to split the legacy browser code into React components and services, then migrate matchmaking/room coordination to FastAPI + a persistent store. Keep Firebase Auth identity verification and WebRTC signaling security explicit; do not simply expose privileged Firebase credentials in the browser.
