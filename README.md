# How publish
```pub.publish_data_on_redis(json.dumps({'message': 'teste msg sent'}), 'notification.new')```

# How subscribe

```
pub.publish_data_on_redis(json.dumps({'message': 'teste msg sent'}), 'notification.new')
```

or 

```
redis-cli
> psubscribe notification.*
```



