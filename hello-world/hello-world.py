import json

def lambda_handler(event, context):
    """ 
        Route the incoming request based on type (LaunchRequest and IntentRequest)
    """
    
    if event['request']['type'] == "LaunchRequest":
        return get_welcome_response()
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])

def get_welcome_response():
    """ 
        Greet the user(s) when the skill is invoked
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Hello World Greeter!"
    
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Sorry, I didn't get that. Welcome to Hello World Greeter!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def on_intent(intent_request, session):
    """ 
        Called when the user specifies an intent for this skill 
    """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "GreetHelloWorld":
        return get_greeting_response() 
    else:
        raise ValueError("Invalid intent")

def get_greeting_response():
    """ 
        The GreetHelloWorld intent has been invoked. Let's greet the users! 
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Hello World!"
    
    reprompt_text = None
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

        
def build_response(session_attributes, speechlet_response):
    """ 
        Function used to format response in a way that Alexa can understand 
    """
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    """ 
        Function used to format response in a way that Alexa can understand 
    """
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
