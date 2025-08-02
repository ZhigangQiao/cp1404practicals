import wikipedia

while True:
    # Prompt the user for input
    search_input = input("Enter a page title or search phrase (or leave blank to exit): ").strip()

    # Check if the input is blank, if so, exit the loop
    if not search_input:
        break

    try:
        # Perform a search and get the page
        page = wikipedia.page(search_input, auto_suggest=False)

        # Print page details
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
        print()
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation pages
        print("Disambiguation Error: Wikipedia suggests multiple pages. Please be more specific.\n")
    except wikipedia.exceptions.PageError:
        # Handle page not found
        print("Page not found. Please try another search.\n")
