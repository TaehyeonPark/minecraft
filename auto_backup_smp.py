from pathlib import Path
from datetime import datetime
from drive_api import *

import os

backup_dir = Path("/home/minecraft/smp")

service = ls()
tabol_file_name = f"smp_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.tar.gz"
tabol_command = f"tar -cvpzf /backups/{tabol_file_name} {backup_dir}"
tabol_file = Path(f"/backups/{tabol_file_name}")

os.system(tabol_command)

upload_file(service, root, tabol_file)

os.system(f"rm {tabol_file}")
