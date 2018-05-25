from mycroft import MycroftSkill, intent_handler


class PptControllerUsingRasaSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.url = "http://135.222.162.94:8001"
        self.file_opened = False

    def initialize(self):
        self.register_rasa_intent('ppt.contoller.using.rasa',
        self.handle_ppt_controller_using_rasa)
        self.register_rasa_intent('open.json', self.handle_ppt_open)

    def handle_ppt_controller_using_rasa(self, message):
        self.speak_dialog('ppt.controller.using.rasa')

    def handle_ppt_open(self, message):
	filename = message.data.get("filename")
	if filename is None:
		self.speak_dialog('ppt.specifyfile')
	else:	
		self.enclosure.mouth_text("Nova opening file " + filename)
		self.file_opened = True;
		# Send a rest request
		param = {'filename':filename}
		self.enclosure.mouth_text("Sending request to " + self.url);
		#response = requests.get(self.url, param)
		response = requests.codes.ok
		resp = {'filename' : filename}
		#if response.status_code == requests.codes.ok:
		if response == requests.codes.ok:
        		self.speak_dialog('ppt.open', data=resp)
		else: 
			self.speak_dialog('ppt.filenotfound')

def create_skill():
    return PptControllerUsingRasaSkill()

