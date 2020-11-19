import requests


def main():
    print("Welcome Isit Down.py!")
    print("Please write a URL or URLs you want to check. (seperated by comma)")

    URLS = input().split(",")

    for URL in URLS:
        url = URL.strip(" ")
        if "https://" in url:
            if "." not in url:
                print(f"{url} is not in valid url")
            else:
                try:
                    request = requests.get(url)
                    status = request.status_code
                    if status == 200:
                        print(f"{url} is up!")
                    else:
                        print(f"{url} is down..")
                except Exception:
                    print(f"{url} is not in valid url")
        elif "https://" not in url:
            if "." not in url:
                print(f"{url} is not in valid url")
            else:
                try:
                    request = requests.get(f"https://{url}")
                    status = request.status_code
                    if status == 200:
                        print(f"{url} is up!")
                    else:
                        print(f"{url} is down..")
                except Exception:
                    print(f"{url} is not in valid url")
    ask()


def ask():
    value = input("do you want start over? y/n ")
    if value == "y":
        main()
    elif value == "n":
        print("ok bye")
    else:
        print("That's not a valid answer")
        ask()


main()
