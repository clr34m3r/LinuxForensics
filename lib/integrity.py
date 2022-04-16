import os
import hashlib
import shutil
from lib import api
from lib.api import bcolors


def integrityResult(folderName, rawOutp):
    try:
        outp = os.path.join(rawOutp, folderName)
        shutil.make_archive(outp, "zip", rawOutp, folderName)

        zipOutp = outp + ".zip"
        api.exeCmd("sudo chmod 777 -R " + zipOutp)

        print(bcolors.OKGREEN + "Compress files successfully!" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + "There was an error while compressing " + folderName + "!")
        print("NameError: " + str(e) + bcolors.ENDC)
    try:
        print(bcolors.OKCYAN + "Exporting encrypted SHA256 signature..." + bcolors.ENDC)
        sha256_hash = hashlib.sha256()
        with open(zipOutp, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)

        print(
            bcolors.OKGREEN
            + "Export encrypted SHA256 signature successfully!"
            + bcolors.ENDC
        )

        print(
            bcolors.OKGREEN
            + "SHA256 Signature: "
            + bcolors.ENDC
            + bcolors.HEADER
            + sha256_hash.hexdigest()
            + bcolors.ENDC
        )
    except Exception as e:
        print(
            bcolors.FAIL
            + "There was an errors while exporting "
            + folderName
            + ".zip encrypted SHA256 signature!"
        )
        print("NameError: " + str(e) + bcolors.ENDC)
