from textwrap import dedent
import urllib.parse

x_intent = "https://x.com/intent/tweet"
fb_sharer = "https://www.facebook.com/sharer/sharer.php"
linkedin_sharer = "https://www.linkedin.com/sharing/share-offsite/"

def on_page_markdown(markdown, **kwargs):
    page = kwargs["page"]
    config = kwargs["config"]

    if page.meta.get("template") != "blog-post.html":
        return markdown

    page_url = urllib.parse.quote(
        config.site_url.rstrip("/") + "/" + page.url.lstrip("/")
    )
    page_title = urllib.parse.quote(page.title)

    return markdown + dedent(f"""
    <div class="social-share">
        <h3>Share this post</h3>

        <div class="social-share-buttons">
            <a href="{x_intent}?text={page_title}&url={page_url}"
               target="_blank"
               rel="noopener noreferrer"
               class="share-btn">
                𝕏 / Twitter
            </a>

            <a href="{fb_sharer}?u={page_url}"
               target="_blank"
               rel="noopener noreferrer"
               class="share-btn">
                Facebook
            </a>

            <a href="{linkedin_sharer}?url={page_url}"
               target="_blank"
               rel="noopener noreferrer"
               class="share-btn">
                LinkedIn
            </a>
        </div>
    </div>
    """)