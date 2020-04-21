import os
import recognize as voice
import recorder as rec


actions = ["INIT", "END", "TORN", "ROBA", "ERROR"]


def get_action(order):
    options = {
        "jugar començar iniciar comencem som-hi": {
            "count":    0,
            "action":   0
        },
        "acabar finalitzar fi prou tancar atura": {
            "count":    0,
            "action":   1
        },
        "et toca es el teu torn espavila va": {
            "count":    0,
            "action":   2
        },
        "ja pots robar roba carta llest": {
            "count":    0,
            "action":   3
        }
    }
    print("order")
    for word in order.split(" "):
        for opt, _ in options.items():
            if word in opt:
                options[opt]['count'] += 1

    max = -1
    maxval = 0
    for opt, _ in options.items():
        if options[opt]['count'] > maxval:
            max = options[opt]['action']
            maxval = options[opt]['count']

    return max


def controller():
    while input("Press enter to talk, q to quit\n") != 'q':
        print("Recording...")
        if rec.get_audio():
            transcription = voice.sample_recognize(rec.out_default)
            action = get_action(transcription)
            print(actions[action])
        else:
            print("Error occurred while trying to record audio.")


if __name__ == '__main__':
    controller()
    # print(get_action("carta roba"))
