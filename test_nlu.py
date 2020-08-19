from rasa_nlu.model import Metadata, Interpreter


class TestClass(object):
    interpreter = Interpreter.load('./models/current/nlu')
    def test_greet(self):
        intent = self.interpreter.parse(u"hi")['intent']['name']
        assert intent == 'greet'

    def test_bye(self):
        intent = self.interpreter.parse(u"bye")['intent']['name']
        assert intent == 'goodbye'

    def test_booksearch(self):
        intent = self.interpreter.parse(u"I want to read books about Fiction")['intent']['name']
        value = self.interpreter.parse(u"I want to read books about Fiction")['entities'][0]['value']
        entity = self.interpreter.parse(u"I want to read books about Fiction")['entities'][0]['entity']
        assert intent == 'book_search'
        #assert value == 'Fiction'
        #assert entity == 'book_type'
    
    def test_booksearch2(self):
        intent = self.interpreter.parse(u"recommend some books about Classics")['intent']['name']
        value = self.interpreter.parse(u"recommend some books about Classics")['entities'][0]['value']
        entity = self.interpreter.parse(u"recommend some books about Classics")['entities'][0]['entity']
        assert intent == 'book_search'
        #assert value == 'Classics'
        #assert entity == 'book_type'

