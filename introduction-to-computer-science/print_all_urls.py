
# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link != -1:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote
    else:
        return None, 0


def print_all_links(page):
    while page != '':
        url, end_quote = get_next_target(page)
        if url:
            print url
        else:
            break
        page = page[end_quote:]

print_all_links('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com"><h1><a href="http://srikar.com"></h1>')

print get_page('http://google.com')