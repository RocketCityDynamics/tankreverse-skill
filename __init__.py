from mycroft import MycroftSkill, intent_file_handler


class Tankreverse(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tankreverse.intent')
    def handle_tankreverse(self, message):
        self.speak_dialog('tankreverse')


def create_skill():
    return Tankreverse()

