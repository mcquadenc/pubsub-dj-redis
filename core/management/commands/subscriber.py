from django.core.management.base import BaseCommand, CommandError
import redis 

class Command(BaseCommand):
    def handle(self, *args, **options):

        r = redis.StrictRedis(host='localhost', port=6379, db=1)
        p = r.pubsub()
        p.psubscribe('notification.*')
        for message in p.listen():
            print(message)
            if message:
                m_type = message.get('type', '')
                m_pattern = message.get('pattern', '')
                m_channel = message.get('channel', '')
                data = message.get('data', '')
                print(m_channel)
                if m_channel == 'notification.*':
                    print('A new user is connected')
                    # Published data of that user => `data`