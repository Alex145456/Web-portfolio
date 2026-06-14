# Flet Web Portfolio

This is a complete Flet portfolio scaffold for a graded engineering project portfolio. It includes:

- Project Timeline
- MATLAB Achievement Hub
- Technical Blog with formulas and video inserts
- GitHub Evidence page

## Folder Structure

```text
portfolio-flet/
  main.py
  requirements.txt
  README.md
  components/
    __init__.py
    navigation.py
    section.py
  pages/
    __init__.py
    timeline.py
    matlab_hub.py
    blog.py
    github_evidence.py
  assets/
    certificates/
      README.md
    github/
      README.md
    videos/
      README.md
```

## Run Locally

1. Open this folder in VS Code.
2. Create a virtual environment:

```powershell
python -m venv .venv
```

3. Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Install dependencies:

```powershell
pip install -r requirements.txt
```

5. Run the app for web:

```powershell
flet run --web
```

## Add Your Evidence

- Your supplied portrait is stored as `assets/profile/portrait.jpeg`.
- Your supplied MATLAB certificate PDFs are stored in `assets/certificates/` and linked from the MATLAB Achievement Hub.
- Add the remaining MATLAB certificate or badge files in `assets/certificates/`.
- Put GitHub screenshots in `assets/github/`.
- Put local video files in `assets/videos/`, or replace the sample video URLs in `pages/blog.py`.
- Replace placeholder text with your real weekly logs, commit links, pull request details, and engineering impact narrative.

## Deploy

Common deployment options:

1. **Flet build for static hosting**

```powershell
flet build web
```

Upload the generated web build output to your hosting provider if your project setup supports static hosting.

2. **Render/Railway/Fly.io style Python host**

Use this command as the web start command:

```powershell
flet run --web --port $PORT main.py
```

3. **VS Code workflow**

Open the integrated terminal, activate your virtual environment, install requirements, then run:

```powershell
flet run --web main.py
```
