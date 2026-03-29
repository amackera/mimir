from mimir.tools.github import read_github_file, search_github
from mimir.tools.google_docs import read_google_doc, search_google_docs

all_tools = [
    search_github,
    read_github_file,
    search_google_docs,
    read_google_doc,
]
