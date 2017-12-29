from google.cloud import datastore

class GoogleDatastore:

    def __init__(self):
        self.client = datastore.Client.from_service_account_json('/home/egregori/mysite/keyfile.json')

    def query(self, kind, filters=[[]]):
        self.query = self.client.query(kind=kind)
        if filters[0]:
            for filter in filters:
                self.query.add_filter(filter[0], filter[1], filter[2])
        return list(self.query.fetch())



test = GoogleDatastore()
print(test.query('paper'))
