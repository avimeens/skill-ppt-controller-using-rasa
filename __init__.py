from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class PptControllerUsingRasaSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('PptControllerUsingRasa'))
    def handle_ppt_controller_using_rasa(self, message):
        self.speak_dialog('ppt.controller.using.rasa')


def create_skill():
    return PptControllerUsingRasaSkill()

