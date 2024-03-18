---
subtitle: Building resuable components in plain HTML using Jinja
date: 2022-11-17
tags:
  - python
---
Building sites with vanilla HTML can be a pain in the ass if you want to redesign an element that appears in every page, like a navigation bar or footer. Static site generators solve this problem with components, but I like reinventing the wheel. Jinja templating can be used to ape components since it is capable of passing arbitrary functions into its DOM templates.

```python
# ssg.py
def blog_footer():
    return """
    <footer>
      <p>
        <a href="/blog/feed.xml">Feed</a> -
        <a
          href="https://github.com/pavo-etc/pavo-etc.github.io/tree/master/generator"
          >ironprof</a
        >
      </p>
    </footer>"""

page_template = jinja2.Template(open("template.html", "r").read())
with open("output.html"), "w") as f:
    f.write(page_template.render({
        "blog_footer":blog_footer
    }))
```

```html
<!-- template.html -->
<!DOCTYPE html>
<html>
  <body>
    {{ blog_footer() }}
  </body>
</html>
```

```html
<!-- output.html -->
<!DOCTYPE html>
<html>
  <body>
    <footer>
      <p>
        <a href="/blog/feed.xml">Feed</a> -
        <a
          href="https://github.com/pavo-etc/pavo-etc.github.io/tree/master/generator"
          >ironprof</a
        >
      </p>
    </footer>
  </body>
</html>
```

This follows normal Python rules, so inheritance is followed and parameters can be passed into functions in the template.

```python
# components.py
def nav(activated_link):
    links = ["projects", "blog"]
    link_elements = []
    for link in links:
        is_active = ' activated-link' if activated_link == link else ''
        link_elements.append(f'        <a href="/{link}/" class="discrete-link{is_active}">{link.capitalize()}</a>')

    right_links_str = '\n'.join(link_elements)

    is_root_active = ' activated-link' if activated_link == '.' else ''
    return f"""
    <nav>
        <div class="flex">
        <div class="flex-left">
            <a href="/" class="discrete-link{is_root_active}">Zach Manson</a>
        </div>
        <div class="flex-right">
{right_links_str}
        </div>
        </div>
    </nav>"""

def blog_footer():
    return """
    <footer>
      <p>
        <a href="/blog/feed.xml">Feed</a> -
        <a
          href="https://github.com/pavo-etc/pavo-etc.github.io/tree/master/generator"
          >ironprof</a
        >
      </p>
    </footer>"""
```

```python
# ssg.py
import components

page_template = jinja2.Template(open("template.html", "r").read())
with open("output.html"), "w") as f:
    f.write(page_template.render({
        "components":components
    }))
```

```html
<!-- template.html -->
<!DOCTYPE html>
<html>
  <body>
    {{ components.nav("blog")}}

    <p>Lorem ipsum amirite</p>

    {{ components.blog_footer() }}
  </body>
</html>
```

```html
<!-- outputs.html -->
<!DOCTYPE html>
<html>
  <body>
    <nav>
      <div class="flex">
        <div class="flex-left">
          <a href="/" class="discrete-link">Zach Manson</a>
        </div>
        <div class="flex-right">
          <a href="/projects/" class="discrete-link">Projects</a>
          <a href="/blog/" class="discrete-link activated-link">Blog</a>
        </div>
      </div>
    </nav>

    <p>Lorem ipsum amirite</p>

    <footer>
      <p>
        <a href="/blog/feed.xml">Feed</a> -
        <a
          href="https://github.com/pavo-etc/pavo-etc.github.io/tree/master/generator"
          >ironprof</a
        >
      </p>
    </footer>
  </body>
</html>
```
