import re
from sqlalchemy import and_
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from msg_template import Template, engine, Base


Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()

def addTemplate(place=None):
	if place is None:
		place = raw_input('Which placeholder is this template for? ')
	templateName = raw_input('Enter the name of your template')
	templateValue =  raw_input('What should ' + templateName + 'be replaced with?')
	new_template = Template(placeholder=place,replacementName=templateName,replacementText=templateValue)
	session.add(new_template)
	session.commit()
	return session.query(Template).filter(and_(Template.replacementName==templateName, Template.replacementText==templateValue)).first()


def findFirstReplacable(paragraph):
	m = re.search('{{(\w|\d)+?}}',paragraph)	
	if (m):
		return m.group(0)

def loadTemplate(templateName = None):
	if (templateName is None):
		templateName = 'basicTemplate'
	possibleTemplates = session.query(Template).filter(Template.placeholder==templateName)
	print[template.replacementName for template in possibleTemplates]
	choice = raw_input('Choose your template, or enter custom for custom')
	
	template = None
	if (choice == 'custom'):
		template = addTemplate(place=templateName)
	else:
		myTemplate = session.query(Template).filter(and_(Template.placeholder==templateName, Template.replacementName==choice))
		if len( myTemplate.all()) == 1:
			template = myTemplate.first()
	
	if template is not None:
		return template.replacementText
	else:
		print("error loading template")
		return loadTemplate(templateName)
def start():
	print("1. Create template")
	print("2. Create message")
	action = raw_input('enter your option: ')
	if action == '1':
		addTemplate()
	elif action == '2':
		paragraph = loadTemplate()
		while (findFirstReplacable(paragraph) is not None):
			result = loadTemplate(findFirstReplacable(paragraph))
			paragraph = re.sub(re.compile(findFirstReplacable(paragraph)),result, paragraph)
		print(paragraph)
	start()

start()
