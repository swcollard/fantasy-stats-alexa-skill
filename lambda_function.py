"""
Alexa Skill for fetching fantasy football stats
"""

from __future__ import print_function
from nfl_client import fetch_player_name_map

players = fetch_player_name_map(2017, 6)


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Fantasy Football Stats"
    speech_output = "Welcome to the Fantasy Football Stats Skill. " \
                    "Ask for stats by saying, " \
                    "how many points does Tom Brady have this week?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Ask for stats by saying, " \
                    "how many points does Tom Brady have this week?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Adios!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_player_stat_attributes(player_name, points):
    return {"playerName": player_name, "points": points}


def get_stats_for_player(intent, session):
    """ Gets the current stats for a given player
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Athlete' in intent['slots']:
        player_name = intent['slots']['Athlete']['value']
        if player_name.lower() in players:
            p = players[player_name.lower()]
            speech_output = str(p)
            session_attributes = create_player_stat_attributes(p.name, p.week_pts)
        else:
            speech_output = "Sorry, I can't find stats for " + player_name
    else:
        speech_output = "Please ask for a player name to get stats."
    reprompt_text = "Ask for stats by saying, " \
                    "how many points does Tom Brady have this week?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_season_stats_for_player(intent, session):
    """ Gets the current stats for a given player
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Athlete' in intent['slots']:
        player_name = intent['slots']['Athlete']['value']
        if player_name.lower() in players:
            p = players[player_name.lower()]
            speech_output = player_name + ' has ' + str(p.season_pts) + ' this season.'
            session_attributes = create_player_stat_attributes(p.name, p.season_pts)
        else:
            speech_output = "Sorry, I can't find stats for " + player_name
    else:
        speech_output = "Please ask for a player name to get stats."
    reprompt_text = "Ask for stats by saying, " \
                    "how many points does Tom Brady have this week?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "PlayerStats":
        return get_stats_for_player(intent, session)
    if intent_name == "PlayerSeasonStats":
        return get_season_stats_for_player(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.8a1b6688-cecc-4451-8760-1b9db895fb85"):
        raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
