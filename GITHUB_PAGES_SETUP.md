# GitHub Pages Setup Guide

This guide explains how to set up GitHub Pages for this repository after it's published to GitHub.

## 🚀 Quick Setup

### 1. Publish Repository to GitHub
- Create a new repository on GitHub
- Push this code to the repository
- Make sure the repository is public (required for free GitHub Pages)

### 2. Enable GitHub Pages
1. Go to your repository on GitHub
2. Click on **Settings** tab
3. Scroll down to **Pages** section in the left sidebar
4. Under **Source**, select **Deploy from a branch**
5. Choose **Branch**: `main` (or your default branch)
6. Select **Folder**: `/docs`
7. Click **Save**

### 3. Update Configuration
After enabling GitHub Pages, update the following files with your actual GitHub username/organization:

#### Update `docs/_config.yml`:
Replace `[username]` with your actual GitHub username or organization name:

```yaml
url: "https://your-username.github.io"
baseurl: "/letscloud-openapi-gpt"

# Update GitHub links
url: "https://github.com/your-username/letscloud-openapi-gpt"
github: your-username/letscloud-openapi-gpt
```

#### Update `README.md`:
Replace the GitHub Pages URL in the documentation section:

```markdown
- **Live Documentation**: [View the interactive API docs](https://letscloud-community.github.io/letscloud-openapi-gpt/)
```

### 4. Access Your Documentation
After setup is complete, your documentation will be available at:
- **URL**: `https://letscloud-community.github.io/letscloud-openapi-gpt/`
- **Build Time**: Usually takes 5-10 minutes for the first build
- **Updates**: Automatically rebuilds when you push changes to the main branch

## 📋 What's Included

The GitHub Pages site includes:
- **Interactive API Documentation**: Swagger UI for testing endpoints
- **Complete API Reference**: All endpoints, schemas, and examples
- **Privacy Policy**: Legal compliance page
- **SEO Optimization**: Proper meta tags and sitemap
- **Responsive Design**: Works on desktop and mobile

## 🔧 Customization

### Changing the Repository Name
If you want to use a different repository name:
1. Update the `baseurl` in `docs/_config.yml`
2. Update all references in the documentation
3. Update the GitHub Pages folder path if needed

### Custom Domain
To use a custom domain:
1. Add a `CNAME` file in the `/docs` folder with your domain
2. Configure DNS settings to point to GitHub Pages
3. Update the `url` in `docs/_config.yml`

## 🐛 Troubleshooting

### Common Issues:
- **404 Error**: Make sure GitHub Pages is enabled and pointing to `/docs` folder
- **Build Fails**: Check that all files in `/docs` are valid
- **Styling Issues**: Ensure `_config.yml` is properly formatted
- **Links Broken**: Verify all URLs are updated with your actual username

### Check Build Status:
1. Go to **Actions** tab in your repository
2. Look for "pages build and deployment" workflow
3. Check for any error messages

## 📚 Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Custom Domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

## ✅ Verification

After setup, verify everything is working:
1. Visit your GitHub Pages URL
2. Test the interactive API documentation
3. Check that all links work correctly
4. Verify the site is mobile-responsive
5. Test the search functionality (if enabled)
