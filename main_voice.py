import speech_recognition


class Voice:

    def __init__(self):

        self.recognizer = speech_recognition.Recognizer()
        self.microphone = speech_recognition.Microphone()

    def record_and_recognize_audio(self, *args: tuple):
        """
        Запись и распознавание аудио
        """
        with self.microphone:
            recognized_data = ""

            # регулирование уровня окружающего шума
            self.recognizer.adjust_for_ambient_noise(self.microphone, duration=2)

            try:
                print("Listening...")
                audio = self.recognizer.listen(self.microphone, 5, 5)

            except speech_recognition.WaitTimeoutError:
                print("Микро?")
                return

            # использование online-распознавания через Google
            try:
                print("Started recognition...")
                recognized_data = self.recognizer.recognize_google(audio, language="ru").lower()

            except speech_recognition.UnknownValueError:
                pass

            # в случае проблем с доступом в Интернет происходит выброс ошибки
            except speech_recognition.RequestError:
                print("Check your Internet Connection, please")

            return recognized_data


if __name__ == "__main__":
    voice = Voice()
    try:
        answer = voice.record_and_recognize_audio().lower()
        print("Ответ:", answer)

        real_answer = ["никита", ["бог", "красавчик"]]
        s = 0

        for i in real_answer:
            if type(i) == type(str()):
                if i in answer:
                    s += 1
            else:
                for k in i:
                    if k in answer:
                        s += 1
                        break
            print(s)
        accuracity = (s / len(real_answer)) * 100
        print(f"Точность ответа: {accuracity}%")

    except:
        pass