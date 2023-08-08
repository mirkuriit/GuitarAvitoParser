import time

from parser import Parser
from guitar import Guitar
from settings import Settings
from stypes import Stypes
settings: Settings = Settings(
    sort_by=Stypes.CHEAPER,
    city="irkutsk",
    is_new=False,
    q="электрогитара"
)


settings: Settings = Settings(
    sort_by=Stypes.CHEAPER,
    city="irkutsk",
    is_new=False,
    q="электрогитара"
)
p: Parser = Parser(
    settings=settings
)

for i in range(1, 10):
    print(p.parse_guitar())
    time.sleep(5)