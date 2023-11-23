# frontend/templatetags/vite_assets.py
import json
from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()

@register.simple_tag(name="vite_assets")
def vite_assets(asset_name):  # Function name changed to 'vite_asset'
    # if settings.DEBUG:
        # return f"http://localhost:3000/{asset_name}"  # Uncomment this if you want to use Vite's dev server in DEBUG mode
    
    manifest_path = settings.BASE_DIR / 'frontend/static/frontend/manifest.json'
    with open(manifest_path, 'r') as manifest_file:
        manifest = json.load(manifest_file)
    if asset_name in manifest:
        return static(f"frontend/{manifest[asset_name]['file']}")
    return static(f"frontend/{asset_name}")