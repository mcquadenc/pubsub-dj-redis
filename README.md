# How publish
```
from pubsub import pub
import json

pub.publish_data_on_redis(json.dumps({'message': 'teste msg sent'}), 'notification.new')
```

# How subscribe

```
python manage.py subscriber
```

or 

```
redis-cli
> psubscribe notification.*
```



