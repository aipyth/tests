import re
import pdb
from main import Window

class TestObj(object):
    def __init__(self, file_name='test.txt'):
        self.file = None
        self.offset = 1
        self.iterator = 0
        try:
            with open(file_name, 'r') as file_object:
                tags_to_delete = ['<startblock>', '']
                split_temp = re.compile('<startblock>|<endblock>')

                file_object = file_object.read()
                file_object = re.split(split_temp, file_object)
                for i, item in enumerate(file_object):
                    file_object[i] = file_object[i].split('\n')
                for block in file_object:
                    while True:
                        try:
                            block.remove('')
                        except ValueError:
                            break
                for item in file_object:
                    if len(item) == 0:
                        del file_object[file_object.index(item)]

                self.file = file_object

        except FileNotFoundError as message:
            print(message)
            # send signal to handler

    def get_name(self):
        if self.file[0][0].startswith('name:'):
            self.file[0][0] = re.sub('name:', '', self.file[0][0])
            if self.file[0][0].startswith(' '):
                return self.file[0][0][1:]
            return self.file[0][0]
        else:
            return ''

    def get_question(self):
        if self.offset >= len(self.file):
            return '<Questions ended>'

        try:
            if self.file[self.offset][0].startswith('question:'):
                self.file[self.offset][0] = re.sub('question:', '', self.file[self.offset][0])
                return self.file[self.offset][0]
            else:
                return ''
        except IndexError:
            return ''

    def get_answers(self):
        if self.offset >= len(self.file):
            return None
        try:
            answers = []
            for i in range(1, len(self.file[self.offset])):
                if self.file[self.offset][i].startswith('answer-true'):
                    self.file[self.offset][i] = re.sub('answer-true:', '', self.file[self.offset][i])
                    answers.append(self.file[self.offset][i])
                    break
            for i in range(1, len(self.file[self.offset])):
                if self.file[self.offset][i].startswith('answer-false:'):
                    self.file[self.offset][i] = re.sub('answer-false:', '', self.file[self.offset][i])
                    answers.append(self.file[self.offset][i])
            self.offset += 1
            return answers
        except IndexError:
            return None

    def count_questions(self):
        counter = -1
        for i in self.file:
            counter += 1
        return counter
