from google.appengine.ext import db


class Item(db.Model):
    name = db.StringProperty()
    price = db.FloatProperty()
    likes = db.IntegerProperty()
    active = db. BooleanProperty()
    calories = db.IntegerProperty()
    description = db.StringProperty()
    dailySpecial = db.BooleanProperty()

    """ 
    Images is a list of blob keys. the first image will be the thumbnail
    Image path will be taken care of in appengine
    """
    images = db.ListProperty(blobstore.BlobKey)

    category = db.ReferenceProperty(Category)

    """ checking newest """
    lastUpdated = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_key_from_name(cls, guestbook_name=None):
        return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')
        
class Recommendation(db.Model):
    item = db.ReferenceProperty(Item)
    recoItem = db.ReferenceProperty(Item)

    lastUpdated = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_key_from_name(cls, guestbook_name=None):
        return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

class Tablet(db.Model):
    macAdress = db.StringProperty()
    
    @classmethod
    def get_key_from_name(cls, guestbook_name=None):
        return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')



class Ping(db.Model):

    """ Ping has parent table """

    time = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_key_from_name(cls, guestbook_name=None):
        return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

class Table(db.Model):
    name = db.StringProperty()
    pairingCode = db.IntegerProperty()

    @classmethod
    def get_key_from_name(cls, guestbook_name=None):
        return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

class OrderDetail(db.Model):

  order = db.ReferenceProperty(Order)

  dateAdded = db.DateTimeProperty(auto_now_add=True)
  dateRemoved = db.DateTimeProperty(auto_now_add=True)

  itemId = ReferenceProperty(Item)

  @classmethod
  def get_key_from_name(cls, guestbook_name=None):
      return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

class Category(db.Model):
    name = db.StringProperty()
    lastUpdated = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_key_from_name(cls, guestbook_name=None):
        return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

class Order(db.Model):

  table = db.ReferenceProperty(Table)

  ratings = db.IntegerProperty()   
  statusId = db.IntegerProperty()
  dateAdded = db.DateTimeProperty(auto_now_add=True)
  dateRemoved = db.DateTimeProperty(auto_now_add=True)

  @classmethod
  def get_key_from_name(cls, guestbook_name=None):
      return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

class SpecialOffer(db.Model):
    
  discount = db.FloatProperty()
  recurring = db.BooleanProperty()

  dateStart = db.DateTimeProperty(auto_now_add=True)
  dateEnd = db.DateTimeProperty(auto_now_add=True)

  @classmethod
  def get_key_from_name(cls, guestbook_name=None):
      return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')
