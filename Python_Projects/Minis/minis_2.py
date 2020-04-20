from enum import Enum
import uuid


class PropertyType(Enum):
    ''' Enum for residence types '''
    COMMERCIAL = 1
    RESIDENTIAL = 2
    LAND = 3


class Property():
    ''' Parent Class '''

    def __init__(self, property_type_selection):
        self.property_type = PropertyType(property_type_selection)
        self.uuid = self.generate_uuid()

    @staticmethod
    def generate_uuid():
        return uuid.uuid1()


class Home(Property):
    ''' Child Class '''

    def __init__(self, home_type, listing_price, listing_type):
        super().__init__(property_type_selection=2)
        self.home_type = home_type
        self.listing_price = listing_price
        self.listing_type = listing_type

    def __repr__(self):
        return 'Home(home_type=%s, listing_price=%s, listing_type=%s)' \
            % (self.home_type, self.listing_price, self.listing_type)


class Land(Property):
    ''' Child Class '''

    def __init__(self, acreage, land_type):
        super().__init__(property_type_selection=3)
        self.acreage = acreage
        self.land_type = land_type

    def get_acreage(self):
        return f'{self.acreage} Acres'

    def __repr__(self):
        return 'Land(acreage=%s, land_type=%s)' % (self.acreage, self.land_type)


home_listing = Home('single_family', 450_000, 'for_sale')
land_listing = Land(20, 'commercial')

print(home_listing.__repr__())
print(land_listing.__repr__())
