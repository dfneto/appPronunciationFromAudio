import os
import all_words

path = "/Users/david/PycharmProjects/pythonProject/audios/"


def generate_59s_mono_audio_from(audio_name):
    os.system(f"ffmpeg -y -i {path}{audio_name}.mp4 -ac 1 -ss 00:05:00.000 -to 00:05:59.000"
              f" ../audios/{audio_name}_59s_mono.wav")


def generate_words_audio_from(audio_name):
    word_counter = {}
    for word, time_stamp in all_words.dictionary.items():
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
        if time_stamp[1] - time_stamp[0] <= 0.11:
            pass
        else:
            os.system(f"ffmpeg -y -i {path}{audio_name}.wav "
                      f"-ss 00:00:{time_stamp[0]} -to 00:00:{time_stamp[1] + 0.1} "
                      f"../audios_generated/{word}_{word_counter[word]}.wav")


# generate_59s_mono_audio_from("the_miracle_morning_hal_elrold")
generate_words_audio_from("brand_1")
