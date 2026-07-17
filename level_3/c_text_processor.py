"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f'Total text length: {len(self.text)}'


# код писать тут
class AdvancedTextProcessor(TextProcessor):

    def summarize(self):

        return super().summarize() + f', total number of words in the text: {len(self.text.split())}'

if __name__ == '__main__':

    any_text = 'any some some any text'

    
    text_proc1 = TextProcessor(any_text)

    print(text_proc1.to_upper())
    print(text_proc1.summarize())


    ad_text_proc1 = AdvancedTextProcessor(any_text)

    print(ad_text_proc1.to_upper())
    print(ad_text_proc1.summarize())
