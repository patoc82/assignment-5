import requests


def get_student_seed():
    student_key = input("Student key: ")
    return sum(ord(ch) for ch in student_key.strip())


def get_sku():
    while True:
        sku = input("SKU: ").strip()

        if sku.upper() == "DONE":
            return "DONE"

        if sku:
            return sku

        print("SKU cannot be blank. Try again.")


def get_on_hand():
    while True:
        try:
            on_hand = int(input("On hand: "))

            if on_hand >= 0:
                return on_hand

            print("On-hand quantity cannot be negative.")
        except ValueError:
            print("Invalid quantity. Enter a whole number.")


def get_threshold(seed):
    if seed % 3 == 0:
        return 15
    elif seed % 3 == 1:
        return 12
    else:
        return 9


def check_api(term):
    url = "https://itunes.apple.com/search"
    parameters = {
        "entity": "song",
        "limit": 5,
        "term": term
    }

    try:
        response = requests.get(
            url,
            params=parameters,
            timeout=10
        )
        response.raise_for_status()

    except requests.RequestException:
        return "N/A", "FAILED"

    try:
        data = response.json()

        if not isinstance(data, dict):
            return "N/A", "INVALID_RESPONSE"

        if "results" not in data:
            return "N/A", "INVALID_RESPONSE"

        results = data["results"]

        if not isinstance(results, list):
            return "N/A", "INVALID_RESPONSE"

        for item in results:
            if not isinstance(item, dict) or "kind" not in item:
                return "N/A", "INVALID_RESPONSE"

        song_count = 0

        for item in results:
            if item["kind"] == "song":
                song_count += 1

        return song_count, "OK"

    except (ValueError, TypeError, KeyError):
        return "N/A", "INVALID_RESPONSE"


def main():
    seed = get_student_seed()
    threshold = get_threshold(seed)

    total_skus = 0
    reorder_count = 0

    while True:
        sku = get_sku()

        if sku == "DONE":
            break

        on_hand = get_on_hand()
        total_skus += 1

        if on_hand < threshold:
            reorder_count += 1
            print(f"{sku}: REORDER")
        else:
            print(f"{sku}: OK")

    if seed % 2 == 0:
        term = "weezer"
    else:
        term = "drake"

    songs_returned, api_status = check_api(term)

    print(f"Seed: {seed}")
    print(f"Threshold: {threshold}")
    print(f"SKUs entered: {total_skus}")
    print(f"Reorder flagged: {reorder_count}")
    print(f"Spotcheck term: {term}")
    print(f"Songs returned: {songs_returned}")
    print(f"API status: {api_status}")


if __name__ == "__main__":
    main()