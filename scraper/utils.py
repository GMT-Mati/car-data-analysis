import hashlib
import os

# This code defines some utility functions for caching the HTML of the Otomoto website's search results pages.
# The generate_hash function generates an MD5 hash of a URL,
# which is used as the filename for the cached HTML.
# The get_cache_filename function generates the full path to the cache file for a given URL.
# The save_to_cache function saves the HTML of a URL to a cache file,
# and the load_from_cache function loads the HTML from a cache file if it exists.#
# You can use these functions to avoid sending requests to the Otomoto website for pages that have already been visited,
# which can save time and reduce the risk of being blocked by the website.


def generate_hash(url):
    """Generate a hash of the URL"""
    return hashlib.md5(url.encode()).hexdigest()


def get_cache_filename(url):
    """Generate a filename for caching the HTML of the given URL"""
    cache_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'cache')
    os.makedirs(cache_folder, exist_ok=True)
    return os.path.join(cache_folder, generate_hash(url))


def save_to_cache(url, html):
    """Save the HTML of the given URL to a cache file"""
    filename = get_cache_filename(url)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


def load_from_cache(url):
    """Load the HTML of the given URL from a cache file, if it exists"""
    filename = get_cache_filename(url)
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return None
