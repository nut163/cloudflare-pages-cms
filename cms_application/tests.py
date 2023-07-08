```python
import unittest
from cms_application import app, db
from cms_application.models import Website, Page, Content
from cms_application.views import create_website, add_page, add_content, preview_website

class TestCMSApplication(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_website(self):
        response = create_website('Test Website')
        self.assertEqual(response.status_code, 200)
        website = Website.query.filter_by(name='Test Website').first()
        self.assertIsNotNone(website)
        self.assertEqual(website.pages[0].label, 'Home')

    def test_add_page(self):
        create_website('Test Website')
        response = add_page('Test Website', 'About')
        self.assertEqual(response.status_code, 200)
        page = Page.query.filter_by(label='About').first()
        self.assertIsNotNone(page)

    def test_add_content(self):
        create_website('Test Website')
        add_page('Test Website', 'About')
        response = add_content('Test Website', 'About', 'Test Content', 'This is a test.', True, '2022-01-01', '2022-12-31')
        self.assertEqual(response.status_code, 200)
        content = Content.query.filter_by(title='Test Content').first()
        self.assertIsNotNone(content)

    def test_preview_website(self):
        create_website('Test Website')
        add_page('Test Website', 'About')
        add_content('Test Website', 'About', 'Test Content', 'This is a test.', True, '2022-01-01', '2022-12-31')
        response = preview_website('Test Website')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```