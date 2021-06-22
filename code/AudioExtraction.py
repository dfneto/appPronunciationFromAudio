import os
import all_words
import transcribe

path2 = "/Users/david/PycharmProjects/pythonProject/audios/"
path = "/Users/david/DEV/app_pronunciation_files/"
path_audios_generated = "/Users/david/PycharmProjects/pythonProject/audios_generated/"


def generate_59s_mono_audio_from(audio_name):
    os.system(f"ffmpeg -y -i {path}{audio_name}.mp4 -ac 1 -ss 00:05:00.000 -to 00:05:29.000 "
              f" ../audios/{audio_name}_29s_mono.wav")


def generate_words_audio_from(audio_name):
    word_counter = {}
    counter = 0
    for word, time_stamp in all_words.dictionary.items():
        # count_the_number_of_repeated_words(word, word_counter)
        os.system(f"ffmpeg -y -i {path2}{audio_name} -ss 00:00:{time_stamp[0]} -to 00:00:{time_stamp[1] + 0.1} "
                      f"../audios_generated/{counter}_{word}.wav")
        counter += 1


# TODO: it is not working because I'm using a dictionary. I should use a list instead
def count_the_number_of_repeated_words(word, word_counter):
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1


def speeding_up_slowing_down_audio(audio_name, speed):
    os.system(f"ffmpeg -y -i {path2}{audio_name}.wav -filter:a \"atempo={speed}\" "
              f" ../audios/{audio_name}_{speed}x.wav")


def speed_up_all_files(speed):
    audios_directory = [audio for audio in os.listdir("../audios_generated/") if "wav" in audio]
    for audio in audios_directory:
        os.system(f"ffmpeg -y -i {path_audios_generated}{audio} -filter:a \"atempo={speed}\" "
                  f" ../audios_generated_normal_speed/{audio}")


# generate_59s_mono_audio_from("the_miracle_morning_hal_elrold")
# speeding_up_slowing_down_audio("the_miracle_morning_hal_elrold_29s_mono", 0.5)
# transcribe.transcribe_file_with_word_time_offsets("../audios/the_miracle_morning_hal_elrold_29s_mono.wav")
#2- tenho que manualmente copiar de all_words.txt para all_words.py e colocar dentro da variavel dictionary
generate_words_audio_from("../audios/the_miracle_morning_hal_elrold_29s_mono.wav")
# speed_up_all_files(2)


