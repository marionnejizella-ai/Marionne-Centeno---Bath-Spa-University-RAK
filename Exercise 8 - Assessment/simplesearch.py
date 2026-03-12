#Exercise 8: Simple Search
#Marionne Jizella E. Centeno
def simple_search(data_list, query):
    """
    Search for items in data_list that contain the query string.
    """
    results = [item for item in data_list if query.lower() in item.lower()]
    return results

def main():
    # Sample data to search
    data_list = [
        "Apple",
        "Banana",
        "Orange",
        "Grapes",
        "Mango",
        "Pineapple",
        "Watermelon"
    ]

    print("Welcome to Simple Search!")
    query = input("Enter the word to search: ")

    results = simple_search(data_list, query)

    if results:
        print("\nSearch Results:")
        for item in results:
            print("- " + item)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
