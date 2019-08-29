Title: Changing of the theme
Slug: changing-of-the-theme
Date: 2019-08-29 13:46:00

Not that any of you really care all that much, but I've changed over from the pelican-bootstrap3 (with darkly) to the "chunk" theme. Although, I did have to make one small change in order for the "pages" to actually work:

From (line 41 - base.html)
```python
{% endfor %}
  {% for p in PAGES %}
	<li{% if p == page %} class="active"{% endif %} class="menu-item menu-item-type-post_type 	menu-item-object-page"><a href="{{ SITEURL }}/{{ p.url }}">{{ p.title }}</a></li>
```

To (note the lowercase PAGES)
```python
{% endfor %}
  {% for p in pages %}
	<li{% if p == page %} class="active"{% endif %} class="menu-item menu-item-type-post_type 	menu-item-object-page"><a href="{{ SITEURL }}/{{ p.url }}">{{ p.title }}</a></li>
```
So far so good.