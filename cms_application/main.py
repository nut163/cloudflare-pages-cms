```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from cms_application.models import Website, Page, Content
from cms_application.forms import WebsiteForm, PageForm, ContentForm
from cms_application.utils import current_time, is_active_content
from cms_application.deploy import deploy_website

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def create_website():
    form = WebsiteForm(request.form)
    if request.method == 'POST' and form.validate():
        website = Website(label=form.label.data)
        db.session.add(website)
        db.session.commit()
        return redirect(url_for('add_page', website_id=website.id))
    return render_template('home.html', form=form)

@app.route('/website/<int:website_id>/page', methods=['GET', 'POST'])
def add_page(website_id):
    form = PageForm(request.form)
    if request.method == 'POST' and form.validate():
        page = Page(label=form.label.data, website_id=website_id)
        db.session.add(page)
        db.session.commit()
        return redirect(url_for('add_content', page_id=page.id))
    return render_template('add_page.html', form=form)

@app.route('/page/<int:page_id>/content', methods=['GET', 'POST'])
def add_content(page_id):
    form = ContentForm(request.form)
    if request.method == 'POST' and form.validate():
        content = Content(
            title=form.title.data,
            body=form.body.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            active_status=form.active_status.data,
            page_id=page_id
        )
        db.session.add(content)
        db.session.commit()
        return redirect(url_for('preview_website', website_id=content.page.website_id))
    return render_template('add_content.html', form=form)

@app.route('/website/<int:website_id>/preview')
def preview_website(website_id):
    website = Website.query.get(website_id)
    return render_template('preview.html', website=website)

@app.route('/website/<int:website_id>/deploy')
def deploy(website_id):
    website = Website.query.get(website_id)
    deploy_website(website)
    return redirect(url_for('preview_website', website_id=website.id))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```