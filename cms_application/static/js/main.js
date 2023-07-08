document.addEventListener('DOMContentLoaded', (event) => {
    const navbar = document.getElementById('navbar');
    const content = document.getElementById('content');
    const preview = document.getElementById('preview');

    function updateNavbar(pages) {
        navbar.innerHTML = '';
        pages.forEach(page => {
            const li = document.createElement('li');
            li.textContent = page.label;
            li.addEventListener('click', () => loadPage(page));
            navbar.appendChild(li);
        });
    }

    function loadPage(page) {
        fetch(`/api/pages/${page.id}`)
            .then(response => response.json())
            .then(data => {
                content.innerHTML = '';
                data.contents.forEach(contentItem => {
                    if (contentItem.active && new Date(contentItem.start_date) <= new Date() && (contentItem.end_date === null || new Date(contentItem.end_date) > new Date())) {
                        const h1 = document.createElement('h1');
                        h1.textContent = contentItem.title;
                        content.appendChild(h1);
                        const div = document.createElement('div');
                        div.innerHTML = contentItem.body;
                        content.appendChild(div);
                    }
                });
            });
    }

    function previewWebsite() {
        fetch('/api/preview')
            .then(response => response.json())
            .then(data => {
                preview.innerHTML = '';
                const iframe = document.createElement('iframe');
                iframe.srcdoc = data.html;
                preview.appendChild(iframe);
            });
    }

    fetch('/api/websites')
        .then(response => response.json())
        .then(data => {
            updateNavbar(data.pages);
            if (data.pages.length > 0) {
                loadPage(data.pages[0]);
            }
        });

    document.getElementById('preview-button').addEventListener('click', previewWebsite);
});