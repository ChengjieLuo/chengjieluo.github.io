import bibtexparser
import re

# LaTeX special character mapping
LATEX_TO_UNICODE = {
    r"\'e": "é",
    r"\'a": "á",
    r"\'i": "í",
    r"\'o": "ó",
    r"\'u": "ú",
    r"\'E": "É",
    r'\"o': "ö",
    r'\"u': "ü",
    r'\"a': "ä",
    r'\"O': "Ö",
    r'\"U': "Ü",
    r'\"A': "Ä",
    r'\`a': "à",
    r'\`e': "è",
    r'\`i': "ì",
    r'\`o': "ò",
    r'\`u': "ù",
    r'\~n': "ñ",
    r'\~N': "Ñ",
    r'\c{c}': "ç",
    r'\c{C}': "Ç",
    r'\ss': "ß",
    r'\aa': "å",
    r'\AA': "Å",
    r'\o': "ø",
    r'\O': "Ø",
}

def latex_to_unicode(text):
    """Convert LaTeX special characters to Unicode."""
    # Handle patterns like {\'e}, {\"o}, {\`a}, etc.
    text = re.sub(r"\{\\(['\"`~^])(\w)\}", lambda m: LATEX_TO_UNICODE.get(f"\\{m.group(1)}{m.group(2)}", m.group(0)), text)
    # Handle patterns like {\ss}, {\aa}, etc.
    text = re.sub(r"\{\\(\w+)\}", lambda m: LATEX_TO_UNICODE.get(f"\\{m.group(1)}", m.group(0)), text)
    # Handle patterns like \'{e}, \"{o}, etc. (without outer braces)
    text = re.sub(r"\\(['\"`~^])(\w)", lambda m: LATEX_TO_UNICODE.get(f"\\{m.group(1)}{m.group(2)}", m.group(0)), text)
    # Remove any remaining curly braces
    text = text.replace('{', '').replace('}', '')
    return text

# Load the .bib file
with open('/Users/chengjie/Documents/Goettingen/projects/homepage/chengjieluo.github.io/_bibliography/references.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Sort entries by year (descending)
sorted_entries = sorted(bib_database.entries, key=lambda x: x.get('year', '0'), reverse=True)

# List of papers with equal contribution authors
# 'cofirst' indicates whether the equal-contribution authors are co-first authors
coauthor_list = [
    {'name': 'ciarella2021multi',
     'authors': ['Ciarella, Simone', 'Luo, Chengjie', 'Debets, Vincent E'],
     'cofirst': True},
    {'name': 'ruscher2021glassy',
     'authors': ['Ciarella, Simone', 'Luo, Chengjie'],
     'cofirst': False},  # co-second authors, not co-first
    {'name': 'menou2023physical',
     'authors': ['Menou, Lucas', 'Luo, Chengjie'],
     'cofirst': True},
    {'name': 'luo2025theory',
     'authors': ['Luo, Chengjie', 'Hess, Nathaniel'],
     'cofirst': True},
]

# List of papers with special highlights (e.g., journal covers)
highlights = {
    'luo2021glassy': [
        {'text': 'cover', 'url': 'https://pubs.rsc.org/en/content/articlelanding/2021/SM/D1SM90156G'}
    ],
}

def get_equal_authors(entry_id):
    """Return a list of equal-contribution authors for a given entry ID."""
    for item in coauthor_list:
        if item['name'] == entry_id:
            return item['authors']
    return []

def is_cofirst(entry_id):
    """Check if the equal-contribution authors are co-first authors."""
    for item in coauthor_list:
        if item['name'] == entry_id:
            return item.get('cofirst', False)
    return False

def is_first_or_cofirst_author(entry):
    """Check if Chengjie Luo is first author or co-first author."""
    authors = entry['author'].split(' and ')
    first_author = authors[0].strip()
    entry_id = entry.get('ID', '')

    # Check if Chengjie Luo is the first author
    if 'Luo' in first_author and 'Chengjie' in first_author:
        return True
    # Check if Chengjie Luo is a co-first (equal contribution) author
    # Only count if cofirst is True
    equal_authors = get_equal_authors(entry_id)
    if equal_authors and is_cofirst(entry_id):
        if any('Luo, Chengjie' in eq for eq in equal_authors):
            return True
    return False

# def format_authors(author_string, equal_authors=None):
#     """Convert 'Last, First' to 'First Last' for each author, bold Chengjie Luo,
#     and add dagger (†) for equal-contribution authors."""
#     if equal_authors is None:
#         equal_authors = []
#     authors = author_string.split(' and ')
#     formatted = []
#     for author in authors:
#         author = author.strip()
#         original = author  # keep original "Last, First" format for matching
#         if ',' in author:
#             parts = [p.strip() for p in author.split(',', 1)]
#             name = f"{parts[1]} {parts[0]}"  # "First Last"
#         else:
#             name = author
#         # Convert LaTeX special characters to Unicode
#         name = latex_to_unicode(name)
#         # Bold Chengjie Luo
#         if 'Chengjie' in name and 'Luo' in name:
#             name = f"**{name}**"
#         # Add dagger for equal-contribution authors
#         if any(eq in original for eq in equal_authors):
#             name += "<sup>†</sup>"
#         formatted.append(name)

#     if len(formatted) > 1:
#         return ', '.join(formatted[:-1]) + ', and ' + formatted[-1]
#     return formatted[0]
def format_authors(author_string, equal_authors=None):
    """Convert 'Last, First' to 'First Last' for each author, bold Chengjie Luo,
    and add dagger (†) for equal-contribution authors."""
    if equal_authors is None:
        equal_authors = []
    authors = author_string.split(' and ')
    formatted = []
    for author in authors:
        author = author.strip()
        original = author  # keep original "Last, First" format for matching
        if ',' in author:
            parts = [p.strip() for p in author.split(',', 1)]
            name = f"{parts[1]} {parts[0]}"  # "First Last"
        else:
            name = author
        # Convert LaTeX special characters to Unicode
        name = latex_to_unicode(name)
        # Semi-bold Chengjie Luo (font-weight: 600 is between normal 400 and bold 700)
        if 'Chengjie' in name and 'Luo' in name:
            name = f'<span style="font-weight: 500;">{name}</span>'
        # Add dagger for equal-contribution authors
        if any(eq in original for eq in equal_authors):
            name += "<sup>†</sup>"
        formatted.append(name)

    if len(formatted) > 2:
        return ', '.join(formatted[:-1]) + ', and ' + formatted[-1]
    if len(formatted) == 2:
        return ' and '.join(formatted)
    
    return formatted[0]
# Count (co-)first author papers
first_author_count = sum(1 for entry in sorted_entries if is_first_or_cofirst_author(entry))

# Generate Markdown
with open('publication.markdown', 'w') as md_file:
    md_file.write('---\nlayout: page\ntitle: Publications\npermalink: /publication/\nnav_order: 4\n---\n\n')

    #Float image to the upper right of the page
    md_file.write('<div style="float: right; margin: 0 0 15px 20px; max-width: 20%;">\n')
    md_file.write('  <img src="{{ \'/assets/images/cover_full.png\' | relative_url }}" alt="Soft Matter cover" style="width: 100%;">\n')
    md_file.write('</div>\n\n')


    md_file.write(f'Totally {len(sorted_entries)} papers, including {first_author_count} (co-)first author papers.\n\n')

    md_file.write('<sup>†</sup>equal contribution\n\n')

    for i, entry in enumerate(sorted_entries, start=1):
        entry_id = entry.get('ID', '')
        equal_authors = get_equal_authors(entry_id)
        authors = format_authors(entry['author'], equal_authors)
        title = latex_to_unicode(entry['title'])  # Also convert title
        journal = latex_to_unicode(entry.get('journal', ''))  # Also convert journal
        
        volume = entry.get('volume', '')
        pages = entry.get('pages', '')
        year = entry.get('year', '')
        doi = entry.get('doi', '')

        # line = f"{i}. **{title}** <br> {authors} <br> [*{journal}*](https://doi.org/{doi}) {volume}, {pages} ({year})"

        line = f'{i}. **{title}** <br> {authors} <br> <a href="https://doi.org/{doi}" style="color: #808080;">{journal} {volume}, {pages} ({year})</a>'

         # Add highlights (e.g., cover links)
        if entry_id in highlights:
            for h in highlights[entry_id]:
                line += f' [<a href="{h["url"]}" style="color: #cc0000;">{h["text"]}</a>]'


        # print(journal)

        line += "\n\n"

        md_file.write(line)

        #### write thesis
    # phd_thesis=f'**PhD thesis**: [A First-Principles Theory of the Complex Dynamics of Glass-Forming Liquids: A Generalized Mode-Coupling Theory](https://research.tue.nl/en/publications/a-first-principles-theory-of-the-complex-dynamics-of-glass-formin/)'
    phd_thesis=f'**PhD thesis**: <a href="https://research.tue.nl/en/publications/a-first-principles-theory-of-the-complex-dynamics-of-glass-formin/" style="color: #808080;">A first-principles theory of the complex dynamics of glass-forming liquids: A generalized mode-coupling theory</a>'
    md_file.write(phd_thesis + "\n\n")
    
    # master_thesis=f'**MPhil thesis**: [Analysis of the potential landscapes of colloidal diffusion systems using the Markov state model](https://lbezone.hkust.edu.hk/bib/991012656469603412)'
    master_thesis=f'**MPhil thesis**: <a href="https://lbezone.hkust.edu.hk/bib/991012656469603412" style="color: #808080;">Analysis of the potential landscapes of colloidal diffusion systems using the Markov state model</a>'
    md_file.write(master_thesis + "\n\n")