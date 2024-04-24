import requests

def len_joke():
    joke = get_joke()
    # print(joke)
    # for i, char in enumerate(joke):
        # print(f'{i}. {char}')
    return len(joke)


def get_joke():
    URL = 'https://official-joke-api.appspot.com/jokes/random'
    
    try:
        response = requests.get(URL, timeout=30)
        response.raise_for_status()

    except requests.exceptions.Timeout:
        return "No Jokes"

    except requests.exceptions.ConnectionError:
        pass

    except requests.exceptions.HTTPError:
        return 'HTTPError was raise'

    else:
        if response.status_code == 200:
            joke = response.json()['setup'] + '\n' + response.json()['punchline']
        else:
            joke = 'No Jokes'
    

    return joke


# if __name__ == '__main__':
#     print('Length of joke:', len_joke())
