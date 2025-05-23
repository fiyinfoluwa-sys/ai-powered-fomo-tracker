# main.py

from data_fetcher import get_fomo_data, load_favorites, save_favorites

def display_trends(trends):
    print("\nToday's FOMO trends from Reddit:")
    for i, trend in enumerate(trends, 1):
        print(f"{i}. {trend['title']} ({trend['score']} upvotes)")
        print(f"   URL: {trend['url']}\n")

def display_favorites(favorites):
    if favorites:
        print("\nYour Favorites:")
        for i, fav in enumerate(favorites, 1):
            print(f"{i}. {fav['title']} ({fav['score']} upvotes)")
            print(f"   URL: {fav['url']}\n")
    else:
        print("\nYou have no favorites yet.")

def main():
    favorites = load_favorites()

    while True:
        print("\nMenu:")
        print("1. View trends")
        print("2. View favorites")
        print("3. Add trend to favorites")
        print("4. View Top Reddit Trends")
        print("5. Remove favorite")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            trends = get_fomo_data()
            display_trends(trends)

        elif choice == "2":
            display_favorites(favorites)

        elif choice == "3":
            trends = get_fomo_data()
            display_trends(trends)
            to_add = input("Enter the number of the trend to add: ").strip()
            if to_add.isdigit():
                idx = int(to_add) - 1
                if 0 <= idx < len(trends):
                    if trends[idx] not in favorites:
                        favorites.append(trends[idx])
                        save_favorites(favorites)
                        print(f"Added '{trends[idx]['title']}' to favorites.")
                    else:
                        print("That trend is already in your favorites.")
                else:
                    print("Invalid trend number.")
            else:
                print("Please enter a valid number.")

        elif choice == "4":
            print("🔻 Top Reddit Trends 🔻")
            reddit_trends = get_fomo_data()
            display_trends(reddit_trends)

        elif choice == "5":
            display_favorites(favorites)
            to_remove = input("Enter the number of the favorite to remove: ").strip()
            if to_remove.isdigit():
                idx = int(to_remove) - 1
                if 0 <= idx < len(favorites):
                    removed = favorites.pop(idx)
                    save_favorites(favorites)
                    print(f"Removed '{removed['title']}' from favorites.")
                else:
                    print("Invalid favorite number.")
            else:
                print("Please enter a valid number.")

        elif choice == "6":
            print("Goodbye! Stay in the know 😉")
            break
        else:
            print("Invalid choice. Please enter a number 1–6.")

if __name__ == "__main__":
    main()

