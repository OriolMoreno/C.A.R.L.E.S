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


def testVoiceRecognition():
    final_score = 0
    print("---------------------------------------")
    print("        TEST 1: INICIAR PARTIDA        ")
    print("---------------------------------------")
    audio = "AudioTests/init.flac"
    transcription = voice.sample_recognize(audio)
    action = get_action(transcription)
    print("Correct action: INIT\nOutput action: %s" % actions[action])
    if actions[action] == 'INIT':
        final_score += 1
        print("TEST 1 OK\n")
    else:
        print("TEST 1 ERROR\n")

    print("---------------------------------------")
    print("        TEST 2: ACABAR PARTIDA         ")
    print("---------------------------------------")
    audio = "AudioTests/end.flac"
    transcription = voice.sample_recognize(audio)
    action = get_action(transcription)
    print("Correct action: END\nOutput action: %s" % actions[action])
    if actions[action] == 'END':
        final_score += 1
        print("TEST 2 OK\n")
    else:
        print("TEST 2 ERROR\n")

    print("---------------------------------------")
    print("          TEST 3: CANVI TORN           ")
    print("---------------------------------------")
    audio = "AudioTests/torn.flac"
    transcription = voice.sample_recognize(audio)
    action = get_action(transcription)
    print("Correct action: TORN\nOutput action: %s" % actions[action])
    if actions[action] == 'TORN':
        final_score += 1
        print("TEST 3 OK\n")
    else:
        print("TEST 3 ERROR\n")

    print("---------------------------------------")
    print("          TEST 4: ROBAR CARTA          ")
    print("---------------------------------------")
    audio = "AudioTests/robar.flac"
    transcription = voice.sample_recognize(audio)
    action = get_action(transcription)
    print("Correct action: ROBA\nOutput action: %s" % actions[action])
    if actions[action] == 'ROBA':
        final_score += 1
        print("TEST 4 OK\n")
    else:
        print("TEST 4 ERROR\n")

    print("---------------------------------------")
    print("             TEST 5: ERROR             ")
    print("---------------------------------------")
    audio = "AudioTests/error.flac"
    transcription = voice.sample_recognize(audio)
    action = get_action(transcription)
    print("Correct action: ERROR\nOutput action: %s" % actions[action])
    if actions[action] == 'ERROR':
        final_score += 1
        print("TEST 5 OK\n")
    else:
        print("TEST 5 ERROR\n")

    print("\nTOTAL CORRECTES: %s de 5" % final_score)
    if final_score >= 5:
        print("-- TOTS ELS TESTS SUPERATS --")


if __name__ == '__main__':
    # controller()
    # print(get_action("carta roba"))
    testVoiceRecognition()
