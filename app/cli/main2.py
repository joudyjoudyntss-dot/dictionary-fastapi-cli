import sys
import requests
diction_url='http://127.0.0.1:8000/words'
def search_word(word_name):
    try:
        response=requests.get(f'{diction_url}/{word_name}')
        if response.status_code==404:
            print(f"{response.json()['detail']}")
            return
        data = response.json()
        print("\n" + "="*40)
        print(f" Word: {data['word'].upper()}")
        print(f" Definition: {data['definition']}")
        if data['example']:
            print(f" Example: \"{data['example']}\"")
        print("="*40)
    except requests.exceptions.ConnectionError:
        print("the api doesnt work")

def add_word(word, definition, example=None):
    payload = {
        "word": word,
        "definition": definition,
        "example": example
    }
    try:
        response = requests.post(diction_url, json=payload)
        if response.status_code == 201:
            print(f'add to dictionary{word}succsessfully')
        else:
            print(f"wrong {response.json()['detail']}")
    except requests.exceptions.ConnectionError:
        print("the server doesnt work")

def main():
    args = sys.argv[1:]
    
    if not args:
        print("usage")
        print("   search: python -m cli.main search [word]")
        print("   add: python -m cli.main add [word] [defenition] [choice_example]")
        return

    command = args[0]
    
    if command == "search" and len(args) > 1:
        search_word(args[1])
    elif command == "add" and len(args) > 2:
        word = args[1]
        definition = args[2]
        example = args[3] if len(args) > 3 else None
        add_word(word, definition, example)
    else:
        print("wrong")

if __name__ == "__main__":
    main()