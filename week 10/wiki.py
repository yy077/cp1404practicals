import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError


def main():
    """Prompt user for Wikipedia page titles, print summary until blank input."""
    while True:
        search_term = input("Enter page title: ").strip()
        if not search_term:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(search_term, autosuggest=False)
            print(page.title)
            print(wikipedia.summary(search_term, sentences=2))
            print(page.url)
        except PageError:
            print(f'Page id "{search_term}" does not match any pages. Try another id!')
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)


if __name__ == "__main__":
    main()