# Do not edit the following link
import shayo
try:
   connect = "https://shayo.cps.com:7075/app?client=69547"
   shayo.connect(connect)
   # token
   shayo.login(shayo.get[i].token())
if shayo.error==true:
   print("We got an error:" + shayo.errors + "\nYou send e-mail to shayo@godhub.com to support")
if shayo.perm==true:
   print("We got an permission error from " + shayo.perms + "\nWe send the logs to developer shayo now")
   shayo.send(shayo.perms)
if shayo.perk == "expired":
   print("You bot expired perk II, Please wait for moment to rebuy perk again")
if shayo.build == "bx":
   print("Building you bot, you have received administration mode to edit/build")
