```python
from datetime import datetime

def is_active(content):
    """
    Check if a piece of content is active.
    """
    now = datetime.now()
    return content.active_status == 'enabled' and content.display_start_date <= now and (content.display_end_date is None or content.display_end_date > now)

def filter_active_contents(contents):
    """
    Filter the active contents from a list of contents.
    """
    return [content for content in contents if is_active(content)]

def get_navbar_pages(website):
    """
    Get the pages to be displayed in the navbar.
    """
    return website.pages

def get_page_contents(page):
    """
    Get the contents of a page.
    """
    return filter_active_contents(page.contents)

def get_content_display(content):
    """
    Get the display of a piece of content.
    """
    return {
        'title': content.title,
        'body': content.body_details
    }
```