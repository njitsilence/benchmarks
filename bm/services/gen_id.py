import re
import random
from datetime import datetime


class GenID(object):

    def __init__(self, user_id):
        self.user_id = str(user_id)
        self.timestamp = re.sub(r'\D', '', str(datetime.today())[2:])
        self.random_num = str(random.randint(0, 99)).zfill(2)

    def generate_prod_id(self):

        return 'prod' + self.user_id + self.timestamp + self.random_num

    def generate_sku_id(self):

        return 'sku' + self.user_id + self.timestamp + self.random_num

