import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


def cleanup_archive_dir(path: str):
    if Path(path).exists():
        logger.info(f"removing temporary unarchived pretrained model dir at {path}")
        shutil.rmtree(path)
