import os
import all_words
import transcribe

path2 = "/Users/david/PycharmProjects/pythonProject/audios/"
path = "/Users/david/DEV/app_pronunciation_files/"


def generate_59s_mono_audio_from(audio_name):
    os.system(f"ffmpeg -y -i {path}{audio_name}.mp4 -ac 1 -ss 00:05:00.000 -to 00:05:59.000"
              f" ../audios/{audio_name}_59s_mono.wav")


def generate_words_audio_from(audio_name):
    word_counter = {}
    counter = 0
    for word, time_stamp in all_words.dictionary.items():
        # count_the_number_of_repeated_words(word, word_counter)
        if time_stamp[1] - time_stamp[0] <= 0.11:
            pass
        else:
            os.system(f"ffmpeg -y -i {path2}{audio_name} "
                      f"-ss 00:00:{time_stamp[0]} -to 00:00:{time_stamp[1] + 0.1} "
                      f"../audios_generated/{counter}_{word}.wav")
        counter += 1


# TODO: it is not working because I'm using a dictionary. I should use a list instead
def count_the_number_of_repeated_words(word, word_counter):
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1


generate_59s_mono_audio_from("the_miracle_morning_hal_elrold")
#1- transcribe.transcribe_file_with_word_time_offsets("../audios/the_miracle_morning_hal_elrold_59s_mono.wav")
#2- tenho que manualmente copiar de all_words.txt para all_words.py e colocar dentro da variavel dictionary
#3- generate_words_audio_from("../audios/the_miracle_morning_hal_elrold_59s_mono.wav")

