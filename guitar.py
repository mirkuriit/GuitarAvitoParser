class Guitar:
    def __init__(self, price, title, descr, date, link):
        self.price = price
        self.title = title
        self.descr = descr
        self.date = date
        self.link = link

    def __str__(self):
        return f"""{self.title[:50]} {self.link} \n{self.price}"""

