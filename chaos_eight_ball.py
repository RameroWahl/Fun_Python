import random

def magic_chaos_ball():
    responses = [
        "Eat the banana peel and all.",
        "Sell your car for a wheel of cheese.",
        "Yes, but only if you're wearing socks on your hands.",
        "No, unless you ask again in a dramatically different accent.",
        "Consult your nearest houseplant for guidance.",
        "The answer lies in the void. Stare at it long enough.",
        "Spin in a circle three times, then ask again.",
        "Your fate is now determined by the next pigeon you see.",
        "Absolutely, but at what cost?",
        "Not in this timeline. Try another one.",
        "Go outside and howl at the moon. The answer will come.",
        "Only if you can recite the alphabet backward while juggling."
    ]
    
    input("Ask the Magic Chaos Ball a question: ")
    print(random.choice(responses))

if __name__ == "__main__":
    magic_chaos_ball()
