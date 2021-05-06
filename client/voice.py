import speech_recognition


class Voice:

    def __init__(self):

        self.recognizer = speech_recognition.Recognizer()
        self.microphone = speech_recognition.Microphone()

    def get_voice_and_accuracity(self, real_answer, answer: str = None):

        if answer is None:
            answer = self.record_and_recognize_audio()
        s = 0

        answer = " " + answer + " "

        # Проверяем количество вхождений ключевых слов
        for i in real_answer:
            if isinstance(i, str):
                if i in answer:
                    s += 1
            else:
                for k in i:
                    if k in answer:
                        s += 1
                        break

        # Вычисляем точность ответа
        accuracity = min((s / len(real_answer)) * 100, 100)

        return accuracity

    def record_and_recognize_audio(self, *args: tuple):
        """
        Запись и распознавание аудио
        """
        with self.microphone:
            recognized_data = ""

            # регулирование уровня окружающего шума
            self.recognizer.adjust_for_ambient_noise(self.microphone, duration=2)

            try:
                print("начинаем прослушивание...")
                audio = self.recognizer.listen(self.microphone, 5, 5)

            except speech_recognition.WaitTimeoutError:
                print("Проверьте микрофон?")
                return

            # использование online-распознавания через Google
            try:
                print("Начинаем преобразование в текст...")
                recognized_data = self.recognizer.recognize_google(audio, language="ru").lower()

            except speech_recognition.UnknownValueError:
                pass

            # в случае проблем с доступом в Интернет происходит выброс ошибки
            except speech_recognition.RequestError:
                print("Пожалуйста, проверьте подключение к интернету")

            return recognized_data.lower()


if __name__ == "__main__":
    voice = Voice()
    test = [[" провожу ", " тестир"], [" тест ", " прогр"]]
    print("Ответь на вопрос, что ты сейчас делаешь")

    while True:
        answer = voice.record_and_recognize_audio()
        print(f"Ваш ответ: {answer}")

        if input("Это ваш ответ? д/н: ").lower() == "д":
            break

    print("Точность ответа на тестовый вопрос:", voice.get_voice_and_accuracity(test, answer), "%")
