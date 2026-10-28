# Hostinger PHP/HTML hosting

This React frontend builds to static files. No Node.js hosting slot or PHP rewrite is needed. An active web hosting plan with a free website slot is required; domain registration alone is insufficient.

1. hPanel → Websites → Create website → PHP/HTML website. Choose your purchased domain.
2. Dashboard → Advanced → Git → Connect with GitHub. Grant access to PrajaktaAdlytica/RoleProgress.
3. Choose branch `hostinger`, deploy directory `public_html`, then Deploy. Back up any existing files before replacing them. The source branch `main` is NOT deployable directly through this feature because generic Git hosting does not run builds.
4. Use hPanel’s domain connection instructions if DNS is not already connected. Use the exact nameservers/IP displayed for this hosting account; preserve mail records.
5. Enable SSL/HTTPS. Test homepage and directly refresh /products/skills-review, /demo and /request-demo.

The hostinger branch contains only built public files and .htaccess for route refreshes. Source and creative files remain on main. For future changes run npm ci, npm run build, npm run test:sites, then publish dist/client contents to hostinger. Hostinger auto-deploy can track that branch.

Manual alternative: upload the contents of the supplied Hostinger ZIP into public_html and extract. index.html and .htaccess must be directly inside public_html, not a nested directory. Do not upload node_modules, source, or dist/server.

Forms and sign-in remain concept previews; hosting does not add email delivery, authentication, a database, or real hiring features. The intro deliverables are still images/prompts, not a rendered video.

References: https://docs.hostinger.com/websites/git and https://docs.hostinger.com/getting-started/creating-your-first-website
