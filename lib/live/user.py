from lib import api
import os
import re
from lib.api import bcolors


def getLocalUsers(outp, eID):
    fName = "17.LocalUsers_" + eID
    outp = os.path.join(outp, fName)
    if not os.path.exists(outp):
        os.makedirs(outp)
    try:
        api.exeCmd("sudo cp /etc/passwd " + outp)
    except Exception as e:
        print(bcolors.FAIL + "Failed to get /etc/passwd!")
        print("NameError: " + str(e) + bcolors.ENDC)
    try:
        api.exeCmd("sudo cp /etc/shadow " + outp)
    except Exception as e:
        print(bcolors.FAIL + "Failed to get /etc/shadow!")
        print("NameError: " + str(e) + bcolors.ENDC)

    api.exeCmd("sudo chmod 777 -R " + outp)

    print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)


def readPasswd(fName):
    userInfo = []
    try:
        with open(fName, "r") as f:
            for line in f:
                entry = line.strip().split(":")
                userInfo.append(entry)
        return userInfo
    except Exception as e:
        print(bcolors.FAIL + "There was an error while reading %s!" % (fName))
        print("NameError: " + str(e) + bcolors.ENDC)
        return 0


def detectAliases(passwd, outp, eID):
    fName = "18.DetectAbnormalAccounts_" + eID + ".txt"
    id2user = {}
    abnormal = False
    try:
        checkAccTxt = open(os.path.join(outp, fName), "w")
        checkAccTxt.write("--- Detect users who share the same numerical id: ")
        for account in passwd:
            user = account[0]
            uid = account[2]
            if uid in id2user:
                abnormal = True
                checkAccTxt.write(
                    '\n- User "%s" is an alias for "%s" with uid=%s'
                    % (user, id2user[uid], uid)
                )
            else:
                id2user[uid] = user

        if abnormal == False:
            checkAccTxt.write("No abnormal users.\n\n")
        else:
            checkAccTxt.write("\n\n")
        checkAccTxt.close()
    except Exception as e:
        print(
            bcolors.FAIL
            + "There was an error while detecting users who share the same ID!"
        )
        print("NameError: " + str(e) + bcolors.ENDC)


def detectMissingUsers(passwd, shadow, outp, eID):
    fName = "18.DetectAbnormalAccounts_" + eID + ".txt"
    abnormal = False
    try:
        checkAccTxt = open(os.path.join(outp, fName), "a")
        checkAccTxt.write(
            "--- Detect users who appear in only /etc/passwd or /etc/shadow: "
        )

        passwdUsers = set([e[0] for e in passwd])
        shadowUsers = set([e[0] for e in shadow])

        missing_in_passwd = shadowUsers - passwdUsers
        if len(missing_in_passwd) > 0:
            abnormal = True
            checkAccTxt.write(
                "\n- Users missing in passwd: %s" % ", ".join(missing_in_passwd)
            )

        missing_in_shadow = passwdUsers - shadowUsers
        if len(missing_in_shadow) > 0:
            abnormal = True
            checkAccTxt.write(
                "\n- Users missing in shadow: %s" % ", ".join(missing_in_shadow)
            )

        if abnormal == False:
            checkAccTxt.write("No abnormal users.\n\n")
        else:
            checkAccTxt.write("\n\n")
        checkAccTxt.close()
    except Exception as e:
        print(
            bcolors.FAIL
            + "There was an error while detecting users who appear in only /etc/passwd or /etc/shadow!"
        )
        print("NameError: " + str(e) + bcolors.ENDC)


def detectUnshadowed(passwd, shadow, outp, eID):
    fName = "18.DetectAbnormalAccounts_" + eID + ".txt"
    abnormal = False
    try:
        checkAccTxt = open(os.path.join(outp, fName), "a")
        checkAccTxt.write("--- Detect users without a password: ")

        nopass = [e[0] for e in passwd if e[1] == ""]
        nopass.extend([e[0] for e in shadow if e[1] == ""])
        if len(nopass) > 0:
            abnormal = True
            checkAccTxt.write("\n- Users without password: %s" % ", ".join(nopass))

        unshadowed = [e[0] for e in passwd if e[1] != "x" and e[1] != ""]
        if len(unshadowed) > 0:
            abnormal = True
            checkAccTxt.write(
                "\n- Users not using password-shadowing: %s" % ", ".join(unshadowed)
            )

        if abnormal == False:
            checkAccTxt.write("No abnormal users.\n\n")
        else:
            checkAccTxt.write("\n\n")
        checkAccTxt.close()
    except Exception as e:
        print(
            bcolors.FAIL
            + "There was an error while detecting users without a password!"
        )
        print("NameError: " + str(e) + bcolors.ENDC)


def detectDeviatingHashing(shadow, outp, eID):
    fName = "18.DetectAbnormalAccounts_" + eID + ".txt"
    abnormal = False
    try:
        checkAccTxt = open(os.path.join(outp, fName), "a")
        checkAccTxt.write(
            "--- Detect non-standard hash algorithms and reusing salts for multiple user accounts: "
        )
        noalgo = set()
        salt2user = {}
        algorithms = set()
        for entry in shadow:
            pwhash = entry[1]
            if len(pwhash) < 3:
                continue

            m = re.search(r"^\$([^$]{1,2})\$([^$]+)\$", pwhash)
            if not m:
                noalgo.add(entry[0])
                continue

            algo = m.group(1)
            salt = m.group(2)

            if salt in salt2user:
                checkAccTxt.write(
                    '\n- Users "%s" and "%s" share same password salt "%s"'
                    % (salt2user[salt], entry[0], salt)
                )
            else:
                salt2user[salt] = entry[0]

            algorithms.add(algo)

        if len(algorithms) > 1:
            abnormal = True
            checkAccTxt.write(
                "\n- Multiple hashing algorithms found: %s" % ", ".join(algorithms)
            )

        if len(noalgo) > 0:
            abnormal = True
            print("Users without hash algorithm spec. found: %s" % ", ".join(noalgo))

        if abnormal == False:
            checkAccTxt.write("No abnormal users.\n\n")
        else:
            checkAccTxt.write("\n\n")
        checkAccTxt.close()
    except Exception as e:
        print(
            bcolors.FAIL
            + "There was an error while detecting non-standard hash algorithms and reusing salts for multiple user accounts!"
        )
        print("NameError: " + str(e) + bcolors.ENDC)


def detectAbnormalAccounts(outp, eID):
    try:
        fName = "18.DetectAbnormalAccounts_" + eID + ".txt"
        passwd = readPasswd("/etc/passwd")
        shadow = readPasswd("/etc/shadow")
        if passwd != 0:
            detectAliases(passwd, outp, eID)
        if passwd != 0 and shadow != 0:
            detectMissingUsers(passwd, shadow, outp, eID)
            detectUnshadowed(passwd, shadow, outp, eID)
        if shadow != 0:
            detectDeviatingHashing(shadow, outp, eID)
        print(bcolors.OKGREEN + fName + " export successfully!" + bcolors.ENDC)
    except Exception as e:
        print(
            bcolors.FAIL
            + "There was an error while exporting "
            + fName
            + "! See destination file for more info."
        )
        print("NameError: " + str(e) + bcolors.ENDC)
