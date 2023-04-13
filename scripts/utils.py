def clean_input(prompt: str=''):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("You interrupted Auto-Llama")
        print("Quitting...")
        exit(0)

