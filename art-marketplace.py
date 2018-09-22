### CLASSES ###
class Art():
  # CONSTRUCTOR #
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  # STRING REPRESENTATION #
  def __repr__(self):
    return '{artist}. "{title}". {year}, {medium}. {owner_name}, {owner_location}.'.format(artist=self.artist, title=self.title, year=self.year, medium=self.medium, owner_name=self.owner.name, owner_location=self.owner.location)
  
class Marketplace():
  # CONSTRUCTOR #
  def __init__(self):
    self.listings = []
  # METHOD | Add a listing. #
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  # METHOD | Remove a listing. #
  def remove_listing(self, r_listing):
    self.listings.remove(r_listing)
  # METHOD | Print all listings. #
  def show_listings(self):
    for listing in self.listings:
      print(listing)
      
class Client():
  # CONSTRUCTOR #
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  # METHOD | Creates listing on marketplace. #
  def sell_artwork(self, artwork, price):
    # Verify client is owner of artwork being sold. #
    if artwork.owner == self:
      # Then add this listing to the veneer marketplace. #
      veneer.add_listing(Listing(artwork, price, self))
  # METHOD | Verifys art is not currently owner and listed then executes transaction. #
  def buy_artwork(self, artwork):
    # Verify client isn't already owner of the artwork. #
    if artwork.owner != self:
      # Loop through each availible listing. #
      for listing in veneer.listings:
        # If the artwork is for sale, proceed with transaction. #
        if listing.art == artwork:
          # First save listing to a class variable. #
          art_listing = listing
          # Update the owner. #
          artwork.owner = self
          # Remove the listing. #
          veneer.remove_listing(listing)
        
class Listing():
  # CONTRSUTRCTOR #
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  #STRING REP. returns the artwork's title and price. #
  def __repr__(self):
    return "{art} PRICE: {price}".format(art=self.art.title, price=self.price)
  
    
### INSTANTIATE OBJECTS ###
# MARKETPLACE #
veneer = Marketplace()

# Show all listings #
#veneer.show_listings()

# CLIENTS #
edytta = Client("Edytta Halpirt", "Private Collection", False)
moma = Client("The MOMA", "New York", True)

# ART #
# Create 'Girl With Mandolin' painting. #
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

# Confirm 'Girl With Mandolin' has been added. #
print("*New artwork created*")
print(girl_with_mandolin)

# List Girl With Mandolin for sale on Veneer Art Marketplace. #
print("*Artwork listed for sale*")
edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")

# Show all listings for sale. #
print("ALL LISTINGS:")
veneer.show_listings()
print("~~~~~~~~~~")

# Sell 'Girl With Mandolin' to MOMA. #
moma.buy_artwork(girl_with_mandolin)
print("*Artwork purchased*")
print("*Listing removed*")

# Show updated owner. #
print("*Owner updated*")
print(girl_with_mandolin)

# Show all listings for sale. #
print("ALL LISTINGS:")
veneer.show_listings()
print("~~~~~~~~~~")













