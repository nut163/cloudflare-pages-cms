from flask import render_template, redirect, url_for, flash, request
from cms_application import app, db
from cms_application.models import Website, Page, Content
from cms_application.forms import WebsiteForm, PageForm, ContentForm
from datetime import datetime

@app.route('/')
def home():
    websites = Website.query.all()
    return render_template('home.html', websites=websites)

@app.route('/create_website', methods=['GET', 'POST'])
def create_website():
    form = WebsiteForm()
    if form.validate_on_submit():
        new_website = Website(name=form.name.data)
        db.session.add(new_website)
        db.session.commit()
        flash('Website created', 'website_created')
        return redirect(url_for('home'))
    return render_template('create_website.html', form=form)

@app.route('/website/<int:website_id>', methods=['GET', 'POST'])
def manage_website(website_id):
    website = Website.query.get_or_404(website_id)
    form = PageForm()
    if form.validate_on_submit():
        new_page = Page(label=form.label.data, website_id=website.id)
        db.session.add(new_page)
        db.session.commit()
        flash('Page added', 'page_added')
        return redirect(url_for('manage_website', website_id=website.id))
    return render_template('manage_website.html', website=website, form=form)

@app.route('/page/<int:page_id>', methods=['GET', 'POST'])
def manage_page(page_id):
    page = Page.query.get_or_404(page_id)
    form = ContentForm()
    if form.validate_on_submit():
        new_content = Content(
            title=form.title.data,
            body=form.body.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            status=form.status.data,
            page_id=page.id
        )
        db.session.add(new_content)
        db.session.commit()
        flash('Content added', 'content_added')
        return redirect(url_for('manage_page', page_id=page.id))
    return render_template('manage_page.html', page=page, form=form)

@app.route('/preview/<int:website_id>')
def preview_website(website_id):
    website = Website.query.get_or_404(website_id)
    return render_template('preview.html', website=website)

@app.route('/content/<int:content_id>')
def view_content(content_id):
    content = Content.query.get_or_404(content_id)
    if content.start_date <= datetime.now() and (content.end_date is None or content.end_date > datetime.now()):
        return render_template('content.html', content=content)
    else:
        flash('Content is not currently active', 'error')
        return redirect(url_for('home'))