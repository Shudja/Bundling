from os import environ

SESSION_CONFIGS = [
    dict(
        name="Shifting_Experimentation_Base",
        app_sequence=["Shifting_Exp_Base"],
        num_demo_participants=1,
    ),
    dict(
        name="Shifting_Experimentation_Bundling_Encouraged_Decreasing",
        app_sequence=["Shifting_Exp_BundlingED"],
        num_demo_participants=1,
    ),
    dict(
        name="Shifting_Experimentation_Bundling_Safe_Decreasing",
        app_sequence=["Shifting_Exp_SafeD"],
        num_demo_participants=1,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=2.50, doc=""
)

# PARTICIPANT_FIELDS = []
PARTICIPANT_FIELDS = ["Ambiguous_Display","Round1", "Payoff1","BoxChosen","CharacterChosen","Draw"
                        ,"Sequence_Used","sequence","orderFirst","orderSecond","orderThird", "envelope","random_sheet","random_row", "order", "decision_info",
                      "color1","color2","color3","color4", "part2_urns", "part2_states","part1_info"]
SESSION_FIELDS = ["Sequence0","Sequence1","Char1First","Char2First","Char1Second","Char2Second","Char1Third","Char2Third", "TimeC", "TimeB", "TimeF",
                  "TimeF2"]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = '$'
USE_POINTS = False

ROOMS = [
    dict(name="EconomicsExperiment", display_name="Economics Experiment"),
    dict(name="Test1", display_name="Test1"),
    dict(name="Test2", display_name="Test2"),
    dict(name="Test3", display_name="Test3"),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '8720610614351'
