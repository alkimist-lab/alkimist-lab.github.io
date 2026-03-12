# Alkimist Lab Website

This is the source code for the Alkimist Lab website, built with [Pelican](https://getpelican.com/), a static site generator written in Python.

## Prerequisites

- Python 3.8 or higher
- pip

## Local Development

1. Clone this repository:
   ```bash
   git clone https://github.com/alkimist-lab/alkimist-lab.github.io.git
   cd alkimist-lab.github.io
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Generate the site:
   ```bash
   pelican content
   ```

4. Run the development server:
   ```bash
   pelican --listen
   ```

5. Visit `http://localhost:8000` in your browser.

## Project Structure

```
.
├── content/              # Markdown content files
│   ├── events/          # Event listings
│   ├── shop/            # Shop items
│   ├── pages/           # Static pages
│   └── images/          # Images and media
├── output/              # Generated site (git-ignored)
├── themes/              # Custom themes
├── pelicanconf.py       # Development configuration
├── publishconf.py       # Production configuration
├── requirements.txt     # Python dependencies
└── Makefile            # Build automation
```

## Writing Content

### Events

Create a new Markdown file in the `content/events/` directory:

```markdown
Title: Your Event Title
Date: 2024-03-12 18:00
Category: Events
Tags: workshop, event-type
Slug: your-event-slug
Authors: Alkimist Lab
Summary: Brief summary of your event

# Your event content here
```

### Shop Items

Create a new Markdown file in the `content/shop/` directory:

```markdown
Title: Your Item Name
Date: 2024-03-12 10:00
Category: Shop
Tags: category, type
Slug: your-item-slug
Authors: Alkimist Lab
Summary: Brief description of your item

# Your item details here
```

### Pages

Create a new Markdown file in the `content/pages/` directory:

```markdown
Title: Page Title
Date: 2024-03-12
Slug: page-slug

# Your page content here
```

## Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch using GitHub Actions.

## Links

- [Instagram](https://www.instagram.com/alkimist_lab)

## License

MIT License
