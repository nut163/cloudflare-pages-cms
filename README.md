# CMS Application

This is an open-source CMS application that can be used to manage content on multiple websites. 

## Features

- Create a new website with a default "Home" page.
- Add pages with labels to the created websites.
- Add content to the pages with an active status (enabled or disabled), a title, display start date and end date, and body details.
- Insert HTML or JS into the body details section.
- Preview the website after saving.
- Deploy the application using Cloudflare Pages.

## Setup

1. Clone the repository to your local machine.
2. Navigate to the project directory `cd cms_application`.
3. Install the required dependencies with `pip install -r requirements.txt`.

## Usage

1. Run the application with `python main.py`.
2. Access the application on your local server.

## Testing

Run the tests with `python -m unittest tests.py`.

## Deployment

This application can be deployed using Cloudflare Pages. Follow the steps below:

1. Push your changes to your GitHub repository.
2. Log in to your Cloudflare account and go to the Pages dashboard.
3. Click on 'Create a project'.
4. Select the repository you want to deploy.
5. In the 'Build settings', set the 'Build command' to `python setup.py` and 'Build output' to `/`.
6. Click on 'Begin setup' and then 'Save and Deploy'.

Your application is now live on Cloudflare Pages!