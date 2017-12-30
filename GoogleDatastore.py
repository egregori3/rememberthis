from google.cloud import datastore

class GoogleDatastore:

    def __init__(self):
        self.client = datastore.Client.from_service_account_json('/home/egregori/mysite/keyfile.json')

    def query(self, kind, filters=[[]]):
        query = self.client.query(kind=kind)
        if filters[0]:
            for filter in filters:
                query.add_filter(filter[0], filter[1], filter[2])
        return list(query.fetch())

    def put(self, kind, data):
        entity = datastore.Entity(key=self.client.key(kind))
        for key, value in data.items():
            entity[key] = value
        self.client.put(entity)


test = GoogleDatastore()
print(test.query('paper'))
print(test.query('bookmark'))