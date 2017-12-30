class CreateObject:

    def BookmarkRecord(category, subcategory, url):
        return {'category':category, 'subcategory':subcategory, 'url':url}


    def PaperRecord(category, subcategory, url, abstract, title):
        return {'category':category, 'subcategory':subcategory, 'url':url, 'abstract':abstract, 'title':title}


    def NoteRecord(category, subcategory, note):
        return {'category':category, 'subcategory':subcategory, 'note':note}