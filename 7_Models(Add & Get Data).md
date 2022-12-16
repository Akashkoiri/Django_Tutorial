##
---
### We have to create a diffrent directory for user media files

```py
# Settings.py
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

```py
# urls.py
urlpatterns = [
	...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

