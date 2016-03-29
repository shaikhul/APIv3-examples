import os


class InvalidAPIKeyException(Exception):
    pass


class MailChimpConfig(object):

    def __init__(self):
        ROOT_PATH = os.path.abspath(os.path.dirname(__name__))
        APIKEY_FILE_PATH = os.path.join(ROOT_PATH, 'APIKEY')

        try:
            with open(APIKEY_FILE_PATH) as f:
                api_key = f.readline()
        except IOError:
            raise InvalidAPIKeyException("Please enter your API Key into the APIKEY file as mentioned in README.md")

        self.parse_api_key(api_key)

    @classmethod
    def parse_api_key(cls, api_key):
        parts = api_key.split('-')
        if len(parts) != 2:
            msg = "This doesn't look like an API Key: {apikey}".format(apikey=api_key)
            msg += "The API Key should have both a key and a server name, separated by a dash, like this: abcdefg8abcdefg6abcdefg4-us1"
            raise InvalidAPIKeyException(msg)

        cls.apikey = api_key
        cls.shard = parts[1]
        cls.api_root = "https://{shard}.api.mailchimp.com/3.0/".format(shard=cls.shard)


if __name__ == '__main__':
    try:
        config = MailChimpConfig()
        print 'Configured properly!'
    except InvalidAPIKeyException as e:
        print e.message
