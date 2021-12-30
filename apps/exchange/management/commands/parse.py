from typing import Any, Optional
from django.core.management.base import BaseCommand
from apps.exchange.parse import MainSiteParser


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        payload = {
            "rtype": "3",
            "ucstep": "1",
            "exam": "0",
            "datafrom": "01.12.2021",
            "dataend": "31.12.2021",
            "formo": "2",
            "formob": "1",
            "prdis": "0"
        }
        parser = MainSiteParser.build_parser("http://inet.ibi.spb.ru/raspisan/rasp.php", payload)
        parser.parse()
