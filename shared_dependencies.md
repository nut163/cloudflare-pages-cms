1. Shared Variables:
   - `app`: The Flask application instance, used across all Python files.
   - `db`: The SQLAlchemy database instance, used in `models.py`, `views.py`, `main.py`, and `tests.py`.

2. Data Schemas:
   - `Website`: The schema for a website, used in `models.py`, `views.py`, `main.py`, and `tests.py`.
   - `Page`: The schema for a page, used in `models.py`, `views.py`, `main.py`, and `tests.py`.
   - `Content`: The schema for a piece of content, used in `models.py`, `views.py`, `main.py`, and `tests.py`.

3. DOM Element IDs:
   - `navbar`: The navigation bar, used in `base.html`, `home.html`, `preview.html`, and `main.js`.
   - `content`: The content area, used in `base.html`, `home.html`, `preview.html`, and `main.js`.
   - `preview`: The preview area, used in `preview.html` and `main.js`.

4. Message Names:
   - `website_created`: A message sent when a website is created, used in `views.py` and `main.py`.
   - `page_added`: A message sent when a page is added, used in `views.py` and `main.py`.
   - `content_added`: A message sent when content is added, used in `views.py` and `main.py`.

5. Function Names:
   - `create_website()`: A function to create a new website, used in `views.py`, `main.py`, and `tests.py`.
   - `add_page()`: A function to add a new page, used in `views.py`, `main.py`, and `tests.py`.
   - `add_content()`: A function to add new content, used in `views.py`, `main.py`, and `tests.py`.
   - `preview_website()`: A function to preview a website, used in `views.py`, `main.py`, and `tests.py`.
   - `deploy_website()`: A function to deploy a website, used in `deploy.py` and `main.py`.