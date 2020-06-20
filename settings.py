from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
       name='trust_game_low',
       display_name="Trust game low",
       num_demo_participants=2,
       app_sequence=['my_trust', 'payment_info'],
       multiplication_factor=3
    ),
    dict(
        name='trust_game_high',
        display_name="Trust game high",
        num_demo_participants=2,
        app_sequence=['my_trust', 'payment_info'],
        multiplication_factor=4
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'v*lczl+n+of(f6r@hjn$g9y-b)1e5(to4)um646i(8hux$5gq)'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
