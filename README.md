# Mudzi RDC website

Run the Flask site with:

```powershell
.\venv\Scripts\python run.py
```

Then visit `http://127.0.0.1:5000`.

## Add the council logo

1. Create `app/static/images/logo/` if it does not exist.
2. Put your logo file there and name it `mudzi-rdc-logo.png` **or** update the filename in `app/templates/public/index.html`.
3. For the best result, use a square transparent PNG at least 256 × 256 pixels.

The logo is used in the header. The footer currently uses the text mark `MR`; replace it with the same image when you are happy with the main logo.

## Add the page photographs

The layout reserves these optional local files:

- `app/static/images/hero/mudzi-landscape.jpg`
- `app/static/images/news/roads-project.jpg`

If they are missing, the page remains readable and displays its green fallback background.
