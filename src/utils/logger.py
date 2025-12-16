import logging


def configure_logging(level: int = logging.INFO) -> None: 
    logging.basicConfig(
        level=level, 
        datefmt="%Y-%m-%d %H:%M:%S",
        format="%(asctime)s | %(levelname)-5s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
        handlers=[
            logging.FileHandler("../app.log"),
            logging.StreamHandler()
        ]
    )
