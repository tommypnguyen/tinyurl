class Short:

    """
    This class will take a large url and a short url representation of it
    A user can take this short url to take them to the long url
    Example:
        input: https://www.google.com/search?qfqfqf
        output: https://short.com/asdfa
    """
    # we will need 5 character digits to make 916,137,832
    # a-z, 0-9, A-Z
    # rfc: https://www.ietf.org/rfc/rfc1738.txt
    # 26 + 10 + 26 = 62
    # 1 million urls in 6 months
    # 2 million urls in 12 months
    # 16 million urls in 8 years for an average life of a company
    # facebook.com/abc123

    BASE_TINY_URL = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
                     12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w',
                     23: 'x', 24: 'y', 25: 'z', 26: 'A', 27: 'B', 28: 'C', 29: 'D', 30: 'E', 31: 'F', 32: 'G', 33: 'H',
                     34: 'I', 35: 'J', 36: 'K', 37: 'L', 38: 'M', 39: 'N', 40: 'O', 41: 'P', 42: 'Q', 43: 'R', 44: 'S',
                     45: 'T', 46: 'U', 47: 'V', 48: 'W', 49: 'X', 50: 'Y', 51: 'Z', 52: '0', 53: '1', 54: '2', 55: '3',
                     56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9'}

    # Variable representing our base
    BASE = 62

    # Variable representing url
    URL_TEMPLATE = "http://www.uRshort.us/"

    def __init__(self):
        self.count = 0
        self.urls = {}

    def convert_large_to_short(self, large_url: str):
        """
        This function will take a large url and convert it into a tinyurl
        :param large_url: str
        :return: tinyurl: str
        """

        # check if large url is in dict
        if large_url in self.urls:
            # if it already exists
            return self.URL_TEMPLATE + self.convert_count_to_tinyurl(self.urls.get(large_url))

        self.urls[large_url] = self.count

        # get the count and convert it to the tinyurl
        tinyurl = self.convert_count_to_tinyurl(self.count)

        # increment count
        self.count += 1

        # return the url
        return self.URL_TEMPLATE + tinyurl

    def convert_short_to_large(self, tinyurl: str):
        """
        This function will take a tinyurl and convert into a large_url
        :param tinyurl: str
        :return: large_url: str
        """

        # check if tinyurl begins with URL_Template, else returns
        if tinyurl.startswith(Short.URL_TEMPLATE):
            tinyurl = self.parse_url(tinyurl)
            count = self.convert_tinyurl_to_count(tinyurl)

            # iterate through url dict, if value is found return key
            for k, v in self.urls.items():
                if self.urls[k] == count:
                    return k

        return "Does not exist"

    def convert_count_to_tinyurl(self, count: int):
        """
        This function will take a count integer and convert into a tinyurl
        :param count: int
        :return: tinyurl: str
        """

        values = []

        if count == 0:
            return self.BASE_TINY_URL.get(count)

        while count > 0:

            # Mod by base and add to list
            values.insert(0, count % Short.BASE)

            # whole number divide by base to get next index
            count = count // Short.BASE

        return self.parse_list_of_values(values)

    def convert_tinyurl_to_count(self, tinyurl: str):
        """
        This function will take a tinyurl and convert into a count integer
        :param tinyurl : str
        :return: count : int
        """
        # parse url and init a reverse map dict
        tinyurl = self.parse_url(tinyurl)
        count = 0
        temp_len = len(tinyurl)-1
        temp_dict = self.flip_dict(Short.BASE_TINY_URL)

        for i in tinyurl:
            # retrieve value and increment value to count
            value = temp_dict.get(i)
            count += value * Short.BASE**temp_len
            temp_len -= 1

        return count

# Private functions

    @staticmethod
    def parse_list_of_values(values: list):

        """
        This function takes a list of integers and converts them into a tinyurl representation
        :param values: list of integers
        :return: tinyurl : str
        """

        tinyurl = ""
        for i in values:
            tinyurl += (Short.BASE_TINY_URL.get(i))

        return tinyurl

    @staticmethod
    def flip_dict(base_map: dict):
        """
        This function takes a dictionary and returns a new dict with the key-value pairs switched
        :param base_map: dict
        :return: new_dict: dict
        """

        new_dict = {}

        for k, v in base_map.items():
            new_dict[v] = k

        return new_dict

    @staticmethod
    def parse_url(tinyurl: str):
        """
        This function will take a url and return the end of the url
        :param tinyurl: str
        :return: new_url : str
        """

        new_url = tinyurl[len(Short.URL_TEMPLATE):]

        return new_url










